import cv2
import numpy as np


def big_image_binary(src):
    print("原图尺寸:", src.shape)
    h, w, c = src.shape

    # 1. 转为灰度图
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # 【核心功能优化】使用双边滤波：保留人物强边缘，模糊楼梯/木纹等弱边缘
    # d=9 (邻域直径), sigmaColor=75 (颜色空间标准差), sigmaSpace=75 (坐标空间标准差)
    # 如果觉得楼梯还不够模糊，可以适当调大后两个参数（例如 100, 100）
    gray = cv2.bilateralFilter(gray, d=9, sigmaColor=10, sigmaSpace=10)

    # 分块参数
    cw, ch = 256, 256

    # 2. 分块进行自适应二值化
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            # 获取当前块的实际边界（防止越界）
            row_end = min(row + ch, h)
            col_end = min(col + cw, w)

            roi = gray[row:row_end, col:col_end]

            # 自适应二值化参数调整：
            # BlockSize(参数5) 设为 31（必须为奇数），C(参数6) 设为 15~25 之间。
            # 增大 C 值可以过滤掉更多像楼梯这样对比度不高的区域。
            dst = cv2.adaptiveThreshold(
                roi, 255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                31, 25
            )

            gray[row:row_end, col:col_end] = dst

            # 打印当前块的统计信息（可选）
            # print(f"Block[{row},{col}] -> Std: {np.std(dst):.2f}, Mean: {np.mean(dst):.2f}")

    # 3. 【性能极限优化】利用 NumPy 矩阵操作代替双重 for 循环，瞬间生成文本
    print("正在导出文本数据...")
    # 建立映射：0(黑色边缘)转为'1'，255(白色背景)转为'0'
    binary_mapped = np.where(gray == 0, '1', '0')

    # 批量拼接并写入文件
    with open('testARRS.txt', 'w+') as f:
        # 将每一行用空格拼接，末尾加换行符
        lines = [' '.join(row) + '\n' for row in binary_mapped]
        f.writelines(lines)

    # 4. 保存二值化效果图
    cv2.imwrite("big_img_binary.jpg", gray)
    print("处理完成！结果已保存。")

# 调用示例
img = cv2.imread("pic.jpg")
big_image_binary(img)