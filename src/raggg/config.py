from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _resolve_path(value: str, root: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return root / path


def _resolve_optional_path(value: str | None, root: Path) -> Path | None:
    if not value or not value.strip():
        return None
    return _resolve_path(value.strip(), root)


def load_dotenv_file(path: Path) -> dict[str, str]:
    """Load simple KEY=VALUE lines without requiring python-dotenv."""
    if not path.exists():
        return {}
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


@dataclass(frozen=True)
class Settings:
    project_root: Path
    waveda_root: Path | None
    waveda_help_root: Path
    waveda_example_root: Path | None
    obsidian_vault_root: Path
    data_dir: Path
    embedding_model: str
    llm_base_url: str
    llm_api_key: str
    llm_model: str

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> "Settings":
        values = dict(os.environ if env is None else env)
        project_root = Path(values.get("RAGGG_PORTABLE_ROOT", str(PROJECT_ROOT)))
        values.setdefault("WAVEDA_HELP_ROOT", "wavEDA_docs/helpHtml/helpHtml")
        values.setdefault("OBSIDIAN_VAULT_ROOT", "knowledge_base")
        return cls(
            project_root=project_root,
            waveda_root=_resolve_optional_path(values.get("WAVEDA_ROOT", ""), project_root),
            waveda_help_root=_resolve_path(
                values.get("WAVEDA_HELP_ROOT", "wavEDA_docs/helpHtml/helpHtml"),
                project_root,
            ),
            waveda_example_root=_resolve_optional_path(values.get("WAVEDA_EXAMPLE_ROOT", ""), project_root),
            obsidian_vault_root=_resolve_path(
                values.get("OBSIDIAN_VAULT_ROOT", "knowledge_base"),
                project_root,
            ),
            data_dir=_resolve_path(values.get("RAG_DATA_DIR", "data"), project_root),
            embedding_model=values.get("RAG_EMBEDDING_MODEL", "local-hashed-vectors"),
            llm_base_url=values.get("RAG_LLM_BASE_URL", "https://api.deepseek.com"),
            llm_api_key=values.get("RAG_LLM_API_KEY", ""),
            llm_model=values.get("RAG_LLM_MODEL", "deepseek-chat"),
        )


def load_settings() -> Settings:
    portable_root = Path(os.environ.get("RAGGG_PORTABLE_ROOT", str(PROJECT_ROOT)))
    dotenv_values = load_dotenv_file(portable_root / "config" / ".env")
    if not dotenv_values:
        dotenv_values = load_dotenv_file(portable_root / ".env")
    merged = dict(os.environ)
    merged.update(dotenv_values)
    return Settings.from_env(merged)
