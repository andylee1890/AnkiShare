# Release 索引

`index.json` 是 AnkiShare 面向网站的机器可读主索引。它参考 `reciter-resources/release-records/index.json` 的组织方式，将卡组摘要和全部版本历史集中在一个文件中。

## 结构

- `schemaVersion`：索引结构版本。
- `generatedAt`：索引生成时间。
- `decks`：按卡组聚合的目录，包含名称、册数、难度、简介、功能、当前版本和版本顺序。
- `releases`：按版本平铺的完整记录，包含状态、发布时间、Release 地址、下载资产、大小、SHA-256、官网和历史 AnkiWeb 地址。
- `status`：当前索引只收录真实存在且可公开下载的 `published` Release。

网站通常先读取 `decks` 展示卡组列表，再按 `latestVersion` 从 `releases` 找到当前下载信息；需要版本历史时读取同一卡组的 `versions`。

索引只记录真实 GitHub Release 资产，不把操作失败、草稿或撤销的 Release 写入索引，也不把 `.apkg` 文件提交到 Git。新增或更新卡组时，应先完成 Release，再更新索引中的 `decks` 和 `releases`，并校验下载文件名、大小和 SHA-256。
