import cv2
import numpy as np
img = cv2.imread("C:\\Users\\Hasee\\Desktop\\bella\\big_img_binary.jpg")
print(len(img.astype(np.int8)[img==1]))