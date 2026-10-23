# Changelog

All notable changes to this repo will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

This is a monorepo containing multiple Claude Skills. Changes are grouped by skill.

---

## [Unreleased]

### Added
- **`us-weekly-cross-asset-recap`** skill v2.1.0 加入 monorepo: 生成经过实时核验、面向交易决策的中文美股跨资产周报，覆盖主要指数、11 个行业板块、美债利率、美元、商品、加密货币、波动率、信用市场、AI/软件轮动、下周催化剂及条件式交易剧本。
- **`nfp-labor-market-analysis`** skill 加入 monorepo: 用 JJ-Macro 的劳动力市场框架分析美国 Employment Situation / Nonfarm Payrolls,覆盖企业调查 vs 家庭调查拆分、失业率分解、劳动力供需信号分类及 Fed/市场影响。

## [0.2.0] - 2026-05-02

### Added
- **`comex-delivery-analysis`** skill 加入 monorepo
- **`daily-portfolio-review`** skill v0.2.0:
  - 第 1 节"组合风险画像":加权 Beta(SPY+QQQ 双对标,股票口径+账户口径)、仓位集中度(Top1/3/5、HHI)、板块暴露分布
  - 手续费追踪:Header/归因表/交易行为节都加入佣金列
  - "Beta 一致性核对":预期波动 vs 实际波动 = 当日 Alpha
  - 关键启发式:手续费一致性自动核对、Beta 数据缺失处理
- Monorepo 基础设施:
  - `install.sh` 支持单个或全部 skill 安装
  - `.github/workflows/lint.yml` skill 结构自动校验
  - `.github/workflows/release.yml` 打 tag 时自动为每个 skill 打 zip + 总包
  - `CONTRIBUTING.md` 通用贡献指南

### Changed
- 报告节数从 7 节(0–6)扩展至 8 节(0–7)
- "组合风险画像"放在归因之前

## [0.1.0] - 2026-05-02

### Added
- 初始版本,包含 `daily-portfolio-review` skill v0.1.0(7 节报告结构)
