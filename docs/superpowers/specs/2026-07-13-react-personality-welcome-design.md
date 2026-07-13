# React GUI 六人格欢迎语完整接入设计

## 目标

把 `main` 分支已有的默认、御姐、甜妹、小狗、小猫、牛马六种人格接入新 React GUI。人格不仅改变欢迎页文案，也必须改变模型回答 Prompt，避免出现“界面换了、回答没换”的假切换。

## 选择的方案

采用完整接入方案：新 GUI 设置页提供人格选择，桌面桥接持久化当前人格，bootstrap 返回人格标识，欢迎页根据人格和语言选择三段专属文案，Prompt 构建器注入相同人格指令。

不采用纯前端文案方案，因为它不会改变模型行为；也不采用只读取旧配置的方案，因为新 GUI 用户无法直接切换人格。

## 后端

- 从当前 `main` 的人格实现回接六个人格定义，保存在独立的 `generation/personality.py`。
- `DesktopStore.bootstrap_payload()` 返回 `personality`，默认值为 `normal`。
- `DesktopStore.save_settings()` 接收并验证 `personality`，写入 `RAG_PERSONALITY`。非法值返回明确错误，不污染配置。
- `DesktopBridge` 保存设置后刷新当前人格，使下一次回答无需重启即可使用新语气。
- `build_prompt()` 在角色说明之前注入当前语言对应的人格 Prompt。

## React GUI

- `BootstrapPayload` 和 `SettingsUpdate` 增加六值联合类型 `Personality`。
- 设置页增加“人格”标签页，以六张选择卡显示人格名称与简短说明；保存时与其他设置一起提交。
- 欢迎页根据 `locale + personality` 显示专属标题、介绍和补充说明。
- 人格设置保存成功后，`App` 已有 bootstrap 更新路径会立即刷新欢迎页；不要求重启。
- 已有对话消息、参考来源、模型选择和加载状态不受影响。

## 文案边界

六套中文和英文欢迎语以 React 端类型化常量维护。默认人格继续保持专业简洁；其余五种沿用 `main` 已有语气，但不在技术信息中加入过量拟声词，保证 WavEDA 内容仍可读。

## 测试与验收

- Python：验证默认人格、保存/重载、非法人格拒绝、Prompt 注入。
- React：验证六人格欢迎文案映射、设置页保存人格、`App` 使用 bootstrap 人格渲染欢迎页。
- 完整运行 Python 测试、前端测试、TypeScript 检查和生产构建。
- 独立启动桌面实例，检查人格设置页与欢迎页布局；不发送真实模型请求。
