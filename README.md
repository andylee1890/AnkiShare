<p align="center">
  <a href="https://englishanchor.online">
    <img src="./docs/icons/icon-192.png" alt="English Anchor" width="144" />
  </a>
</p>

<h1 align="center">Anki 卡组资料库</h1>

<p align="center">
  在 English Anchor 发布可下载、可持续更新的英语学习 Anki 卡组。
</p>

<p align="center">
  <a href="https://englishanchor.online">English Anchor 官网</a>
  ·
  <a href="https://t.me/+zUqHQVAF42xlODgx">Telegram 交流群</a>
</p>

## 卡组下载

卡组通过 GitHub Releases 发布。下表记录每个卡组当前 Release 中可下载的最新版本；卡组更新后，会同步更新日期、版本和下载链接。

| 卡组 | 介绍 | 更新日期 | 版本 | 下载链接 |
| --- | --- | --- | --- | --- |
| NCE2 實踐與進步（Practice & Progress） | 第二册课文逐句学习，配有中文理解、句型和完整笔记 | 待发布 | `nce2-v1.0.0` | [前往 Releases](../../releases) |
| NCE3 培養技能（Developing Skills） | 第三册课文逐句学习与背诵，配有语法、词汇、表达和知识点笔记 | 待发布 | `nce3-v1.0.0` | [前往 Releases](../../releases) |
| NCE4 流利英語（Fluency in English） | 第四册课文逐句学习与背诵，配有语法、词汇、表达和知识点笔记 | 待发布 | `nce4-v1.0.0` | [前往 Releases](../../releases) |

> 下载后请使用 Anki Desktop、AnkiMobile、AnkiDroid 或其他兼容 Anki `.apkg` 格式的应用导入。

## 这个项目是什么

AnkiShare 是 English Anchor 的卡组制作与发布配套项目。这里维护卡片模板和发布说明；实际的 `.apkg` 文件不提交到 Git，而是作为 GitHub Release 附件发布。

Anki 仍然是本地卡片制作和最终导出的工作台。项目不依赖 AnkiWeb 存储，卡组文件由项目维护者自行发布和更新。

三个牌组均以课文句子为学习单位。第二册属于入门阶段，已补全四个单元的笔记；第三册和第四册提供更密集的语法、词汇、表达和知识点整理。部分句子没有额外笔记并不表示卡片缺失，而是根据句子本身的学习价值保留简洁内容。

第三册的历史 AnkiWeb 页面为[新概念第三册课文【按句子背诵、带笔记】](https://ankiweb.net/shared/info/1533041577)，第四册的历史页面为[新概念第四册课文【按句子背诵、带笔记】](https://ankiweb.net/shared/info/1169581791)。历史页面中的文件和说明可能早于本项目当前版本；GitHub Releases 中的 APKG 才是当前发布文件。

## 项目内容

- `docs/`：卡组发布、维护和使用相关文档。
- `note-templates/`：从 Anki 导出的笔记类型、字段、卡片正反面模板与 CSS，可审阅、可版本控制。
- `note-resources/`：卡片模板依赖的 CSS、JavaScript 等媒体资源标准源；维护后同步到本地 Anki 的 `collection.media`。

## 版本与发布

每个卡组使用独立的 GitHub Release 版本。发布前应完成：

1. 在 Anki 中复核卡片内容和媒体。
2. 导出 `.apkg`，在干净的 Anki 环境中测试导入。
3. 计算文件校验和，并将文件附加到 Release。
4. 回填本 README 的卡组表格，确保链接指向当前 Release 附件。

仓库不提交 `.apkg`、Anki 数据库、媒体目录、复习记录或其他个人集合数据。

## 为什么不再依赖 AnkiWeb

> **AnkiWeb 单个账户的可用空间上限为 300 MB。** 当一个带有大量音频、图片等媒体文件的卡组本身就接近或超过 300 MB 时，即使删除其他卡组，也无法稳定地通过同一个 AnkiWeb 账户继续上传、同步或更新它。

Anki 官方手册将 AnkiWeb 定义为用于跨设备同步卡片和媒体的服务，详见[官方同步说明](https://docs.ankiweb.net/syncing.html)。本项目因此保留 Anki 作为本地制作和导出工具，但不把 AnkiWeb 作为卡组发布渠道；`.apkg` 文件会由本项目维护者通过 GitHub Releases 或 English Anchor 官网发布。300 MB 是当前服务限制，未来如 Anki 官方调整配额，应以官方账户页面和最新文档为准。
