# ♟️ Chess Automation Bot

An intelligent bot built using **Python** and **Selenium** to automate gameplay on [Chess.com](https://www.chess.com). This bot mimics human-like gameplay by detecting the board state and making autonomous moves in real-time.

## 🚀 Features

- 🌐 **Web Automation**: Opens a web browser and navigates to Chess.com using Selenium.
- 🧠 **Move Detection**: Detects the current board state to determine the next legal move.
- 🕹️ **Minimal User Interaction**: Start the bot and let it handle the game.

## 🔧 Tech Stack

- Python  
- Selenium WebDriver  
- Stockfish Chess Engine for move logic

## 🛠️ Future Enhancements

- Integrate Stockfish for smarter move decisions
- GUI control panel for starting/stopping the bot
- Difficulty adjustment
- Multi-platform support (desktop/browser)


## 📂 How to Run

```bash
git clone https://github.com/yourusername/chess-automation-bot
cd chess-automation-bot
pip install -r requirements.txt
Download Stockfish from https://stockfishchess.org/download/ 
Add the path of Stockfish Executable file in line 13 in chess.py file.
Run gui.py.
Click on online or offline button while playing respective modes at the time of your move.
When playing new game click reset button to reset the position of last match.

