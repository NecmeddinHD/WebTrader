#First set your chat id
import os
os.system("pyinstaller --onefile --noconsole --add-data config.py --name WebTrader main.py")
