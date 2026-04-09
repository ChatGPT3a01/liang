<div align="center">

# 🦞 liang

### 雙 AI CLI 切換器 — Claude Code × Codex CLI

<br>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Anthropic-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex CLI](https://img.shields.io/badge/Codex_CLI-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/openai/codex)
[![Zero Deps](https://img.shields.io/badge/依賴-零外部依賴-28A745?style=for-the-badge)](#-技術細節)
[![License](https://img.shields.io/badge/授權-阿亮老師課程專用-FF4444?style=for-the-badge)](#-授權聲明)

<br>

**在同一個終端機中，一鍵切換兩大 AI 程式助手**

**簡單任務用 Codex（省錢）｜困難任務用 Claude（品質）**

<br>

```
  ██╗     ██╗ █████╗ ███╗   ██╗ ██████╗
  ██║     ██║██╔══██╗████╗  ██║██╔════╝
  ██║     ██║███████║██╔██╗ ██║██║  ███╗
  ██║     ██║██╔══██║██║╚██╗██║██║   ██║
  ███████╗██║██║  ██║██║ ╚████║╚██████╔╝
  ╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝
```

<br>

</div>

---

## 📋 目錄

- [🤔 為什麼需要 liang？](#-為什麼需要-liang)
- [💰 省錢策略](#-省錢策略用對工具做對事)
- [📦 前置需求](#-前置需求)
- [🚀 安裝](#-安裝)
- [🔐 首次登錄設定](#-首次登錄設定)
- [🎮 使用方式](#-使用方式)
- [💡 最佳實踐：交叉協作](#-最佳實踐交叉協作)
- [❓ FAQ](#-faq)
- [👨‍🏫 關於作者](#-關於作者)
- [📜 授權聲明](#-授權聲明)

---

## 🤔 為什麼需要 liang？

<div align="center">

```
你現在的工作流：                      用了 liang 之後：

┌──────────┐  ┌──────────┐           ┌──────────────────┐
│ Terminal 1│  │ Terminal 2│           │   Terminal 1     │
│  claude   │  │  codex    │    ──►   │   liang          │
│           │  │           │           │   /cl  /co 切換  │
└──────────┘  └──────────┘           └──────────────────┘
  來回切換 😫    目錄不同步              一個入口搞定 ✅
```

</div>

<table>
<tr>
<td width="50%">

### 😫 以前的痛點

- ❌ 每次要開兩個 terminal 切換 AI 工具
- ❌ 忘記各 CLI 的啟動指令
- ❌ 工作目錄不同步
- ❌ 想讓 Claude 寫、Codex 審，來回很麻煩

</td>
<td width="50%">

### ✅ liang 的解法

- ✅ 一個視窗，`/cl` `/co` 即時切換
- ✅ 統一入口，兩個字母搞定
- ✅ 共享同一個工作目錄
- ✅ 秒速切換，交叉協作

</td>
</tr>
</table>

---

## 💰 省錢策略：用對工具做對事

<div align="center">

**liang 的核心理念：簡單的交給 Codex（省錢），困難的交給 Claude（品質）**

</div>

<br>

<table>
<tr>
<td width="50%">

### 🟢 用 Codex（`/co`）— 省錢

| 任務 | 理由 |
|:---|:---|
| 📝 改變數名、格式化、小修改 | 有免費額度，token 便宜 |
| 🐛 簡單 bug 修復 | 省成本，夠用就好 |
| 🔍 程式碼審查 Code Review | 不必殺雞用牛刀 |
| 📄 產生樣板程式碼 | 套路性工作交給便宜的 |

</td>
<td width="50%">

### 🔴 用 Claude（`/cl`）— 品質

| 任務 | 理由 |
|:---|:---|
| 🏗️ 架構設計、系統規劃 | 深度推理能力強 |
| 🔬 複雜 debug、跨檔案分析 | 長上下文 + 強邏輯 |
| ♻️ 大型重構 | 需要全局理解力 |
| 📖 技術文件撰寫 | 表達品質高 |

</td>
</tr>
</table>

<div align="center">

<br>

> 💡 **實際效果**：日常 **70%** 的工作用 Codex 免費/低成本完成，只有 **30%** 真正需要 Claude 的火力
>
> 每月可以 **省下大量 API 費用** 💰，同時維持高品質產出

<br>

```
典型工作流：

liang › /co 幫我加一個 logger         ← 🟢 簡單任務，用 Codex（免費）
        ↓ 完成 ↓
liang › /cl 重構整個認證模組           ← 🔴 困難任務，用 Claude（強）
        ↓ 完成 ↓
liang › /co review auth.py            ← 🟢 審查程式碼，用 Codex（省錢）
```

</div>

---

## 📦 從零開始完整安裝教學

> 🎯 **跟著以下 6 個步驟，10 分鐘內完成所有設定！**

<div align="center">

```
Step 1        Step 2        Step 3        Step 4        Step 5        Step 6
安裝 Python → 安裝 Node.js → 安裝 AI CLI → 下載 liang → 設定指令 → 登錄帳號
  🐍            📦            🤖            🦞            ⚙️            🔐
```

</div>

---

### Step 1️⃣ 安裝 Python 3.10+

<table>
<tr>
<td width="50%">

**🪟 Windows**

1. 前往 [python.org/downloads](https://www.python.org/downloads/)
2. 下載最新版 Python
3. 安裝時 **務必勾選** ✅ `Add Python to PATH`
4. 驗證安裝：

```powershell
python --version
# 應顯示 Python 3.10 以上
```

</td>
<td width="50%">

**🍎 macOS / 🐧 Linux**

```bash
# macOS（用 Homebrew）
brew install python

# Ubuntu / Debian
sudo apt install python3

# 驗證安裝
python3 --version
```

</td>
</tr>
</table>

> 💡 如果已經裝過 Python，跳過這步！

---

### Step 2️⃣ 安裝 Node.js（npm）

Claude Code 和 Codex CLI 都透過 npm 安裝，所以需要 Node.js。

<table>
<tr>
<td width="50%">

**🪟 Windows**

1. 前往 [nodejs.org](https://nodejs.org/)
2. 下載 **LTS 版本**（推薦）
3. 安裝後驗證：

```powershell
node --version
npm --version
```

</td>
<td width="50%">

**🍎 macOS / 🐧 Linux**

```bash
# macOS
brew install node

# Ubuntu / Debian
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install nodejs

# 驗證
node --version && npm --version
```

</td>
</tr>
</table>

---

### Step 3️⃣ 安裝兩個 AI CLI

打開終端機，執行以下指令安裝兩大 AI 助手：

```bash
# 安裝 Claude Code（Anthropic）
npm install -g @anthropic-ai/claude-code

# 安裝 Codex CLI（OpenAI）
npm install -g @openai/codex
```

驗證安裝：

```bash
claude --version     # 應顯示 Claude Code 版本
codex --version      # 應顯示 Codex CLI 版本
```

<details>
<summary>⚠️ <b>安裝失敗？常見問題排除（點擊展開）</b></summary>

<br>

| 問題 | 解法 |
|:---|:---|
| `npm: command not found` | 回到 Step 2 安裝 Node.js |
| `EACCES permission denied` | macOS/Linux 加 `sudo`，或用 [nvm](https://github.com/nvm-sh/nvm) 管理 Node |
| `EPERM` (Windows) | 用**系統管理員**開啟 CMD / PowerShell |
| 安裝超慢 | 換源：`npm config set registry https://registry.npmmirror.com` |

</details>

---

### Step 4️⃣ 下載 liang

<table>
<tr>
<td width="50%">

**方法 A：Git Clone（推薦）**

```bash
git clone https://github.com/ChatGPT3a01/liang.git
cd liang
```

</td>
<td width="50%">

**方法 B：手動下載**

1. 前往 [GitHub 頁面](https://github.com/ChatGPT3a01/liang)
2. 點擊綠色 **Code** 按鈕
3. 選擇 **Download ZIP**
4. 解壓縮到你喜歡的位置

</td>
</tr>
</table>

---

### Step 5️⃣ 設定全域指令

讓你在任何目錄都能直接輸入 `liang` 啟動。

<table>
<tr>
<td width="50%">

**🪟 Windows CMD / PowerShell**

```powershell
# 用 PowerShell 執行（以系統管理員）
$liangDir = "C:\你的路徑\liang"
$userPath = [Environment]::GetEnvironmentVariable(
    'Path', 'User')
[Environment]::SetEnvironmentVariable(
    'Path', "$userPath;$liangDir", 'User')
```

設定後**重新開啟**終端機，輸入：

```powershell
liang
```

</td>
<td width="50%">

**🐧 Git Bash / WSL / macOS**

```bash
# 加入 alias 到 shell 設定檔
echo 'alias liang="python /你的路徑/liang.py"' \
    >> ~/.bashrc
source ~/.bashrc
```

設定後輸入：

```bash
liang
```

</td>
</tr>
</table>

> 💡 看到 LIANG 的 ASCII art 歡迎畫面就代表安裝成功！🎉

---

### Step 6️⃣ 首次登錄 AI 帳號

> ⚠️ **第一次使用前，必須登錄兩個 AI 服務！登錄只需做一次。**

#### 6-A：登錄 Claude Code

```bash
claude
```

首次執行會自動開啟瀏覽器引導登錄：

| 方式 | 說明 |
|:---:|:---|
| 🌐 **Anthropic 帳號** | 開啟瀏覽器 → 登入 → 自動授權完成 |
| 🔑 **API Key** | 輸入 `sk-ant-...` 金鑰 |

👉 API Key 從 [console.anthropic.com](https://console.anthropic.com/) 取得

登錄成功後輸入 `/exit` 離開 Claude Code。

#### 6-B：登錄 Codex CLI

```bash
codex
```

首次執行會自動引導登錄：

| 方式 | 說明 |
|:---:|:---|
| 🌐 **OpenAI 帳號** | 開啟瀏覽器 → 登入 → 自動授權完成 |
| 🔑 **API Key** | 設定環境變數 `OPENAI_API_KEY` |

👉 API Key 從 [platform.openai.com](https://platform.openai.com/api-keys) 取得

<details>
<summary>📋 <b>Codex API Key 手動設定方式（點擊展開）</b></summary>

<br>

```powershell
# ── Windows PowerShell ──

# 臨時（只在當前視窗有效）
$env:OPENAI_API_KEY = "sk-..."

# 永久（重啟後仍有效，推薦）
[Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'sk-...', 'User')
```

```bash
# ── Git Bash / Linux / macOS ──

# 臨時
export OPENAI_API_KEY="sk-..."

# 永久（推薦）
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.bashrc
source ~/.bashrc
```

</details>

#### 6-C：驗證登錄狀態 ✅

啟動 liang 後輸入 `/status`，確認兩個 CLI 都顯示 ✔：

```
$ liang

liang (my-project) › /status

  CLI 狀態
  ────────────────────────────────────────
  ✔ Claude Code  2.x.x (Claude Code)    ← 看到 ✔ 就對了！
  ✔ Codex CLI    codex-cli 0.x.x        ← 看到 ✔ 就對了！
  ────────────────────────────────────────
```

<div align="center">

### 🎉 恭喜！安裝完成！

**現在輸入 `/cl` 或 `/co` 就能開始使用了！**

</div>

> 💡 **登錄只需要做一次**，之後 liang 會自動沿用已儲存的認證。

---

## 🎮 使用方式

### 啟動 liang

```bash
liang
```

### 📌 可用指令

| 指令 | 說明 | 範例 |
|:---:|:---|:---|
| 🟠 `/cl` | 啟動 Claude Code（互動模式） | `/cl` |
| 🟠 `/cl <提示詞>` | 帶提示詞啟動 Claude Code | `/cl 幫我寫一個 REST API` |
| 🟢 `/co` | 啟動 Codex CLI（互動模式） | `/co` |
| 🟢 `/co <提示詞>` | 帶提示詞啟動 Codex CLI | `/co fix the login bug` |
| 📂 `/cd <路徑>` | 切換工作目錄 | `/cd ~/projects/my-app` |
| 📂 `/pwd` | 顯示目前工作目錄 | `/pwd` |
| ℹ️ `/status` | 顯示 CLI 版本資訊 | `/status` |
| ❓ `/help` | 顯示指令列表 | `/help` |
| 🚪 `/exit` | 離開 liang | `/exit` |

### 🖥️ 實際操作流程

```
$ liang

  ██╗     ██╗ █████╗ ███╗   ██╗ ██████╗
  ██║     ██║██╔══██╗████╗  ██║██╔════╝
  ...
  雙 AI CLI 切換器 — Claude Code × Codex CLI

liang (my-project) › /cl              ← 🟠 進入 Claude Code
  Claude > 幫你寫好 FastAPI server...
  Claude > /exit                       ← 離開 Claude

liang (my-project) › /co              ← 🟢 切換到 Codex CLI
  Codex > review 剛才的程式碼...
  Codex > exit                         ← 離開 Codex

liang (my-project) › /exit            ← 🚪 離開 liang
```

---

## 💡 最佳實踐：交叉協作

<table>
<tr>
<td width="33%">

### 🔄 模式一：寫 + 審

```
/cl 用 FastAPI 寫 TODO API
  ← Claude 寫程式
  ... 完成 ...

/co review main.py
  ← Codex 審查
  ... 完成 ...
```

**Claude 負責寫**
**Codex 負責審**

</td>
<td width="33%">

### 🔄 模式二：雙模型比較

```
/cl 用最簡潔方式實作
    二分搜尋
  ... 看 Claude 寫法 ...

/co implement binary
    search
  ... 看 Codex 寫法 ...
```

**比較兩家的解法**
**取長補短**

</td>
<td width="33%">

### 🔄 模式三：分工合作

```
/cl 設計資料庫 schema
    和 API 架構
  ← Claude 做設計

/co 根據 schema.sql
    產生 CRUD
  ← Codex 做生成
```

**Claude 做架構**
**Codex 做實作**

</td>
</tr>
</table>

---

## 🏗️ 專案結構

```
liang/
├── 🐍 liang.py        # 主程式（Python，零外部依賴）
├── 🪟 liang.bat       # Windows CMD / PowerShell 啟動器
├── 🐧 liang           # Git Bash / Linux / macOS 啟動器
├── 🖼️ 作者資訊.png     # 作者資訊圖片
├── 📄 .gitignore
├── 📄 LICENSE
└── 📖 README.md
```

---

## 🔧 技術細節

<table>
<tr>
<td width="25%" align="center">

**🚫 零外部依賴**

只用 Python 標準庫
`os` `sys` `subprocess`

</td>
<td width="25%" align="center">

**💻 跨平台**

Windows CMD
PowerShell
Git Bash

</td>
<td width="25%" align="center">

**🔒 非侵入式**

透過 subprocess 啟動
不攔截 AI 輸出

</td>
<td width="25%" align="center">

**📂 共享目錄**

兩個 CLI 同一個 cwd
檔案變更即時可見

</td>
</tr>
</table>

---

## ❓ FAQ

<details>
<summary><b>Q: 兩個 AI 的對話記錄會共享嗎？</b></summary>

<br>

不會。Claude Code 和 Codex CLI 各自維護獨立的對話上下文。但它們共享同一個工作目錄，所以檔案層面的變更是即時同步的。

</details>

<details>
<summary><b>Q: 可以同時執行兩個 AI 嗎？</b></summary>

<br>

liang 是序列切換模式（一次只跑一個）。如果需要同時執行，可以開兩個終端機分別使用。

</details>

<details>
<summary><b>Q: 支援其他 AI CLI 嗎？</b></summary>

<br>

目前支援 Claude Code 和 Codex CLI。如需新增其他 CLI（如 Gemini CLI），可以擴展 `liang.py`。

</details>

<details>
<summary><b>Q: liang 這個名字是什麼意思？</b></summary>

<br>

取自阿「亮」老師的「亮」（Liang）😄，也諧音「兩」— 代表「兩」個 AI 的切換器。

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

[![YouTube](https://img.shields.io/badge/YouTube-@Liang--yt02-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@Liang-yt02)
[![Facebook](https://img.shields.io/badge/Facebook-3A科技研究社-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/groups/2754139931432955)
[![Email](https://img.shields.io/badge/Email-3a01chatgpt@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:3a01chatgpt@gmail.com)

</div>

---

## 📜 授權聲明

```
© 2026 阿亮老師 版權所有

本專案僅供「阿亮老師課程學員」學習使用。

⚠️ 禁止事項：
  ❌ 禁止修改本專案內容
  ❌ 禁止轉傳或散布
  ❌ 禁止商業使用
  ❌ 禁止未經授權之任何形式使用

如有任何授權需求，請聯繫作者。
```

---

<div align="center">

## 🌟 喜歡這個專案嗎？

如果這個工具對您有幫助，請給我們一個 ⭐ Star！

<br>

**Made with ❤️ by 阿亮老師**

<br>

[⬆️ 回到頂部](#-liang)

---

© 2026 阿亮老師 版權所有

</div>
