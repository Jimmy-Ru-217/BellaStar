result=[]
import json
with open("testARRS.txt", "r") as f:  # 打开文件
    data = f.readline()
    while data!="":
        result.append(data.split(" ")[:-1])
        data = f.readline()
print(len(result))
print(result)
with open("output.json", "w", encoding="utf-8") as f:
    # 去掉 indent=4，直接写入
    json.dump(result, f)
sum=0
for i in range(len(result)):
    for j in range(len(result[i])):
        if(result[i][j]=="1"):
            sum+=1
print(sum)