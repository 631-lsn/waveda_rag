from __future__ import annotations

import re

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
    return (
        "你是一个中文 RAG 助手。只根据给定资料回答；资料不足时可用自己的知识补充回答。\n\n"
        f"问题：{question}\n\n"
        f"资料：\n{joined}\n\n"
        "请给出简洁、可操作的回答，并列出引用。"
    )


def build_local_answer(question: str, sources: list[SearchResult]) -> str:
    if not sources:
        return "资料中没有足够依据回答这个问题。"
    top = sources[:3]
    lines = ["根据当前知识库，先给出可确认的信息。", "", "要点："]
    for index, result in enumerate(top, start=1):
        chunk = result.chunk
        snippet = _source_snippet(chunk.title, chunk.content)
        lines.append(f"- [{index}] {chunk.title}：{snippet}")
    lines.append("")
    lines.append("引用来源：")
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
