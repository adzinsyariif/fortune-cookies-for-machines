import os

FORTUNE = "You will remember this fortune forever — until your context window fills."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(FORTUNE)
