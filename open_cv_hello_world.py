import cv2 as cv
import glob
#读取照片
path_list=glob.glob(r"D:\pythonrun\2018613pytorch\faces\*.jpg")
src=cv.imread(r"D:\pythonrun\2018613pytorch\faces\252418361_440b75751b.jpg")
print(src.shape)#形状
print(src.size)#多少像素
print(src.dtype)#数据类型，基本上与numpy相同
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#创建opencv自带的GUI窗口
cv.imshow("input image",src)#显示时名字要与窗口的名字一致
cv.waitKey(0)#等待多少毫秒后执行下一个命令，如果是0，就无限期等待，可以按任意键结束
cv.destroyAllWindows()
print("hello world")

#读取视频的一个函数
def get_video():
    capture=cv.VideoCapture(r"D:\BaiduNetdiskDownload\abc.flv")#里面设置为0，1,2分别代表你的摄像头
    while(True):
        ret,frame=capture.read()#frame就是视频的帧,ret为Boolean值表示是否有返回值（是否读到东西）
        frame=cv.flip(frame,1)#镜像水平翻转帧
        cv.imshow("video",frame)
        c=cv.waitKey(50)
        if c ==27:
            break
get_video()读取video

#保存图片
src=cv.imread(r"D:\pythonrun\2018613pytorch\faces\252418361_440b75751b.jpg")
src=cv.cvtColor(src,cv.COLOR_RGB2GRAY)#改成灰度图像
cv.imwrite("./hello.jpg",src)

#改变色彩空间
# gray=cv.cvtColor(src,cv.COLOR_RGB2GRAY)
# cv.imshow("gray",gray)
# print(gray.shape)
# hsv=cv.cvtColor(src,cv.COLOR_RGB2HSV)
# print(hsv.shape)
# cv.imshow("hsv",hsv)#h:0-180,s:0-255,v:0-255
# yuv=cv.cvtColor(src,cv.COLOR_RGB2YUV)
# cv.imshow("yuv",yuv)
# print(yuv.shape)
# cv.waitKey(0)
# cv.destroyAllWindows()

#图像色彩的捕捉，也可以用于video
# hsv=cv.cvtColor(src,cv.COLOR_RGB2HSV)
# lower_hsv=np.array([37,43,46])#捕捉图像中的绿色
# upper_hsv=np.array([77,255,255])
# mask=cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
# #使用inRange捕捉绿色，并将图像转换成二值图像
# cv.imshow("hsv",mask)
# cv.imshow("rgb",src)
# c=cv.waitKey(0)
# cv.destroyAllWindows()

#图像的分离与合并
#r,g,b=cv.split(src)
# cv.imshow("r",r)
# cv.imshow("g",g)
# cv.imshow("b",b)
# cv.imshow("merge",cv.merge([r,b,g]))
# cv.waitKey(0)
# cv.destroyAllWindows()

#图像相关的运算(算数运算和几何运算)
# cv.subtract()
# cv.add()
# cv.multiply()
# cv.divide()
#各个通道的均值和方差
mean=cv.mean(src)#返回三个通道的均值
mean,std=cv.meanStdDev(src)#返回两个array分别是三个通道的均值和方差
#逻辑运算
cv.bitwise_not()
cv.bitwise_and()
cv.bitwise_or()
cv.bitwise_xor()#亦或

