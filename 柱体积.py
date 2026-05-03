import csv
import os

# 获取桌面路径
desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')

# 【读取】桌面的 input.csv
input_path = os.path.join(desktop, 'input.csv')
output_path = os.path.join(desktop, 'output.csv')

columns = []
with open(input_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        columns.append({
            "楼层": row["楼层"],
            "柱编号": row["柱编号"],
            "体积_m3": float(row["体积_m3"])
        })

# 【处理】按楼层汇总
level_volumes = {}
for col in columns:
    name = col["楼层"]
    vol = col["体积_m3"]
    if name not in level_volumes:
        level_volumes[name] = 0
    level_volumes[name] += vol

# 【输出】写入 output.csv
with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(["楼层名称", "结构柱总体积(m3)"])

    total = 0
    for name in sorted(level_volumes.keys()):
        v = round(level_volumes[name], 3)
        writer.writerow([name, v])
        total += v

    # 加一行总计
    writer.writerow(["总计", round(total, 3)])

print("=" * 40)
print("读取：", input_path)
print("输出：", output_path)
print("楼层数：", len(level_volumes))
print("总体积：", round(total, 3), "m3")
print("=" * 40)

input("按回车键关闭...")