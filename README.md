# 🖥️ Windows Control Bot 🤖

A voice/text-based desktop assistant powered by LLMs and system control tools to help you manage your Windows PC using natural language commands. Built with LangChain, `customtkinter`, and Python system automation tools.

---

## 🚀 Features

- Natural language interaction with a bot to control your PC.
- Clean and modern GUI built using `customtkinter`.
- Integrates with LangChain agents and tools.
- Supports commands like:
  - Increase/Decrease volume
  - Open/Close applications
  - Take screenshots
  - Shutdown or restart the PC
  - Get current time/date
  - And much more...

---

## 🛠️ Tech Stack

- 🧠 LangChain Agents (`ZERO_SHOT_REACT_DESCRIPTION`)
- 🔧 Custom Tool Definitions (`tools.py`)
- 🪟 Windows Automation (via Python modules like `pyautogui`, `pyttsx3`, `pygetwindow`, etc.)
- 💻 `customtkinter` for GUI
- ⚙️ LLM support via `model_setup.py`

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/Windows-Control-Bot.git
cd Windows-Control-Bot

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt
