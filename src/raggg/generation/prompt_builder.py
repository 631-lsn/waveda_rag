from __future__ import annotations

import re

from raggg.i18n import get_text
from raggg.retrieval.retriever import SearchResult


def build_prompt(question: str, sources: list[SearchResult]) -> str:
    snippets = []
    for index, result in enumerate(sources, start=1):
        chunk = result.chunk
        snippets.append(
            f"[{index}] {chunk.title} | {chunk.source_type} | {chunk.relative_path}\n"
            f"{chunk.content[:900]}"
        )
    joined = "\n\n".join(snippets)
    if joined.strip():
        context = (
            f"{get_text('prompt_context_label')}：\n{joined}\n\n"
            f"{get_text('prompt_context_instruction')}"
        )
    else:
        context = get_text("prompt_no_context")
    return (
        f"{get_text('prompt_role')}\n\n"
        f"{get_text('prompt_question_prefix')}：{question}\n\n"
        f"{context}\n\n"
        f"{get_text('prompt_final_instruction')}"
    )


def build_local_answer(question: str, sources: list[SearchResult]) -> str:
    if not sources:
        return get_text("local_answer_no_sources")
    top = sources[:3]
    lines = [
        get_text("local_answer_title"),
        "",
        f"{get_text('local_answer_points')}：",
    ]
    for index, result in enumerate(top, start=1):
        chunk = result.chunk
        snippet = _source_snippet(chunk.title, chunk.content)
        lines.append(f"- [{index}] {chunk.title}：{snippet}")
    lines.append("")
    lines.append(f"{get_text('local_answer_sources')}：")
    for index, result in enumerate(top, start=1):
        chunk = result.chunk
        lines.append(f"[{index}] {chunk.title} | {chunk.source_type} | {chunk.relative_path}")
    return "\n".join(lines)


def _source_snippet(title: str, content: str, limit: int = 180) -> str:
    snippet = re.sub(r"\s+", " ", content).strip()
    prefix_tokens = (title, "WavEDA")
    changed = True
    while changed:
        changed = False
        for token in prefix_tokens:
            trimmed = _strip_heading_token(snippet, token)
            if trimmed != snippet:
                snippet = trimmed
                changed = True
    if len(snippet) <= limit:
        return snippet
    return snippet[:limit].rstrip(" ，。；、") + "..."


def _strip_heading_token(text: str, token: str) -> str:
    if not token or not text.startswith(token):
        return text
    rest = text[len(token) :]
    if rest and rest[0] not in " \t\r\n：:-|":
        return text
    return rest.strip(" ：:-|")
