"""
多会话管理器 — 创建/切换/删除会话，持久化到 data/conversations.json
"""
from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

MAX_HISTORY_TURNS = 5
MAX_SESSIONS = 50


@dataclass
class Session:
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])
    title: str = "新对话"
    messages: list[tuple[str, str]] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


class SessionManager:

    def __init__(self, data_dir: Path) -> None:
        self._file = data_dir / "conversations.json"
        self._sessions: dict[str, Session] = {}
        self._current_id: str = ""
        self._load()

    @property
    def current(self) -> Session | None:
        return self._sessions.get(self._current_id)

    @property
    def current_id(self) -> str:
        return self._current_id

    @property
    def sessions(self) -> dict[str, Session]:
        return self._sessions

    def new_session(self) -> Session:
        if len(self._sessions) >= MAX_SESSIONS:
            oldest = min(self._sessions.values(), key=lambda s: s.created_at)
            del self._sessions[oldest.id]
        session = Session()
        self._sessions[session.id] = session
        self._current_id = session.id
        self._save()
        return session

    def switch_to(self, session_id: str) -> Session | None:
        if session_id in self._sessions:
            self._current_id = session_id
            return self._sessions[session_id]
        return None

    def delete(self, session_id: str) -> bool:
        if session_id not in self._sessions or len(self._sessions) <= 1:
            return False
        del self._sessions[session_id]
        if self._current_id == session_id:
            self._current_id = next(iter(self._sessions))
        self._save()
        return True

    def add_message(self, question: str, answer: str) -> None:
        if not self.current:
            return
        self.current.messages.append((question, answer))
        if len(self.current.messages) > MAX_HISTORY_TURNS:
            self.current.messages = self.current.messages[-MAX_HISTORY_TURNS:]
        self._save()

    def set_title(self, title: str) -> None:
        if self.current:
            self.current.title = title
            self._save()

    def get_history(self, session_id: str | None = None) -> list[tuple[str, str]]:
        sid = session_id or self._current_id
        session = self._sessions.get(sid)
        return list(session.messages) if session else []

    def _save(self) -> None:
        data = {sid: {"id": s.id, "title": s.title, "messages": s.messages, "created_at": s.created_at}
                for sid, s in self._sessions.items()}
        self._file.parent.mkdir(parents=True, exist_ok=True)
        self._file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def _load(self) -> None:
        if not self._file.exists():
            self.new_session()
            return
        try:
            raw = json.loads(self._file.read_text(encoding="utf-8"))
            for sid, data in raw.items():
                self._sessions[sid] = Session(
                    id=data.get("id", sid), title=data.get("title", "新对话"),
                    messages=[tuple(m) for m in data.get("messages", [])],
                    created_at=data.get("created_at", ""),
                )
        except Exception:
            pass
        if not self._sessions:
            self.new_session()
        else:
            self._current_id = next(iter(self._sessions))
