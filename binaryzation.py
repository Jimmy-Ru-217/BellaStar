import cv2
import numpy as np
# 读取图片
img = cv2.imread("C:\\Users\\Hasee\\Desktop\\bella\\bella2x.png")

# 转灰度图片
def big_image_binary(src):
    print(src.shape)
    cw = 256
    ch = 256
    h, w, c = src.shape
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            dst = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
           # ret_otsu, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            gray[row:row+ch, col:col+cw] = dst
            #计算方差和平均值，当这两个数值小于某一值时，可以认为图像为空白，做空白图像过滤
            print(np.std(dst), np.mean(dst))
    f = open('C:\\Users\\Hasee\\Desktop\\bella\\testARRS.txt', 'w+')

    for i in range(len(gray)):
        jointsFrame = gray[i]  # 每行
        for Ji in range(len(jointsFrame)):
            if(jointsFrame[Ji]==0):
                strNum = str(1)
            else:
                strNum = str(0)
            f.write(strNum)
            f.write(' ')
        f.write('\n')
    f.close()
    cv2.imwrite("C:/Users/Hasee/Desktop/bella/big_img_binary.jpg", gray)
big_image_binary(img)