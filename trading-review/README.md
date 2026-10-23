# trading-review

Tiger 只读数据接入与简洁交易复盘。

分类：组合复盘。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

Tiger 只读数据接入与简洁交易复盘。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

本地 Tiger read_only.py、其虚拟环境、外置 adapter 配置、复盘日期。

## 会得到什么

账户 P&L、持仓/行业暴露、净买卖、已实现盈亏与手续费的简洁报告。

## 使用示例

- “使用 trading-review：读取 Tiger 账户并生成今天的交易复盘。”
- “使用 trading-review：按已配置的定时任务生成简洁账户日报。”

## 边界与相邻技能

依赖 daily-portfolio-review 的共用口径；生成与投递分离。账户目录和频道保留在本地配置，不打包凭据。

## 环境与依赖

- Python 3（标准库启动器）
- 已有 Tiger adapter 和其 .venv/tigeropen 环境

同仓库依赖：`daily-portfolio-review`

## 本地配置

将 `config.example.json` 复制到 `~/.openclaw/local-config/trading-review.json`，设置 `tiger_api_dir`。可用 `TRADING_REVIEW_CONFIG` 指定其他位置。凭据继续由已有 Tiger adapter 管理；本仓库不包含券商登录或密钥。发送目标存于本地配置，已有定时任务优先使用任务自己的投递配置。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py trading-review` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `trading-review/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `config.example.json`
- `scripts/read_account.py`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
