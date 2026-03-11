import os
import random
from datetime import datetime

# 配置
LOG_FILE = "contribution_log.txt"

def generate_random_message():
    messages = [
        "chore: daily contribution update",
        "docs: update project documentation",
        "refactor: optimize internal logic",
        "style: adjust UI/UX elements",
        "fix: minor bug fixes and improvements",
        "feat: add new design exploration snippet"
    ]
    return random.choice(messages)

def main():
    # 确保日志文件存在
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("# Contribution Log\n")
    
    # 写入当前时间戳
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().isoformat()} - Automated daily update\n")
    
    print(f"Successfully updated {LOG_FILE}")

if __name__ == "__main__":
    main()
