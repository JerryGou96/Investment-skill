# Investment-skill

Jerry 的投资研究与交易框架技能库。每个技能独立一个文件夹，包含人可读的用途说明、Agent 执行规则、版本记录及来源说明。

`Finance-Skill` 已合并到本仓库。后续统一在这里维护；Finance 的完整原始目录、MIT 许可及 Git 历史保留在 [imports/Finance-Skill](imports/Finance-Skill/README.md)，供后续逐步整理。同名技能的两个版本暂时分别保留。

本次整理提供 20 个投资相关技能目录，覆盖公司研究、财报研究、市场宏观、组合复盘、交易框架及数据分析。包括个人框架、定制流程和注明来源的第三方改编；详细来源见各目录的 `ORIGIN.md`。

## 从哪里开始

- [完整技能目录](CATALOG.md)：按用途、分类和版本选择技能。
- [版本与维护约定](docs/MAINTENANCE.md)：如何修改、验证和复用。
- [本次迁移说明](docs/MIGRATION.md)：技能合并、改名及兼容路径。
- [Finance 合并说明](docs/FINANCE-MERGE.md)：4 个原始技能、重复版本对照与历史保留方式。

## 从 Finance 合入的原始技能

| 技能 | 位置与处理方式 |
|---|---|
| COMEX 交割分析 | [comex-delivery-analysis](imports/Finance-Skill/skills/comex-delivery-analysis/SKILL.md)，保留原始版本 |
| 每日账户复盘 | [Finance 原版](imports/Finance-Skill/skills/daily-portfolio-review/SKILL.md)，与根目录维护版并存 |
| 非农分析 | [Finance 原版](imports/Finance-Skill/skills/nfp-labor-market-analysis/SKILL.md)，与根目录维护版并存 |
| 跨资产周报 | [Finance 原版](imports/Finance-Skill/skills/us-weekly-cross-asset-recap/SKILL.md)，与根目录维护版并存 |

Finance 导入目录暂不加入默认安装列表，也不覆盖已安装技能。需要复用原版时，复制对应技能的完整文件夹；以后再逐个比较、选择或合并。

## 常用入口

| 要做什么 | 技能 |
|---|---|
| AI 基建公司研究 | [ai-infra-five-factor-investing](ai-infra-five-factor-investing/README.md) |
| 行业与 AI 产业链轮动 | [analyze-equity-rotation](analyze-equity-rotation/README.md) |
| 把新闻转成研究假设 | [serenity-alpha](serenity-alpha/README.md) |
| 财报事实速览 | [earnings-recap](earnings-recap/README.md) |
| 财报后的投资判断 | [post-earnings-investment-review](post-earnings-investment-review/README.md) |
| 电话会与问答摘要 | [summarizing-earnings-calls](summarizing-earnings-calls/README.md) |
| 账户完整复盘 / Tiger 简报 | [daily-portfolio-review](daily-portfolio-review/README.md) / [trading-review](trading-review/README.md) |
| 箱体突破或缺口回踩 | [frank-trading-setups](frank-trading-setups/README.md) |
| 美股日报 / 跨资产周报 | [us-market-close-recap](us-market-close-recap/README.md) / [us-weekly-cross-asset-recap](us-weekly-cross-asset-recap/README.md) |

## 一个技能的结构

```text
skill-name/
├── README.md       用途、输入输出、示例、依赖和复用方式
├── SKILL.md        Agent 执行规则
├── skill.json      独立版本、分类、依赖和来源记录
├── CHANGELOG.md    本技能变更历史
├── ORIGIN.md       原始来源及本地改动
├── references/     按需存在的详细框架
└── scripts/        按需存在的辅助脚本
```

## 本地安装

在仓库根目录运行：

```bash
python3 scripts/validate.py --check-lock
python3 scripts/install.py frank-trading-setups
python3 scripts/install.py frank-trading-setups --apply
```

默认先预览；`--apply` 在共用目录 `~/.openclaw/skills` 创建源码链接。已有同名目录时先比较，再使用 `--replace`，安装器会备份旧目录。可以用 `--target` 指定 Agent 工作区；`auto` 模式会使用受管理的文件副本，因为当前 OpenClaw 工作区默认不加载跨目录符号链接。依赖按需安装，例如 trading-review 会包含 daily-portfolio-review。

本仓库是唯一维护源；共用目录使用链接，不要随意移动 checkout。工作区安装副本只用于部署，更新仓库后再次运行安装命令同步，不独立编辑。跨机器复用可复制完整技能文件夹，但本地账户配置和运行依赖需重新配置。

## 当前验证范围

结构、内容哈希、依赖和本地链接校验用于防止整理漂移，不代表所有技能已经完成联网或金融数据端到端验证。SaaS 旧解析原型和第三方科技深研脚本的限制在各自 README 中说明。

所有技能保留详细介绍、原作者与参考来源，并区分本地定制和第三方改编。来源说明不等于统一的许可证授权；各技能的来源与许可记录见 `ORIGIN.md` 和 `skill.json`。
