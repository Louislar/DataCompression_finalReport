import  lzma
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#data總共22bytes
data=b"abcdefghijklmnopqrstuv"

imgRaw=np.fromfile("Lena.raw", dtype=np.uint8)
imgRaw=imgRaw.reshape([512, 512])
print(imgRaw)

plt.imshow(imgRaw, cmap='gray')
plt.show()



with lzma.open("afile.lzma", "w", format=lzma.FORMAT_ALONE) as f:
    f.write(data)

file_content=0
with lzma.open("afile.lzma", format=lzma.FORMAT_ALONE) as f:
    file_content = f.read()

print(file_content)

file_compress=lzma.compress(file_content)
print(file_compress)
