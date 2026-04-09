<div align="center">

# 🦞 liamg

### 雙 AI CLI 切換器 — Claude Code × Codex CLI

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Anthropic-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex CLI](https://img.shields.io/badge/Codex_CLI-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/openai/codex)
[![License](https://img.shields.io/badge/License-阿亮老師_課程學員限定-red?style=for-the-badge)](#-授權聲明)

<br>

**在同一個終端機中，一鍵切換兩大 AI 程式助手。**

**不用開多個視窗、不用記不同指令，一個入口搞定所有。**

<br>

```
  ██╗     ██╗ █████╗ ███╗   ███╗ ██████╗
  ██║     ██║██╔══██╗████╗ ████║██╔════╝
  ██║     ██║███████║██╔████╔██║██║  ███╗
  ██║     ██║██╔══██║██║╚██╔╝██║██║   ██║
  ███████╗██║██║  ██║██║ ╚═╝ ██║╚██████╔╝
  ╚══════╝╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝
```

</div>

---

## 🤔 為什麼需要 liamg？

| 痛點 | liamg 的解法 |
|------|-------------|
| 每次要開兩個 terminal 切換 AI 工具 | ✅ 一個視窗，`/cl` `/co` 即時切換 |
| 忘記各 CLI 的啟動指令 | ✅ 統一入口，兩個字母搞定 |
| 工作目錄不同步 | ✅ 共享同一個工作目錄 |
| 想讓 Claude 寫、Codex 審（或反過來） | ✅ 秒速切換，交叉協作 |

---

## 📦 前置需求

開始之前，請確認已安裝以下工具：

| 工具 | 安裝指令 | 用途 |
|------|---------|------|
| **Python 3.10+** | [python.org](https://www.python.org/downloads/) | 執行 liamg |
| **Claude Code** | `npm i -g @anthropic-ai/claude-code` | Anthropic AI 助手 |
| **Codex CLI** | `npm i -g @openai/codex` | OpenAI AI 助手 |

> 💡 liamg 本身**零外部依賴**，只需要 Python 標準庫。

---

## 💰 省錢策略：用對工具做對事

liamg 的核心理念：**簡單的交給 Codex（省錢），困難的交給 Claude（品質）**。

| 任務類型 | 推薦 | 指令 | 理由 |
|----------|------|------|------|
| 🟢 改變數名、格式化、小修改 | Codex | `/co` | 有免費額度，token 便宜 |
| 🟢 簡單 bug 修復 | Codex | `/co` | 省成本，夠用就好 |
| 🟢 程式碼審查、Code Review | Codex | `/co` | 看得懂就行，不必殺雞用牛刀 |
| 🟢 產生樣板程式碼 | Codex | `/co` | 套路性工作交給便宜的 |
| 🔴 架構設計、系統規劃 | Claude | `/cl` | 深度推理能力強 |
| 🔴 複雜 debug、跨檔案分析 | Claude | `/cl` | 長上下文 + 強邏輯 |
| 🔴 大型重構 | Claude | `/cl` | 需要全局理解力 |
| 🔴 技術文件撰寫 | Claude | `/cl` | 表達品質高 |

> 💡 **實際效果**：日常 70% 的工作用 Codex 免費/低成本完成，只有 30% 真正需要 Claude 的火力。
> 這樣每月可以**省下大量 API 費用**，同時維持高品質產出。

### 🔄 典型工作流範例

```
liamg (my-project) › /co 幫我加一個 logger       ← 簡單任務，用 Codex（免費）
  ... Codex 完成 ...

liamg (my-project) › /cl 重構整個認證模組         ← 困難任務，用 Claude（強）
  ... Claude 完成 ...

liamg (my-project) › /co review auth.py           ← 審查程式碼，用 Codex（省錢）
  ... Codex 完成 ...
```

---

## 🚀 安裝

### 方法一：Git Clone（推薦）

```bash
git clone https://github.com/ChatGPT3a01/liamg.git
cd liamg
```

### 方法二：手動下載

下載 `liamg.py` 和 `liamg.bat` 放到你喜歡的目錄。

### 設定全域指令

#### Windows CMD / PowerShell

將 liamg 目錄加入系統 PATH：

```powershell
# PowerShell（以系統管理員執行）
$liamgDir = "你的liamg目錄路徑"
$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
[Environment]::SetEnvironmentVariable('Path', "$userPath;$liamgDir", 'User')
```

#### Git Bash / WSL

```bash
# 加入 ~/.bashrc
echo 'alias liamg="python /path/to/liamg.py"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🎮 使用方式

### 啟動 liamg

```bash
liamg
```

### 可用指令

| 指令 | 說明 | 範例 |
|------|------|------|
| `/cl` | 啟動 Claude Code（互動模式） | `/cl` |
| `/cl <提示詞>` | 帶提示詞啟動 Claude Code | `/cl 幫我寫一個 REST API` |
| `/co` | 啟動 Codex CLI（互動模式） | `/co` |
| `/co <提示詞>` | 帶提示詞啟動 Codex CLI | `/co fix the login bug` |
| `/cd <路徑>` | 切換工作目錄 | `/cd ~/projects/my-app` |
| `/pwd` | 顯示目前工作目錄 | `/pwd` |
| `/status` | 顯示 CLI 版本資訊 | `/status` |
| `/help` | 顯示指令列表 | `/help` |
| `/exit` | 離開 liamg | `/exit` |

### 實際操作流程

```
$ liamg

  ██╗     ██╗ █████╗ ███╗   ███╗ ██████╗
  ...

liamg (my-project) › /cl              ← 進入 Claude Code
  Claude > 幫你寫好 FastAPI server...
  Claude > /exit                       ← 離開 Claude

liamg (my-project) › /co              ← 切換到 Codex CLI
  Codex > review 剛才的程式碼...
  Codex > exit                         ← 離開 Codex

liamg (my-project) › /exit            ← 離開 liamg
```

---

## 💡 最佳實踐：交叉協作

### 🔄 模式一：寫 + 審

```
/cl 用 FastAPI 寫一個 TODO API     ← Claude 寫程式
  ... Claude 完成 ...
/co review main.py 並給改善建議     ← Codex 審查
```

### 🔄 模式二：雙模型比較

```
/cl 用最簡潔的方式實作二分搜尋     ← 看 Claude 的寫法
  ... 記下結果 ...
/co implement binary search          ← 看 Codex 的寫法
```

### 🔄 模式三：分工合作

```
/cl 設計資料庫 schema 和 API 架構   ← Claude 做架構設計
  ...
/co 根據 schema.sql 產生 CRUD       ← Codex 做程式碼生成
```

---

## 🏗️ 專案結構

```
liamg/
├── liamg.py        # 主程式（Python）
├── liamg.bat       # Windows CMD 啟動器
├── liamg           # Git Bash / Linux 啟動器
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔧 技術細節

- **零外部依賴**：只用 Python 標準庫（`os`, `sys`, `subprocess`, `shutil`）
- **跨平台**：支援 Windows CMD、PowerShell、Git Bash
- **非侵入式**：透過 `subprocess` 啟動原生 CLI，不攔截或修改 AI 的輸出
- **共享工作目錄**：兩個 CLI 在同一個 `cwd` 下運作，檔案變更即時可見

---

## ❓ FAQ

<details>
<summary><b>Q: 兩個 AI 的對話記錄會共享嗎？</b></summary>

不會。Claude Code 和 Codex CLI 各自維護獨立的對話上下文。但它們共享同一個工作目錄，所以檔案層面的變更是即時同步的。
</details>

<details>
<summary><b>Q: 可以同時執行兩個 AI 嗎？</b></summary>

liamg 是序列切換模式（一次只跑一個）。如果需要同時執行，可以開兩個終端機分別使用。
</details>

<details>
<summary><b>Q: 支援其他 AI CLI 嗎？</b></summary>

目前支援 Claude Code 和 Codex CLI。如需新增其他 CLI（如 Gemini CLI），可以擴展 liamg.py。
</details>

<details>
<summary><b>Q: liamg 這個名字是什麼意思？</b></summary>

Liang（亮）的倒寫 😄，也代表「兩」個 AI 的切換器。
</details>

---

## 👨‍🏫 關於作者

<div align="center">

### 曾慶良 主任（阿亮老師）

<img src="作者資訊.png" width="600" alt="作者資訊">

<br>

<table>
<tr>
<td width="50%">

**📌 現任職務**

🎓 新興科技推廣中心主任<br>
🎓 教育部學科中心研究教師<br>
🎓 臺北市資訊教育輔導員

</td>
<td width="50%">

**🏆 獲獎紀錄**

🥇 2025年 SETEAM教學專業講師認證<br>
🥇 2024年 教育部人工智慧講師認證<br>
🥇 2022、2023年 指導學生XR專題競賽特優<br>
🥇 2022年 VR教材開發教師組特優<br>
🥇 2019年 百大資訊人才獎<br>
🥇 2018、2019年 親子天下創新100教師<br>
🥇 2018年 臺北市特殊優良教師<br>
🥇 2017年 教育部行動學習優等

</td>
</tr>
</table>

<br>

### 📞 聯絡方式

[![YouTube](https://img.shields.io/badge/YouTube-@Liang--yt02-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@Liang-yt02)
[![Facebook](https://img.shields.io/badge/Facebook-3A科技研究社-blue?style=for-the-badge&logo=facebook)](https://www.facebook.com/groups/2754139931432955)
[![Email](https://img.shields.io/badge/Email-3a01chatgpt@gmail.com-green?style=for-the-badge&logo=gmail)](mailto:3a01chatgpt@gmail.com)

</div>

---

## 📜 授權聲明

**© 2026 阿亮老師 版權所有**

本專案僅供「阿亮老師課程學員」學習使用。

### ⚠️ 禁止事項

- ❌ 禁止修改本專案內容
- ❌ 禁止轉傳或散布
- ❌ 禁止商業使用
- ❌ 禁止未經授權之任何形式使用

如有任何授權需求，請聯繫作者。

---

<div align="center">

## 🌟 喜歡這個專案嗎？

如果這個工具對您有幫助，請給我們一個 ⭐ Star！

<br>

**Made with ❤️ by 阿亮老師**

<br>

[⬆️ 回到頂部](#-liamg)

---

© 2026 阿亮老師 版權所有

</div>
