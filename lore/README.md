# 锻造之王宇宙 · 阅读与设定导航

## 故事与世界

- [故事目录](stories.md)：各本故事的简介与正文入口。
- [世界观总纲](world-bible.md)：起源、魔法、资源、器械与生物。
- [区域与城镇志](regions-and-cities.md)：地域和城镇详情。
- [组织、政体与外交](organizations.md)：势力名录、统治归属、同盟与敌对关系。
- [人物档案](characters.md)与[人物关系](relationships.md)。
- [编年史](timeline.md)：按时代查阅世界事件。
- [典籍与文献](library.md)：故事世界内的书籍、论文、法典档案和节选。
- [坦普拉专册](world-bible-tanpula.md)：暂保留的详细设定；独有细节尚未逐项归并，不应直接删除。

## 小说正文

每本小说独立存放在 `drafts/`，章节不拆成多本书：

- [王锻](drafts/wangduan.md)
- [苍赫](drafts/canghe-final.md)
- [双生](drafts/shuangsheng.md)
- [探险家笔记](drafts/tanxianjiabiji.md)：同一个文件包含两卷。
- [大魔法师](drafts/damofashi.md)
- [王冢](drafts/wangzhong.md)：创作中的正文。

## 文件维护与网站对应

创作规范、大纲、伏笔和游戏策划不属于读者版内容，不随公开故事仓库发布；世界设定可能涉及剧透。

- 网站通过 `src/data/story-catalog.js` 直接读取《苍赫》《大魔法师》《探险家笔记》的 Markdown，三份正文路径保持不变。
- 组织、人物、区域与城镇页面使用 `src/data/game-data.js`；合并设定文档不会自动更新这些数据。
- 人物关系证据由网站的 `src/data/character-relationships.js` 维护，其引用路径必须与本地文件一致。《王冢》未发表的终局关系引用本目录内的关系设定表，仍标为设定依据，不视作已完成正文。
- `scripts/sync-lore.js` 目前只是文件检查脚本，并非完整的数据同步器。不能把运行它视为完成网站内容同步。
- 修改设定时先核对正文，更新对应网站字段和关系证据，再运行测试及本地构建。不要把同一项完整设定重复复制到多个总表。
