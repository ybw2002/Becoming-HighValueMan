import os
import re
import matplotlib.pyplot as plt
from datetime import datetime

folder = "discipline"
scores = []

# 遍历所有打卡文件
for fname in sorted(os.listdir(folder)):
    if fname.endswith(".md"):
        path = os.path.join(folder, fname)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        # 正则匹配自律分数
        match = re.search(r"\| 自律（discipline） \| (\d) \|", content)
        if match:
            score = int(match.group(1))
            date = fname.replace(".md", "")
            scores.append((date, score))

# 画图
dates = [datetime.strptime(d, "%Y-%m-%d") for d, _ in scores]
values = [s for _, s in scores]

plt.figure(figsize=(8, 4))
plt.plot(dates, values, marker="o", color="gold", linewidth=2)
plt.title("每日 Discipline 得分曲线")
plt.ylabel("打分（满分 5）")
plt.xlabel("日期")
plt.ylim(0, 5.5)
plt.grid(True)
plt.tight_layout()
plt.savefig("progress.png", dpi=150)
print("✅ 成长图已生成：progress.png")
