import  lzma
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#data總共22bytes
data=b"abcdefghijklmnopqrstuv"


#isShowImg是讓使用者決定要不要顯示圖片
def readInRawImg(filePath, imgShape, isShowImg):
    # file讀進來, 是一個一條直線的array, 所以要轉成512*512的array才會是圖片的二維格式
    imgRaw = np.fromfile(filePath, dtype=np.uint8)  #若是跟這個.py檔案放在一起，就直接打檔名即可

    if(isShowImg):
        #若是要show出圖片就要將原本一維的array修改成二維的
        imgRaw_afterReshape = imgRaw.reshape(imgShape) #imgShape example [512, 512]
        print(imgRaw_afterReshape)
        # 把圖片show出來, 是以graylevel show出來
        plt.imshow(imgRaw_afterReshape, cmap='gray')
        plt.show()

    # 原本紀錄在array的pixel改成用string存
    imgRaw_toString = imgRaw.tostring()
    print(imgRaw_toString)
    return imgRaw_toString
    pass




#raw檔讀入
imgRaw_toString=readInRawImg("Lena.raw", [512, 512], True)
#jpeg檔讀入
imgJpeg_toString=readInRawImg("Lena_jpeg_format.jpg", [512, 512], False)
#png檔讀入
imgPng_toString=readInRawImg("Lena_png_format.png", [512, 512], False)

with lzma.open("afile.lzma", "w", format=lzma.FORMAT_ALONE) as f:
    f.write(imgRaw_toString)

#對已經壓縮過後的jpeg再做一次LZMA壓縮
with lzma.open("afterJpegThenLzma.lzma", "w", format=lzma.FORMAT_ALONE) as f:
    f.write(imgJpeg_toString)

#對已經壓縮過後的png再做一次LZMA壓縮
with lzma.open("afterPngThenLzma.lzma", "w", format=lzma.FORMAT_ALONE) as f:
    f.write(imgPng_toString)

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
#壓縮過後的bit轉成array, 以方便做PSNR的計算
file_compress_afterCompress_array=np.frombuffer(file_compress, dtype=np.uint8)
print(file_compress_afterCompress_array)




#用過濾器調整dictionary大小
my_filters_1G = [
    {"id": lzma.FILTER_LZMA1, "dict_size": 1000000000},
]

my_filters_4K = [
    {"id": lzma.FILTER_LZMA1, "dict_size": 4000},
]

my_filters_50K = [
    {"id": lzma.FILTER_LZMA1, "dict_size": 50000},
]
my_filters_100K = [
    {"id": lzma.FILTER_LZMA1, "dict_size": 100000},
]
my_filters_700K = [
    {"id": lzma.FILTER_LZMA1, "dict_size": 700000},
]
my_filters_10M = [
    {"id": lzma.FILTER_LZMA1, "dict_size": 10000000},
]
my_filters_500M = [
    {"id": lzma.FILTER_LZMA1, "dict_size": 500000000},
]
my_filters_1_5G = [
    {"id": lzma.FILTER_LZMA1, "dict_size": 1500000000},
]
#對已經壓縮過後的jpeg再做一次LZMA壓縮, 但是使用各種dictionary size(1GByte)

with lzma.open("afterJpegThenLzma_Dict1G.lzma", "w", format=lzma.FORMAT_ALONE, filters=my_filters_1G) as f:
    f.write(imgRaw_toString)
with lzma.open("afterJpegThenLzma_Dict1_5G.lzma", "w", format=lzma.FORMAT_ALONE, filters=my_filters_1_5G) as f:
    f.write(imgRaw_toString)



#後來把以下code改寫成function了

#file讀進來, 是一個一條直線的array, 所以要轉成512*512的array才會是圖片的二維格式
#imgRaw=np.fromfile("Lena.raw", dtype=np.uint8)
#imgRaw_afterReshape=imgRaw.reshape([512, 512])
#print(imgRaw_afterReshape)

#把圖片show出來, 是以graylevel show出來
#plt.imshow(imgRaw_afterReshape, cmap='gray')
#plt.show()


#原本紀錄在array的pixel改成用string存
#imgRaw_toString=imgRaw.tostring()
#print(imgRaw_toString)