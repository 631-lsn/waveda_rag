# 收藏夹搜索空白容错设计

## 问题

收藏夹搜索目前只通过 `.replace(" ", "")` 移除普通半角空格。连续半角空格通常可以匹配，但从网页、PDF 或富文本复制的不换行空格、全角空格、Tab 和换行没有统一处理，导致视觉上相似的查询无法稳定命中。

当前 `main` 还在后续收藏夹 UI 重构中移除了 `favoritesSearchInput` 和 `favoritesNoResults` 对象名，造成既有界面回归测试失败。搜索控件本身仍存在，但自动验证基线不再可靠。

## 设计

- 新增纯函数 `normalize_favorite_search_text(text: object) -> str`。
- 归一化先执行 `str(text).casefold()`，再通过 `"".join(...split())` 移除所有 Unicode 空白字符。
- `favorite_matches()` 对查询以及问题、回答的组合文本使用同一归一化函数，再执行子串匹配。
- `favorite_score()` 使用同一归一化结果计算紧凑文本命中次数，避免过滤与排序采用不同的空白规则。
- 空查询或只包含空白字符的查询继续匹配全部收藏。
- `highlight_keywords()` 保持现状；跨空白命中可能无法整段高亮，但不影响搜索结果显示。
- 恢复搜索框 `favoritesSearchInput` 和无结果标签 `favoritesNoResults` 的对象名，不改变视觉样式或交互。

## 验证

- 覆盖普通空格增加、普通空格缺失、Tab、换行、不换行空格和全角空格。
- 覆盖纯空白查询仍返回全部收藏。
- 覆盖问题与回答字段都使用相同规则。
- 恢复并运行现有收藏夹对话框测试。
- 运行完整测试集、`compileall` 和 `git diff --check`。
