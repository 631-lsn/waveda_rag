from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any
from uuid import NAMESPACE_URL, uuid4, uuid5

from raggg.config import Settings, load_dotenv_file


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class DesktopStore:
    """Persistent desktop data with sanitized frontend-facing payloads."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.data_dir = settings.data_dir
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.conversations_path = self.data_dir / "conversations.json"
        self.favorites_path = self.data_dir / "favorites.json"
        self.env_path = settings.project_root / "config" / ".env"

    def bootstrap_payload(self) -> dict[str, Any]:
        env = load_dotenv_file(self.env_path)
        theme = env.get("RAG_THEME", "dark")
        locale = env.get("RAG_LANGUAGE", "zh")
        theme = theme if theme in {"dark", "light"} else "dark"
        locale = locale if locale in {"zh", "en"} else "zh"
        api_key = env.get("RAG_LLM_API_KEY", self.settings.llm_api_key)
        index_status, chunk_count = self._index_status()
        return {
            "locale": locale,
            "theme": theme,
            "apiConfigured": bool(api_key.strip()),
            "model": env.get("RAG_LLM_MODEL", self.settings.llm_model),
            "baseUrl": env.get("RAG_LLM_BASE_URL", self.settings.llm_base_url),
            "chunkCount": chunk_count,
            "indexStatus": index_status,
            "watcherStatus": "active",
            "conversations": self.list_conversations(),
            "favorites": self.list_favorites(),
        }

    def list_conversations(self) -> list[dict[str, Any]]:
        records = self._read_list(self.conversations_path)
        return sorted(records, key=lambda item: item.get("updatedAt", ""), reverse=True)

    def get_conversation(self, conversation_id: str) -> dict[str, Any]:
        for conversation in self.list_conversations():
            if conversation.get("id") == conversation_id:
                return conversation
        raise KeyError("Conversation not found.")

    def save_turn(
        self,
        conversation_id: str | None,
        question: str,
        answer: str,
        sources: list[dict[str, Any]],
        warning: str | None = None,
    ) -> dict[str, Any]:
        conversations = self._read_list(self.conversations_path)
        conversation = next(
            (item for item in conversations if item.get("id") == conversation_id),
            None,
        )
        timestamp = _now()
        if conversation is None:
            conversation = {
                "id": conversation_id or str(uuid4()),
                "title": self._conversation_title(question),
                "createdAt": timestamp,
                "updatedAt": timestamp,
                "messages": [],
            }
            conversations.append(conversation)
        messages = conversation.setdefault("messages", [])
        messages.extend(
            [
                {
                    "id": str(uuid4()),
                    "role": "user",
                    "content": question,
                    "createdAt": timestamp,
                },
                {
                    "id": str(uuid4()),
                    "role": "assistant",
                    "content": answer,
                    "createdAt": timestamp,
                    "sources": sources,
                    "warning": warning,
                },
            ]
        )
        conversation["updatedAt"] = timestamp
        self._write_list(self.conversations_path, conversations)
        return conversation

    def rename_conversation(self, conversation_id: str, title: str) -> dict[str, Any]:
        cleaned = title.strip()
        if not cleaned:
            raise ValueError("Conversation title cannot be empty.")
        conversations = self._read_list(self.conversations_path)
        for conversation in conversations:
            if conversation.get("id") == conversation_id:
                conversation["title"] = cleaned[:80]
                conversation["updatedAt"] = _now()
                self._write_list(self.conversations_path, conversations)
                return conversation
        raise KeyError("Conversation not found.")

    def delete_conversation(self, conversation_id: str) -> bool:
        conversations = self._read_list(self.conversations_path)
        remaining = [item for item in conversations if item.get("id") != conversation_id]
        if len(remaining) == len(conversations):
            return False
        self._write_list(self.conversations_path, remaining)
        return True

    def list_favorites(self) -> list[dict[str, Any]]:
        records = self._read_list(self.favorites_path)
        normalized: list[dict[str, Any]] = []
        for index, item in enumerate(records):
            favorite = dict(item)
            if not favorite.get("id"):
                legacy_key = "|".join(
                    [
                        str(index),
                        str(favorite.get("question", "")),
                        str(favorite.get("answer", "")),
                        str(favorite.get("time", "")),
                    ]
                )
                favorite["id"] = str(uuid5(NAMESPACE_URL, f"raggg-favorite:{legacy_key}"))
            if not favorite.get("createdAt"):
                favorite["createdAt"] = favorite.pop("time", "") or _now()
            else:
                favorite.pop("time", None)
            normalized.append(favorite)
        return normalized

    def save_favorite(self, question: str, answer: str) -> dict[str, Any]:
        if not question.strip() or not answer.strip():
            raise ValueError("A favorite requires both a question and an answer.")
        favorites = self.list_favorites()
        favorite = {
            "id": str(uuid4()),
            "question": question.strip(),
            "answer": answer.strip(),
            "createdAt": _now(),
        }
        favorites.append(favorite)
        self._write_list(self.favorites_path, favorites)
        return favorite

    def delete_favorite(self, favorite_id: str) -> bool:
        favorites = self.list_favorites()
        remaining = [item for item in favorites if item.get("id") != favorite_id]
        if len(remaining) == len(favorites):
            return False
        self._write_list(self.favorites_path, remaining)
        return True

    def save_settings(self, update: dict[str, Any]) -> dict[str, Any]:
        env = load_dotenv_file(self.env_path)
        mapping = {
            "baseUrl": "RAG_LLM_BASE_URL",
            "model": "RAG_LLM_MODEL",
            "apiKey": "RAG_LLM_API_KEY",
            "theme": "RAG_THEME",
            "locale": "RAG_LANGUAGE",
            "wavedaRoot": "WAVEDA_ROOT",
            "wavedaHelpRoot": "WAVEDA_HELP_ROOT",
            "wavedaExampleRoot": "WAVEDA_EXAMPLE_ROOT",
        }
        for field, key in mapping.items():
            if field in update and update[field] is not None:
                env[key] = str(update[field]).strip()
        if env.get("RAG_THEME", "dark") not in {"dark", "light"}:
            raise ValueError("Unsupported theme.")
        if env.get("RAG_LANGUAGE", "zh") not in {"zh", "en"}:
            raise ValueError("Unsupported locale.")
        self.env_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"{key}={value}" for key, value in env.items()]
        self.env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return self.bootstrap_payload()

    def _index_status(self) -> tuple[str, int]:
        chunks_path = self.data_dir / "index" / "chunks.json"
        vectors_path = self.data_dir / "index" / "vectors.npy"
        if not chunks_path.exists() or not vectors_path.exists():
            return "missing", 0
        try:
            chunks = json.loads(chunks_path.read_text(encoding="utf-8"))
            return "ready", len(chunks) if isinstance(chunks, list) else 0
        except (OSError, ValueError):
            return "error", 0

    @staticmethod
    def _conversation_title(question: str) -> str:
        cleaned = " ".join(question.split())
        return (cleaned[:36] + "…") if len(cleaned) > 36 else cleaned

    @staticmethod
    def _read_list(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return []
        return payload if isinstance(payload, list) else []

    @staticmethod
    def _write_list(path: Path, records: list[dict[str, Any]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(
            json.dumps(records, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temporary.replace(path)
