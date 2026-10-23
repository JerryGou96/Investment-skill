# Finance 技能整合到根目录

整理日期：2026-10-23。统一维护仓库：[JerryGou96/Investment-skill](https://github.com/JerryGou96/Investment-skill)。

Finance 的技能与其他技能平级放置，每个名称只保留一个维护目录。当前文件树已移除整仓导入目录，也不包含 Finance 的旧安装脚本、仓库级说明或嵌套工作流。

## 四个技能的结果

| Finance 技能 | 根目录位置 | 内容取舍 | 当前版本 |
|---|---|---|---|
| COMEX 交割分析 | [comex-delivery-analysis](../comex-delivery-analysis/README.md) | 新增独立包，原执行规则一致，补齐介绍与元数据 | 1.0.0 |
| 每日账户复盘 | [daily-portfolio-review](../daily-portfolio-review/README.md) | 保留精确触发、手续费修正及共用复盘口径；原模板和参考文件均已包含 | 1.0.1 |
| 非农分析 | [nfp-labor-market-analysis](../nfp-labor-market-analysis/README.md) | SKILL.md 和参考框架完全一致，统一为一个包 | 1.0.1 |
| 跨资产周报 | [us-weekly-cross-asset-recap](../us-weekly-cross-asset-recap/README.md) | 保留周度触发及已修正关联引用；原分析正文已包含 | 2.1.2 |

原有 20 个维护包加上 COMEX，现在共 21 个独立技能。新增包与其他包一样包含 README、SKILL、skill.json、CHANGELOG 和 ORIGIN；Finance 对应四个包另保留原始 LICENSE。

## 来源与许可

来源仓库为 [JerryGou96/Finance-Skill](https://github.com/JerryGou96/Finance-Skill)，内容基于提交 `ba2df58f27cd855dd1bb4461b79233d708e8e09f`。

四个包的 ORIGIN.md 分别记录来源路径、提交和合并取舍；原仓库的 MIT LICENSE 分别保存在包内。这个来源许可不为统一仓库中其他第三方技能统一声明许可。

旧 Finance 仓库继续作为只读历史归档。此前合入的原提交仍在当前仓库的 Git 历史中，删除重复目录没有改写或删除历史。

## 使用与检查

统一使用根目录安装器，例如 `python3 scripts/install.py comex-delivery-analysis` 预览安装，加 `--apply` 才实际安装。此次只整理仓库，没有自动给 Agent 增加 COMEX 技能。

`python3 scripts/validate.py --check-lock` 检查 21 个包的结构、依赖、链接及文件哈希。COMEX 的执行文件与来源提交逐字节比较；三个同名包的现有执行文件保持不变。原 Finance 业务规则的准确性不属于此次目录迁移验证。
