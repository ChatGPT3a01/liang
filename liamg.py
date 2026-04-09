#!/usr/bin/env python3
"""
liamg - 雙 AI CLI 切換器
在同一個 shell 中快速切換 Claude Code 與 Codex CLI

指令：
  /cl [prompt]   啟動 Claude Code（可選帶入提示詞）
  /co [prompt]   啟動 Codex CLI（可選帶入提示詞）
  /cd <path>     切換工作目錄
  /pwd           顯示目前工作目錄
  /status        顯示兩個 CLI 的版本資訊
  /help          顯示指令列表
  /exit          離開 liamg
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# ── 顏色 ──────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    # 品牌色
    CLAUDE  = "\033[38;5;208m"   # 橘色 (Anthropic)
    CODEX   = "\033[38;5;48m"    # 綠色 (OpenAI)
    LIAMG   = "\033[38;5;141m"   # 紫色
    YELLOW  = "\033[33m"
    RED     = "\033[31m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"


BANNER = f"""
{C.LIAMG}{C.BOLD}
  ██╗     ██╗ █████╗ ███╗   ███╗ ██████╗
  ██║     ██║██╔══██╗████╗ ████║██╔════╝
  ██║     ██║███████║██╔████╔██║██║  ███╗
  ██║     ██║██╔══██║██║╚██╔╝██║██║   ██║
  ███████╗██║██║  ██║██║ ╚═╝ ██║╚██████╔╝
  ╚══════╝╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝
{C.RESET}
{C.DIM}  雙 AI CLI 切換器 — Claude Code × Codex CLI{C.RESET}
{C.DIM}  ─────────────────────────────────────────{C.RESET}
  {C.CLAUDE}▸ /cl{C.RESET}  Claude Code    {C.CODEX}▸ /co{C.RESET}  Codex CLI
  {C.CYAN}▸ /help{C.RESET} 指令列表      {C.YELLOW}▸ /exit{C.RESET} 離開
"""

HELP_TEXT = f"""
{C.BOLD}可用指令：{C.RESET}
  {C.CLAUDE}/cl [prompt]{C.RESET}     啟動 Claude Code（互動模式，或帶提示詞）
  {C.CODEX}/co [prompt]{C.RESET}     啟動 Codex CLI（互動模式，或帶提示詞）
  {C.CYAN}/cd <path>{C.RESET}       切換工作目錄
  {C.CYAN}/pwd{C.RESET}             顯示目前工作目錄
  {C.CYAN}/status{C.RESET}          顯示 CLI 版本資訊
  {C.YELLOW}/help{C.RESET}            顯示此說明
  {C.YELLOW}/exit{C.RESET}            離開 liamg

{C.BOLD}快捷用法：{C.RESET}
  {C.CLAUDE}/cl 幫我寫一個 FastAPI server{C.RESET}
      → 帶著提示詞直接啟動 Claude Code

  {C.CODEX}/co fix the bug in main.py{C.RESET}
      → 帶著提示詞直接啟動 Codex CLI

{C.DIM}提示：在 Claude/Codex 裡輸入各自的 exit 指令即可回到 liamg{C.RESET}
"""


def find_cli(name: str) -> str | None:
    """找到 CLI 的完整路徑"""
    return shutil.which(name)


def get_version(cli_path: str) -> str:
    """取得 CLI 版本"""
    try:
        result = subprocess.run(
            [cli_path, "--version"],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout.strip() or result.stderr.strip() or "unknown"
    except Exception:
        return "unknown"


def launch_cli(name: str, cli_path: str, prompt: str = ""):
    """啟動指定的 CLI"""
    color = C.CLAUDE if name == "claude" else C.CODEX
    label = "Claude Code" if name == "claude" else "Codex CLI"

    print(f"\n{color}{C.BOLD}▸ 啟動 {label}...{C.RESET}")
    print(f"{C.DIM}  (結束後會回到 liamg){C.RESET}\n")

    cmd = [cli_path]
    if prompt:
        # Claude Code 用 -p 做 one-shot, Codex 直接帶 prompt
        if name == "claude":
            cmd.extend(["-p", prompt])
        else:
            cmd.append(prompt)

    try:
        subprocess.run(cmd, cwd=os.getcwd())
    except KeyboardInterrupt:
        pass

    print(f"\n{C.LIAMG}▸ 已返回 liamg{C.RESET}\n")


def show_status(claude_path: str | None, codex_path: str | None):
    """顯示狀態資訊"""
    print(f"\n{C.BOLD}  CLI 狀態{C.RESET}")
    print(f"  {'─' * 40}")

    if claude_path:
        ver = get_version(claude_path)
        print(f"  {C.CLAUDE}✔ Claude Code{C.RESET}  {ver}")
        print(f"    {C.DIM}{claude_path}{C.RESET}")
    else:
        print(f"  {C.RED}✘ Claude Code  未安裝{C.RESET}")

    if codex_path:
        ver = get_version(codex_path)
        print(f"  {C.CODEX}✔ Codex CLI{C.RESET}    {ver}")
        print(f"    {C.DIM}{codex_path}{C.RESET}")
    else:
        print(f"  {C.RED}✘ Codex CLI    未安裝{C.RESET}")

    print(f"  {'─' * 40}")
    print(f"  {C.CYAN}工作目錄：{C.RESET}{os.getcwd()}\n")


def main():
    # 找到兩個 CLI
    claude_path = find_cli("claude")
    codex_path = find_cli("codex")

    # 如果有傳入初始目錄
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isdir(target):
            os.chdir(target)

    print(BANNER)

    while True:
        try:
            cwd_short = Path(os.getcwd()).name
            prompt = input(
                f"{C.LIAMG}liamg{C.RESET} "
                f"{C.DIM}({cwd_short}){C.RESET} "
                f"{C.BOLD}›{C.RESET} "
            )
        except (KeyboardInterrupt, EOFError):
            print(f"\n{C.YELLOW}👋 再見！{C.RESET}")
            break

        line = prompt.strip()
        if not line:
            continue

        # ── 指令解析 ──
        if line in ("/exit", "/quit", "/q"):
            print(f"\n{C.YELLOW}👋 再見！{C.RESET}")
            break

        elif line == "/help":
            print(HELP_TEXT)

        elif line == "/pwd":
            print(f"  {os.getcwd()}")

        elif line.startswith("/cd "):
            target = line[4:].strip().strip('"').strip("'")
            target = os.path.expanduser(target)
            if os.path.isdir(target):
                os.chdir(target)
                print(f"  {C.CYAN}→{C.RESET} {os.getcwd()}")
            else:
                print(f"  {C.RED}目錄不存在：{target}{C.RESET}")

        elif line == "/status":
            show_status(claude_path, codex_path)

        elif line.startswith("/cl"):
            if not claude_path:
                print(f"  {C.RED}Claude Code 未安裝。請執行 npm i -g @anthropic-ai/claude-code{C.RESET}")
                continue
            extra = line[3:].strip()
            launch_cli("claude", claude_path, extra)

        elif line.startswith("/co"):
            if not codex_path:
                print(f"  {C.RED}Codex CLI 未安裝。請執行 npm i -g @openai/codex{C.RESET}")
                continue
            extra = line[3:].strip()
            launch_cli("codex", codex_path, extra)

        else:
            print(f"  {C.DIM}未知指令。輸入 /help 查看可用指令{C.RESET}")


if __name__ == "__main__":
    main()
