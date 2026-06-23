import numpy as np

def pool_2x2(matrix):
    # 1. 将输入的字符串矩阵转换为整型 NumPy 数组
    arr = np.array(matrix, dtype=int)

    # 2. 检查矩阵的长宽是否为偶数（池化要求）
    h, w = arr.shape
    if h % 2 != 0 or w % 2 != 0:
        raise ValueError("矩阵的行数和列数必须是偶数才能进行 2x2 池化！")

    # 3. 重塑数组形状，以便进行 2x2 窗口操作
    # 将形状从 (h, w) 变为 (h//2, 2, w//2, 2)
    reshaped = arr.reshape(h // 2, 2, w // 2, 2)

    # 4. 在 2x2 的窗口上取最大值（Max Pooling）
    # 保证结果只有 0 和 1
    pooled = reshaped.max(axis=(1, 3))

    # 5. 将结果转回字符串格式的二维列表
    return pooled.astype(str).tolist()



result=[]
with open("testARRS.txt", "r") as f:  # 打开文件
    data = f.readline()
    while data!="":
        result.append(data.split(" ")[:-1])
        data = f.readline()

result = pool_2x2(result)
print(result)