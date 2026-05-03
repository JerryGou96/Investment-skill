# Changelog

All notable changes to this repo will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

This is a monorepo containing multiple Claude Skills. Changes are grouped by skill.

---

## [Unreleased]

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
