#!/usr/bin/env bash
# install.sh — 把 Finance-Skill 中的 skills 安装到 Claude Code skills 目录
#
# 用法:
#   ./install.sh                          # 列出所有 skills,交互选择
#   ./install.sh all                      # 安装全部 skills
#   ./install.sh <skill-name>             # 安装指定 skill
#   ./install.sh <skill-name> <target>    # 安装到自定义路径

set -e

SKILLS_DIR="skills"
DEFAULT_TARGET="$HOME/.claude/skills"

# ─── 检查环境 ──────────────────────────────────
if [ ! -d "$SKILLS_DIR" ]; then
  echo "❌ 找不到 ./$SKILLS_DIR 目录,请确认你在 repo 根目录下运行此脚本"
  exit 1
fi

# 收集所有可用的 skills
mapfile -t AVAILABLE_SKILLS < <(find "$SKILLS_DIR" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort)

if [ ${#AVAILABLE_SKILLS[@]} -eq 0 ]; then
  echo "❌ ./$SKILLS_DIR 目录下没有发现任何 skill"
  exit 1
fi

# ─── 解析参数 ──────────────────────────────────
SELECTED=""
TARGET="$DEFAULT_TARGET"

if [ -z "$1" ]; then
  # 交互模式
  echo "可用 skills:"
  for i in "${!AVAILABLE_SKILLS[@]}"; do
    echo "  $((i+1)). ${AVAILABLE_SKILLS[$i]}"
  done
  echo "  $((${#AVAILABLE_SKILLS[@]}+1)). 全部安装"
  echo ""
  read -p "选择要安装的 skill 编号: " choice

  if [ "$choice" -eq $((${#AVAILABLE_SKILLS[@]}+1)) ] 2>/dev/null; then
    SELECTED="all"
  elif [ "$choice" -ge 1 ] 2>/dev/null && [ "$choice" -le ${#AVAILABLE_SKILLS[@]} ]; then
    SELECTED="${AVAILABLE_SKILLS[$((choice-1))]}"
  else
    echo "❌ 无效的选择"
    exit 1
  fi
elif [ "$1" = "all" ]; then
  SELECTED="all"
else
  # 检查指定的 skill 是否存在
  found=0
  for s in "${AVAILABLE_SKILLS[@]}"; do
    if [ "$s" = "$1" ]; then
      found=1
      break
    fi
  done
  if [ $found -eq 0 ]; then
    echo "❌ 找不到 skill: $1"
    echo "可用 skills:"
    printf '  - %s\n' "${AVAILABLE_SKILLS[@]}"
    exit 1
  fi
  SELECTED="$1"
fi

# 自定义目标路径
if [ -n "$2" ]; then
  TARGET="$2"
fi

# ─── 执行安装 ──────────────────────────────────
mkdir -p "$TARGET"

install_one() {
  local skill="$1"
  local src="$SKILLS_DIR/$skill"
  local dst="$TARGET/$skill"

  if [ ! -f "$src/SKILL.md" ]; then
    echo "  ⚠️  $skill: 缺少 SKILL.md,跳过"
    return
  fi

  if [ -d "$dst" ]; then
    echo "  ⚠️  $dst 已存在,覆盖中..."
    rm -rf "$dst"
  fi

  cp -r "$src" "$dst"
  echo "  ✅ $skill → $dst"
}

echo ""
echo "📦 安装到: $TARGET"
echo ""

if [ "$SELECTED" = "all" ]; then
  for s in "${AVAILABLE_SKILLS[@]}"; do
    install_one "$s"
  done
else
  install_one "$SELECTED"
fi

# ─── 收尾 ──────────────────────────────────
echo ""
echo "🎉 安装完成!"
echo ""
echo "下一步:"
echo "  1. 重启 Claude Code"
echo "  2. 在对话中触发 skill 测试(如:'复盘今天的账户' 或 '分析这份 COMEX 报告')"
echo ""
echo "如果 skill 没被自动加载,检查:"
echo "  - Claude Code 版本是否支持 skills"
echo "  - $TARGET 路径是否在 Claude Code 的 skills 搜索路径中"
