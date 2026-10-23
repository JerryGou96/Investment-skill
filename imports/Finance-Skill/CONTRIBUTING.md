# Contributing to Finance-Skill

感谢你愿意贡献!以下是参与开发的指南。

## Repo 结构

```
Finance-Skill/
├── skills/                       # ← 所有 skills 放这里,每个 skill 一个文件夹
│   ├── daily-portfolio-review/
│   │   ├── SKILL.md             # 主指令(必需)
│   │   ├── references/          # 参考资料(可选)
│   │   └── assets/              # 模板与示例(可选)
│   └── comex-delivery-analysis/
│       └── SKILL.md
├── .github/workflows/            # 自动化流程
└── ...
```

## 添加新 Skill 的步骤

1. **创建文件夹**:`skills/<skill-name>/`(文件夹名必须与 SKILL.md 的 `name` 字段完全一致)

2. **编写 SKILL.md**,顶部必须有 YAML frontmatter:
   ```markdown
   ---
   name: your-skill-name
   description: 用一句话讲清楚 (1) 这个 skill 能做什么 (2) 什么场景下应该触发。
   ---

   # Skill 内容
   ```

3. **可选目录**:
   - `references/` —— 详细参考资料,Claude 按需加载,主体精简
   - `assets/` —— 模板、示例输出
   - `scripts/` —— 可执行脚本(如果需要确定性逻辑)

4. **更新顶层 README** 的 "Skills 一览" 表格

5. **更新 CHANGELOG.md**

6. **本地校验** 通过后再 push

## 编写 SKILL.md 的最佳实践

### Description 要"主动一点"

description 是 Claude 决定**触发**的唯一依据。要列出关键词、覆盖典型场景。**不写得主动 → Claude 倾向于不触发**。

✅ 好的:
> 分析 CME/COMEX 金属期货交割报告(silver, gold, copper, platinum, palladium, aluminum)。... 当用户分析月度交割模式、市场结构、供需信号、机构持仓时使用。

❌ 太被动:
> 用于分析 COMEX 数据。

### 主体保持精简(< 500 行)

详细的、不常用的内容放到 `references/` 里,在 SKILL.md 中引用,如 `详见 references/sector-mapping.md`。

### 用祈使句

✅ 好的:用 `web_search` 查询,必须包含日期。
❌ 啰嗦:你应该使用 web_search 工具,并且应该在查询里包含日期。

### 解释为什么

比起堆砌 MUST,解释为什么这样做更有效。

## 测试

skill 是 prompt,测试方法是端到端跑用例:

1. 本地安装:`./install.sh <skill-name>`
2. 准备 2-3 个测试用例,覆盖典型场景和边界情况
3. 在 Claude Code 中触发,检查输出是否符合 SKILL.md 标准
4. 关注**触发准确性**:该触发的有没有触发?不该触发的有没有误触发?

## 自动化校验

push 或 PR 时,GitHub Actions 会自动检查:

- ✅ 每个 skill 文件夹里有 `SKILL.md`
- ✅ `SKILL.md` 顶部有合法的 YAML frontmatter
- ✅ frontmatter 含 `name` 和 `description`
- ✅ frontmatter 的 `name` 与文件夹名一致
- ✅ 没有遗留的 `<your-username>` / `TODO` 占位符

如果校验失败,在 PR 页面会看到红色 ✗,点进去看具体哪一项没过。

## 发布 Release

打 tag 时(如 `v0.3.0`),GitHub Actions 会:

1. 为每个 skill 单独打 zip(`daily-portfolio-review.zip` 等)
2. 打一个 all-skills 总包(`finance-skill-all.zip`)
3. 自动创建 GitHub Release,把 zip 作为附件

发布流程:
```bash
git tag -a v0.3.0 -m "v0.3.0: 加入新 skill X"
git push origin v0.3.0
```

## 报 Bug / 提需求

请提供:
- 涉及的 skill 名(或新 skill 的需求描述)
- Claude 客户端环境(Claude Code / Claude.ai)
- 最小可复现输入
- 预期 vs 实际输出
- **不要** 在 issue 中粘贴真实账户数据,用脱敏数据
