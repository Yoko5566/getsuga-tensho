import os
import sys
from pathlib import Path


# Use the executable folder when packaged, otherwise use the script folder.
if getattr(sys, "frozen", False):
    app_folder = Path(sys.executable).parent
else:
    app_folder = Path(__file__).parent


txt_file = app_folder / "test.txt"


# Reset the story every time the game starts.
with open(txt_file, "w", encoding="utf-8") as file:
    file.write("失魂界.....友哈巴赫 在你面前")


print("================================")
print("        月牙天沖")
print("================================")
print()
print("失魂界陷入危機……")
print()


while True:
    command = input("請輸入指令：").strip()

    if command == "月牙天沖":
        with open(txt_file, "a", encoding="utf-8") as file:
            file.write("\n\n月牙天沖")
            file.write("\n\n友哈巴赫 被消滅")
            file.write("\n你又拯救了失魂界 感謝你的努力!")

        print()
        print("月牙天沖施放成功！")
        print("友哈巴赫已被消滅！")
        print()
        print("正在開啟戰鬥結果...")

        os.startfile(txt_file)

        print()
        input("按 Enter 鍵結束程式...")
        break

    else:
        print("沒有這個招式，請重新輸入。")
        print()
