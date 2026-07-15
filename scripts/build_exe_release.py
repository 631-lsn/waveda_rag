from __future__ import annotations

import json
import shutil
import struct
import subprocess
import sys
import zipfile
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP_NAME = "WavEDA_Assistant"
DIST_DIR = ROOT / "dist"
APP_DIR = DIST_DIR / APP_NAME
TEXT_SUFFIXES = {".md", ".txt", ".json", ".csv", ".html", ".htm"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".webp"}
ARCHIVE_ROOT = "WavEDA"


def _run(*args: str) -> None:
    print(">", " ".join(args), flush=True)
    subprocess.run(args, cwd=ROOT, check=True)


def _create_windows_icon() -> None:
    """Wrap the existing 96x96 PNG in a Windows ICO container."""
    source = ROOT / "wavEDA_docs" / "helpHtml" / "image" / "助手图标.png"
    target = ROOT / "build" / "waveda.ico"
    png = source.read_bytes()
    target.parent.mkdir(parents=True, exist_ok=True)
    header = struct.pack("<HHH", 0, 1, 1)
    entry = struct.pack("<BBBBHHII", 96, 96, 0, 0, 1, 32, len(png), 22)
    target.write_bytes(header + entry + png)


def _portable_text(text: str) -> str:
    replacements = (
        (r"D:\Staid\app\waveda\documentation\helpHtml", r"wavEDA_docs\helpHtml\helpHtml"),
        (r"D:\Staid\app\waveda\Example", "Example"),
        (r"D:\Staid\app\waveda", "<WAVEDA_ROOT>"),
        (str(ROOT), "."),
        (str(ROOT).replace("\\", "/"), "."),
    )
    for source, replacement in replacements:
        text = text.replace(source, replacement)
    return text


