## 🎵 Study Playlist Automation with Python

### 📄 Overview

This is a Python-based project designed to automate the quick launch of study music playlists in Microsoft Edge, using the YouTube platform. It simulates human interactions with the operating system and browser to streamline the start of focused study sessions.

> ⚠️ **Note:** This script is mapped to a specific screen and system layout (Windows 11). Coordinates and behaviors may need adjustment on other setups.

---

### 🧠 Features

* Automatically opens Microsoft Edge
* Navigates to YouTube
* Searches for a specific ambient music playlist
* Starts playback with minimal user input
* Includes time delays to simulate natural usage

---

### 🖥️ Requirements

* Python 3.x
* `pyautogui`
* Windows 11 (or a similarly configured system)
* Screen resolution and layout matching the coordinates used in the script

You can install the required Python package with:

```bash
pip install pyautogui
```

---

### 🚀 How It Works

1. Presses the Windows key and launches **Microsoft Edge**
2. Opens `YouTube.com`
3. Searches for `"skyrim ambient music everness"`
4. Clicks to play the video automatically

The script uses fixed screen coordinates, such as:

```python
pa.click(x=1008, y=30)  # Address bar
pa.click(x=531, y=103)  # YouTube search bar
pa.click(x=527, y=271)  # First video result
```

These may require calibration for different systems.

### ⏱️ Timers and Automation

The script uses `time.sleep()` and `pa.PAUSE` to introduce natural delays between actions. You can customize these to fine-tune responsiveness or add productivity timers.

### ⚠️ Disclaimer

* This automation is system-specific and not universally portable.
* It’s intended for personal use on Windows 11.
* You should avoid running this script while doing other tasks, as it takes control of mouse and keyboard input.

### 📌 Future Improvements (Suggestions)

* Make screen coordinates dynamic based on window size
* Add GUI for selecting playlist themes
* Include Pomodoro-style timer integration
