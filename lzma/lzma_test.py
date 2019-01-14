import  lzma
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#data總共22bytes
data=b"abcdefghijklmnopqrstuv"

imgRaw=np.fromfile("Lena.raw", dtype=np.uint8)
imgRaw_afterReshape=imgRaw.reshape([512, 512])
print(imgRaw_afterReshape)

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


img_after_decompress=file_content
print(img_after_decompress)
img_after_decompress=np.frombuffer(img_after_decompress, dtype=np.uint8)
print(img_after_decompress)
img_after_decompress=img_after_decompress.reshape([512, 512])
plt.imshow(img_after_decompress, cmap='gray')
plt.show()

file_compress=lzma.compress(file_content, format=lzma.FORMAT_ALONE)
print(file_compress)
