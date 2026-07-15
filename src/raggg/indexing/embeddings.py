from __future__ import annotations

import hashlib
import math
import re

import numpy as np


TOKEN_RE = re.compile(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]+")
CHINESE_RE = re.compile(r"^[\u4e00-\u9fff]+$")


def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    for match in TOKEN_RE.finditer(text):
        value = match.group(0).lower()
        if not CHINESE_RE.match(value):
            tokens.append(value)
            continue
        tokens.extend(value)
        tokens.extend(value[index : index + 2] for index in range(len(value) - 1))
    return tokens


class HashedEmbeddingModel:
    def __init__(self, dimensions: int = 384) -> None:
        self.dimensions = dimensions

    def embed_text(self, text: str) -> np.ndarray:
        vector = np.zeros(self.dimensions, dtype=np.float32)
        for token in tokenize(text):
            digest = hashlib.md5(token.encode("utf-8")).digest()
            index = int.from_bytes(digest[:4], "little") % self.dimensions
            sign = 1.0 if digest[4] % 2 == 0 else -1.0
            vector[index] += sign
        norm = math.sqrt(float(np.dot(vector, vector)))
        if norm > 0:
            vector /= norm
        return vector

    def embed_many(self, texts: list[str]) -> np.ndarray:
        if not texts:
            return np.zeros((0, self.dimensions), dtype=np.float32)
        return np.vstack([self.embed_text(text) for text in texts])