def _sanitize_release_text() -> None:
    roots = (APP_DIR / "knowledge_base", APP_DIR / "data", APP_DIR / "config")
    for root in roots:
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if path.suffix.lower() == ".json":
                try:
                    value = json.loads(path.read_text(encoding="utf-8"))
                except (UnicodeDecodeError, json.JSONDecodeError):
                    continue

                def sanitize_json(item):
                    if isinstance(item, str):
                        return _portable_text(item)
                    if isinstance(item, list):
                        return [sanitize_json(child) for child in item]
                    if isinstance(item, dict):
                        return {key: sanitize_json(child) for key, child in item.items()}
                    return item

                path.write_text(
                    json.dumps(sanitize_json(value), ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            sanitized = _portable_text(text)
            if sanitized != text:
                path.write_text(sanitized, encoding="utf-8")


def _copy_release_files() -> None:
    for name in ("knowledge_base", "wavEDA_docs"):
        shutil.copytree(ROOT / name, APP_DIR / name, dirs_exist_ok=True)

    shutil.copytree(ROOT / "data" / "index", APP_DIR / "data" / "index", dirs_exist_ok=True)
    (APP_DIR / "data" / "favorites.json").write_text("[]\n", encoding="utf-8")
    # conversations.json is intentionally omitted; the app creates a clean session on first launch.
    (APP_DIR / "data" / "conversations.json").unlink(missing_ok=True)

    config_dir = APP_DIR / "config"
    config_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "config" / ".env.example", config_dir / ".env.example")
    _write_release_env(config_dir / ".env")
    shutil.copy2(ROOT / "README-EXE.md", APP_DIR / "使用说明.md")
    _sanitize_release_text()


def _read_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def _write_release_env(target: Path) -> None:
    local = _read_env(ROOT / "config" / ".env")
    api_key = local.get("RAG_LLM_API_KEY", "")
    if not api_key:
        raise RuntimeError("The local API key is empty; refusing to create a preconfigured release.")
    release_values = {
        "RAG_LANGUAGE": local.get("RAG_LANGUAGE", "zh"),
        "RAG_THEME": local.get("RAG_THEME", "light"),
        "RAG_PERSONALITY": local.get("RAG_PERSONALITY", "normal"),
        "RAG_LLM_BASE_URL": local.get("RAG_LLM_BASE_URL", "https://api.deepseek.com"),
        "RAG_LLM_API_KEY": api_key,
        "RAG_LLM_MODEL": local.get("RAG_LLM_MODEL", "deepseek-chat"),
        "WAVEDA_ROOT": "",
        "WAVEDA_HELP_ROOT": "wavEDA_docs/helpHtml/helpHtml",
        "WAVEDA_EXAMPLE_ROOT": "",
    }
    target.write_text(
        "\n".join(f"{key}={value}" for key, value in release_values.items()) + "\n",
        encoding="utf-8",
    )


def _validate_release() -> None:
    required = (
        APP_DIR / f"{APP_NAME}.exe",
        APP_DIR / "data" / "index" / "chunks.json",
        APP_DIR / "data" / "index" / "vectors.npy",
        APP_DIR / "knowledge_base",
        APP_DIR / "wavEDA_docs",
        APP_DIR / "config" / ".env.example",
    )
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(f"Release is incomplete: {missing}")
    release_env = _read_env(APP_DIR / "config" / ".env")
    if not release_env.get("RAG_LLM_API_KEY"):
        raise RuntimeError("The release API key is missing.")
    if release_env.get("WAVEDA_ROOT") or release_env.get("WAVEDA_EXAMPLE_ROOT"):
        raise RuntimeError("Personal WavEDA folders must be empty in the release.")
    if release_env.get("WAVEDA_HELP_ROOT") != "wavEDA_docs/helpHtml/helpHtml":
        raise RuntimeError("The release help folder must use the bundled relative path.")
    if (APP_DIR / "data" / "conversations.json").exists():
        raise RuntimeError("Private conversation history must not be included in a release.")

    chunks = json.loads((APP_DIR / "data" / "index" / "chunks.json").read_text(encoding="utf-8"))
    if not chunks:
        raise RuntimeError("The packaged knowledge index is empty.")

    leaks: list[str] = []
    for root in (APP_DIR / "knowledge_base", APP_DIR / "data", APP_DIR / "config"):
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "D:\\Staid" in text or r"D:\\Staid" in text or "D:/Staid" in text:
                leaks.append(str(path.relative_to(APP_DIR)))
    if leaks:
        raise RuntimeError(f"Private local paths remain in release files: {leaks[:10]}")
    print(f"Validated {len(chunks)} packaged knowledge chunks; no private settings or paths found.")


def _make_zip() -> Path:
    archive_base = DIST_DIR / f"{APP_NAME}_Windows_{date.today():%Y%m%d}"
    archive = archive_base.with_suffix(".zip")
    archive.unlink(missing_ok=True)
    with zipfile.ZipFile(archive, "w", allowZip64=True) as output:
        for path in sorted(APP_DIR.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(APP_DIR)
            archive_name = (Path(ARCHIVE_ROOT) / relative).as_posix()
            compression = zipfile.ZIP_STORED if path.suffix.lower() in IMAGE_SUFFIXES else zipfile.ZIP_DEFLATED
            output.write(path, archive_name, compress_type=compression, compresslevel=6)

    with zipfile.ZipFile(archive) as check:
        bad_member = check.testzip()
        if bad_member:
            raise RuntimeError(f"ZIP CRC validation failed: {bad_member}")
        longest = max((len(name) for name in check.namelist()), default=0)
        if longest > 200:
            raise RuntimeError(f"ZIP contains an extraction-unfriendly path ({longest} characters).")
    return archive


def main() -> int:
    _create_windows_icon()
    _run(sys.executable, "-B", str(ROOT / "scripts" / "build_knowledge_base.py"))
    _run(
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        str(ROOT / "packaging" / "WavEDA_Assistant.spec"),
    )
    _copy_release_files()
    _validate_release()
    archive = _make_zip()
    print(f"\nRelease folder: {APP_DIR}")
    print(f"Release archive: {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
