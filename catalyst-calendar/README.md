# catalyst-calendar

跟踪公司、行业、宏观及加密资产的未来催化剂。

分类：市场与宏观。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

跟踪公司、行业、宏观及加密资产的未来催化剂。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

标的或观察清单；时间跨度默认为未来 4–8 周。

## 会得到什么

带来源、日期确定性、影响判断和研究准备事项的事件日历。

## 使用示例

- “使用 catalyst-calendar：整理 NVDA、MU、CRDO 未来 4–8 周催化剂。”
- “使用 catalyst-calendar：把下周宏观事件与我的观察清单放在一起。”

## 边界与相邻技能

事件存在不等于买卖信号；区分确认、预计和未核验日期。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py catalyst-calendar` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `catalyst-calendar/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。
