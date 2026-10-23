# 2026-10-23 整理迁移

- 原 volume-range-breakout-setup 已并入 frank-trading-setups 的 references/range-breakout.md；跳空回踩仍为另一模式。
- 原 investment 的 earnings-recap 改名为 post-earnings-investment-review；earnings-recap 现在统一为事实速览。旧名称请求若需要投资判断，请使用新名称。
- trading-review 保留 Tiger 只读接入及简洁报告，依赖 daily-portfolio-review 的共用复盘口径，配置外置。
- 同名、同内容工作区副本归档后链接至共用版本，旧路径继续可达。
- tech-earnings-deepdive 的运行产物移到技能数据目录，不进入 Git；脚本以实际技能目录定位代码。
- 加载实测发现工作区跨目录链接不被发现：ai-infra-five-factor-investing、saas-valuation-analyzer、serenity-alpha、post-earnings-investment-review 使用受管理部署副本，继续保持 investment 专属范围；其余共享技能从共用目录加载。
- analyze-equity-rotation 保留最新远端内容并补说明；此次不额外自动安装到新的 Agent。
- find-skills、substack-reader、youtube-content 等通用技能参与本地副本去重，但不收入本投资仓库。广告、SEO、法律、内置技能和插件缓存不在本轮仓库收录范围。

从旧名字迁移时，同时检查定时任务和人工保存的指令。既有对话可能缓存旧技能说明，下一轮或新会话再检查发现结果。
