import  lzma
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#data總共22bytes
data=b"abcdefghijklmnopqrstuv"

#file讀進來, 是一個一條直線的array, 所以要轉成512*512的array才會是圖片的二維格式
imgRaw=np.fromfile("Lena.raw", dtype=np.uint8)
imgRaw_afterReshape=imgRaw.reshape([512, 512])
print(imgRaw_afterReshape)

#把圖片show出來, 是以graylevel show出來
plt.imshow(imgRaw_afterReshape, cmap='gray')
plt.show()


#原本紀錄在array的pixel改成用string存
imgRaw_toString=imgRaw.tostring()
print(imgRaw_toString)

with lzma.open("afile.lzma", "w", format=lzma.FORMAT_ALONE) as f:
    f.write(imgRaw_toString)

file_content=0
with lzma.open("afile.lzma", format=lzma.FORMAT_ALONE) as f:
    file_content = f.read()


#把decode過後的pixel stream轉換為array, 再轉換為512*512, 再用graylevel show出來
img_after_decompress=file_content
print(img_after_decompress)
img_after_decompress=np.frombuffer(img_after_decompress, dtype=np.uint8)
print(img_after_decompress)
img_after_decompress=img_after_decompress.reshape([512, 512])
plt.imshow(img_after_decompress, cmap='gray')
plt.show()

#觀察壓縮過後的bit長成甚麼樣子
file_compress=lzma.compress(file_content, format=lzma.FORMAT_ALONE)
print(file_compress)
