# us-weekly-cross-asset-recap

周度美股跨资产总结与下周准备。

分类：市场与宏观。当前版本以 [skill.json](skill.json) 为准；更新记录见 [CHANGELOG.md](CHANGELOG.md)。

## 什么时候用

周度美股跨资产总结与下周准备。本技能的具体执行步骤在 [SKILL.md](SKILL.md)，介绍文档不重复整套提示词。

## 需要提供什么

明确周度范围、跨资产行情、宏观事件、未来日历。

## 会得到什么

指数/板块、利率/美元/商品/加密、波动/信用、市场环境和下周重点。

## 使用示例

- “使用 us-weekly-cross-asset-recap：总结本周美股与跨资产表现。”
- “使用 us-weekly-cross-asset-recap：做一份周末复盘，列出下周最重要的宏观催化剂。”

## 边界与相邻技能

只在周度请求时触发；保留已有 2.1.0 历史，本次路由和引用修正递增至 2.1.1。

## 环境与依赖

- Agent 可用的网页/资料读取能力；使用最新信息时需联网核验

同仓库依赖：无强制的同仓库技能依赖；文中其他技能名是可选协作入口。

## 安装和复用

在仓库根目录运行 `python3 scripts/install.py us-weekly-cross-asset-recap` 预览，再加 `--apply` 安装。已有同名目录时先比较；确认替换可加 `--replace`，安装器会备份。依赖技能会一并解析。共用目录默认使用链接；`--target` 指向 Agent 工作区时默认使用部署副本，更新后用同一命令同步。

手动安装时复制整个 `us-weekly-cross-asset-recap/` 文件夹，保留 `references/`、`scripts/` 等实际存在的资源；跨机器使用时重新配置本地工具。安装只是让 Agent 找到说明，不会自动运行联网分析、读取账户或发送消息。

## 文件说明

- `CHANGELOG.md`
- `ORIGIN.md`
- `SKILL.md`
- `skill.json`

## 来源和维护

详见 [ORIGIN.md](ORIGIN.md)。更新时修改本技能，递增 `skill.json` 的版本，补充变更记录，再运行仓库校验；不要在不同 Agent 工作区各维护一个副本。

## Finance 合并记录

保留 Investment 已修正的周度触发范围、有效关联技能及独立版本元数据；Finance 的周报分析正文已包含，正文差异仅为 Markdown 换行格式。原始版权与许可见 [LICENSE](LICENSE)，来源提交及取舍见 [ORIGIN.md](ORIGIN.md)。
