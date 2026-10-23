# Finance 与 Investment 仓库合并

合并日期：2026-10-23。

统一维护仓库：[JerryGou96/Investment-skill](https://github.com/JerryGou96/Investment-skill)。

## 本次合入内容

来源：[JerryGou96/Finance-Skill](https://github.com/JerryGou96/Finance-Skill)。

来源分支：`main`；来源提交：`ba2df58f27cd855dd1bb4461b79233d708e8e09f`。

使用不压缩历史的 Git subtree，将来源提交的完整文件树放入 `imports/Finance-Skill/`。该目录与来源提交的 Git tree 完全一致，包含原 README、LICENSE、CHANGELOG、贡献指南、安装脚本、工作流和全部技能资源。原有 3 个提交的历史通过合并提交保留，没有改写原提交。

来源仓库在检查时只有 main 分支，没有其他分支或标签。GitHub issues、PR、release 附件及仓库设置不属于 Git 文件树；它们仍留在原仓库。

## 技能对照

| 技能 | 现有维护版 | 导入原版 |
|---|---|---|
| COMEX 交割分析 | 暂不提取到根目录 | [原版](../imports/Finance-Skill/skills/comex-delivery-analysis/SKILL.md) |
| 每日账户复盘 | [维护版](../daily-portfolio-review/README.md) | [原版](../imports/Finance-Skill/skills/daily-portfolio-review/SKILL.md) |
| 非农分析 | [维护版](../nfp-labor-market-analysis/README.md) | [原版](../imports/Finance-Skill/skills/nfp-labor-market-analysis/SKILL.md) |
| 跨资产周报 | [维护版](../us-weekly-cross-asset-recap/README.md) | [原版](../imports/Finance-Skill/skills/us-weekly-cross-asset-recap/SKILL.md) |

根目录仍有 20 个带完整介绍及版本记录的维护版包；原始导入另保留 4 个条目，其中 3 个同名、1 个新增名称。合计 21 个不同技能名称。现在只合并仓库，不对同名版本作自动取舍。

## 后续整理方式

1. 从本仓库选择一对同名技能，比较规则与参考文件。
2. 确认采用哪个版本或合并哪些内容，更新根目录对应技能的版本、README、CHANGELOG 和来源说明。
3. 新增 COMEX 维护版时再建立独立包、详细介绍和版本基线。
4. 原始导入可继续作为历史参考；不要直接运行其中的旧安装脚本覆盖当前维护版。

原 Finance 的 [MIT LICENSE](../imports/Finance-Skill/LICENSE) 原样保留，适用于原仓库所声明的范围，不给整个 Investment 仓库的第三方技能统一套用许可。嵌套的 `.github/workflows` 仅作为原始文件保留，不会成为统一仓库的顶层工作流。

## 原仓库

统一仓库推送与校验成功后，Finance 原仓库已添加迁移入口并归档为只读历史。原仓库保留，不删除；之后的维护集中在本仓库。迁移提示提交为 `a6e524c97aababa765638f5f19add320578edc91`；原始内容快照仍对应上面的 ba2df58 提交。

## 验证

可比较 `git rev-parse HEAD:imports/Finance-Skill` 与来源提交的 tree SHA，验证原始文件树完全保留。`git merge-base --is-ancestor ba2df58f27cd855dd1bb4461b79233d708e8e09f HEAD` 应成功，证明来源历史仍可达。

原有维护版继续通过 `python3 scripts/validate.py --check-lock` 检查。原 Finance 快照不要求补写当前仓库的包元数据，避免在尚未整理时改变来源文件。
