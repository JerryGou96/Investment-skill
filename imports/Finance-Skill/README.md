# Finance-Skill

> 一组用于金融分析的 Claude Skills。每个 skill 是一个独立模块,可单独安装、组合使用。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-4-blue)](./skills)

---

## 📚 Skills 一览

| Skill | 用途 | 状态 |
|---|---|---|
| [`daily-portfolio-review`](./skills/daily-portfolio-review) | 每日证券账户复盘:盈亏归因、组合 Beta、Alpha 分解、当日新闻、催化剂日历、交易行为复盘 | ✅ v0.2.0 |
| [`comex-delivery-analysis`](./skills/comex-delivery-analysis) | CME/COMEX 金属期货交割报告分析:Issuer / Client Short / House Short 三栏数据提取与市场结构判读 | ✅ Stable |
| [`nfp-labor-market-analysis`](./skills/nfp-labor-market-analysis) | 美国非农 / Employment Situation 分析:企业调查与家庭调查拆分、失业率分解、劳动力供给/需求信号、Fed 与市场影响 | ✅ Stable |
| [`us-weekly-cross-asset-recap`](./skills/us-weekly-cross-asset-recap) | 中文美股跨资产周报:指数、11 个行业板块、利率、美元、商品、加密、AI/软件轮动及下周催化剂 | ✅ v2.1.0 |

> 后续会持续添加更多 skills,关注 [CHANGELOG](./CHANGELOG.md)。

---

## 🚀 快速安装

### 安装全部 skills(Claude Code)

```bash
git clone https://github.com/JerryGou96/Finance-Skill.git
cd Finance-Skill
./install.sh
```

### 只安装某一个

```bash
./install.sh daily-portfolio-review
# 或
./install.sh comex-delivery-analysis
# 或
./install.sh nfp-labor-market-analysis
# 或
./install.sh us-weekly-cross-asset-recap
```

### 自定义安装路径

```bash
./install.sh daily-portfolio-review /custom/path/to/skills
```

### Claude.ai(网页 / App)

每个 skill 文件夹可以单独打成 zip 上传。从 [GitHub Releases](https://github.com/JerryGou96/Finance-Skill/releases) 下载预打包好的 zip 也可以(Release 流程会自动为每个 skill 打单独的 zip)。

> 具体上传入口可能因产品更新有变,以 [Anthropic 官方文档](https://docs.claude.com) 为准。

---

## 🗂️ Repo 结构

```
Finance-Skill/
├── README.md                              # 本文档
├── LICENSE                                # MIT
├── CHANGELOG.md                           # 全 repo 版本变更
├── CONTRIBUTING.md                        # 贡献指南
├── install.sh                             # 安装脚本(支持单个/全部)
├── .gitignore
├── .github/
│   └── workflows/
│       ├── lint.yml                       # PR 时自动校验 skill 结构
│       └── release.yml                    # 打 tag 时自动打包 release
└── skills/
    ├── daily-portfolio-review/
    │   ├── SKILL.md
    │   ├── references/
    │   │   ├── sector-mapping.md
    │   │   └── catalyst-types.md
    │   └── assets/
    │       └── report-template.md
    ├── comex-delivery-analysis/
    │   └── SKILL.md
    ├── nfp-labor-market-analysis/
    │   ├── SKILL.md
    │   └── references/
    │       └── nfp-framework.md
    └── us-weekly-cross-asset-recap/
        └── SKILL.md
```

---

## 📦 单个 Skill 的详情

### `daily-portfolio-review`

每日证券账户复盘 skill。**8 节结构化日报**:

| 节 | 内容 |
|---|---|
| 0 | Header(总市值 / 净盈亏 / 佣金 / vs SPY、QQQ) |
| 1 | 组合风险画像(加权 Beta、HHI、板块暴露) |
| 2 | 当日盈亏归因(扣除佣金) |
| 3 | 持仓相对表现(Alpha 视角) |
| 4 | 当日新闻 + 走势-新闻一致性 |
| 5 | 催化剂日历(未来 4-8 周) |
| 6 | 交易行为复盘 |
| 7 | 明日观察清单 |

详见 [skills/daily-portfolio-review/SKILL.md](./skills/daily-portfolio-review/SKILL.md)。

### `comex-delivery-analysis`

CME/COMEX 金属期货交割报告分析 skill,处理 Silver / Gold / Copper / Platinum / Palladium / Aluminum 的月度交割数据。覆盖:

- 三栏数据提取(Issuer / Client Short / House Short)
- 集中度分析(HHI、Top 3/5 比例)
- 客户 vs 交易所交割平衡(Client-to-House Ratio)
- 供需信号判读
- 月环比对比

详见 [skills/comex-delivery-analysis/SKILL.md](./skills/comex-delivery-analysis/SKILL.md)。

### `nfp-labor-market-analysis`

美国 Employment Situation / Nonfarm Payrolls 分析 skill,用 JJ-Macro 的劳动力市场框架拆解非农报告。覆盖:

- 官方 BLS 数据优先校验
- Establishment Survey vs Household Survey 拆分
- 失业率变化分解:就业人口、失业人口、劳动力人口、退出劳动力人口
- 劳动力信号分类:健康供给扩张、需求降温、隐藏疲弱、再加速/过热、衰退式恶化
- Fed、美债/美元、美股、加密/黄金、行业轮动影响

详见 [skills/nfp-labor-market-analysis/SKILL.md](./skills/nfp-labor-market-analysis/SKILL.md)。

### `us-weekly-cross-asset-recap`

面向主动交易者的中文美股跨资产周报 skill。覆盖:

- 美股主要指数、11 个行业板块及市场宽度
- 美债利率、美元、黄金、原油、BTC、VIX 与信用市场
- AI 半导体、硬件、软件及 SaaS 轮动
- 宏观市场状态判断与证据置信度
- 下周宏观、Fed、全球央行及重点财报日历
- 带触发条件、周期和失效条件的交易剧本

详见 [skills/us-weekly-cross-asset-recap/SKILL.md](./skills/us-weekly-cross-asset-recap/SKILL.md)。

---

## 🛠️ 开发与贡献

欢迎 issue 和 PR。新 skill 的添加流程:

1. 在 `skills/` 下创建新文件夹(名字与 SKILL.md 的 `name` 字段一致)
2. 至少包含一个 `SKILL.md`,顶部 YAML frontmatter 包含 `name` 和 `description`
3. 复杂 skill 可以加 `references/`、`assets/`、`scripts/` 子目录
4. 更新顶层 README 的 "Skills 一览" 表格
5. 更新 `CHANGELOG.md`
6. push 时 GitHub Actions 会自动校验结构

详见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

---

## 🔐 隐私与安全

- 所有 skills **不存储**任何账户数据,所有数据在对话中处理
- skills **不提供买卖建议**,只做事实陈述和中性归因
- 不替代税务、合规、法律或投资顾问意见
- `.gitignore` 已配置过滤 `*.csv` / `*.xlsx` / `account-snapshots/` 等,防止意外提交真实数据

---

## 📜 License

MIT — 详见 [LICENSE](./LICENSE)。

---

## 🙏 致谢

基于 [Anthropic Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) 框架。

---

*Disclaimer: 本 repo 中的 skills 仅为辅助分析工具,所有投资决策由用户自行承担。*
