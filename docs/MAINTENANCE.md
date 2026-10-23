# 版本与维护约定

## 一份源码

每个技能在仓库根目录拥有一个与 name 一致的文件夹。OpenClaw 共用安装位置链接到该文件夹；Agent 工作区的旧路径可以保留兼容链接，同名技能从共用目录发现。当前版本对工作区跨目录链接执行边界检查，因此 investment 的 4 个专属技能使用受管理部署副本。所有改动回到仓库，不另建人工维护版本。更新工作区部署副本时运行安装器（--target 指定工作区，默认 copy），版本与内容哈希应与仓库一致。

README.md 给人看：用途、输入、输出、示例、边界、依赖、安装和来源。SKILL.md 给 Agent 看：精简触发描述、执行规则、按需读取的参考文件。详细子流程放 references，脚本放 scripts。不要为没有资源的技能建立空目录。

## 每个技能独立版本

`skill.json` 是版本号唯一权威来源，采用 MAJOR.MINOR.PATCH：

- PATCH：纠错、修路径、补说明，用户输入和输出契约不变，例如 1.0.0 → 1.0.1。
- MINOR：增加兼容的分析模式、可选输入或输出，例如 1.0.1 → 1.1.0。
- MAJOR：改名、删除旧模式、改变必填输入或默认输出行为，例如 1.1.0 → 2.0.0；写迁移说明。

没有旧版本的技能以本次整理后的 1.0.0 建立基线；不表示原作者刚发布 1.0.0。保留已有周报 2.1.0 和科技深研 v3.0 的历史，本次本地修正分别为 2.1.1、3.0.1。第三方 upstream 版本与本地适配版本分开。

不要同时在 README、SKILL frontmatter 和脚本里维护多个代表同一含义的版本号。现存第三方脚本中的 v3.0 仍表示其原实现代际；本地包版本以 skill.json 为准。

发布时可为单技能建立 tag，例如 `frank-trading-setups/v1.0.0`。tag 指向完整仓库 commit，但只声明这个技能的发布。尚未发布的整理稿先通过本地校验，不需要人为补建历史 tag。

## 日常修改流程

1. 修改对应技能源码和必要资源。
2. 更新 skill.json 的版本、依赖/来源（如果改变），并补 CHANGELOG.md。
3. `python3 scripts/validate.py` 检查结构、命名、依赖、个人路径/凭据模式和文件链接。
4. `python3 scripts/catalog.py` 更新 CATALOG.md 与 skills-lock.json。
5. `python3 scripts/validate.py --check-lock` 确认目录及内容哈希没有漂移。
6. 运行改动涉及的脚本检查或代表性场景；结构校验不代替真实数据验证。
7. 提交 Git；需要分享时再推送和发布。

`skills-lock.json` 记录每个技能的版本和文件内容哈希，用于发现未记录变化；不是 Python 依赖锁。运行依赖目前记录在各 skill.json，未经测试不随意把所有技能固定到一个 Python 环境。需要可执行发布时按技能维护并验证其 requirements/lock 文件。

## 本地配置与数据

券商凭据、账户数据、频道 ID、个人绝对路径、运行输出不进技能源码。Tiger 配置在 `~/.openclaw/local-config/trading-review.json`；科技深研运行数据在 `~/.openclaw/skill-data/tech-earnings-deepdive`。配置样例保留在技能目录。

## 来源

原创、个人改编、第三方导入分别记录在 ORIGIN.md / skill.json。不根据安装位置推定原创，也不统一套用 MIT 等许可证。推送时保留各技能的 README、ORIGIN、版本与变更记录；不要把本地配置、凭据或运行数据加入提交。
