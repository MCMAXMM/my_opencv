import cv2 as cv
import glob
#读取照片
path_list=glob.glob(r"D:\pythonrun\2018613pytorch\faces\*.jpg")
src=cv.imread(r"D:\pythonrun\2018613pytorch\faces\252418361_440b75751b.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#创建opencv自带的GUI窗口
cv.imshow("input image",src)#显示时名字要与窗口的名字一致
cv.waitKey(0)#等待多少毫秒后执行下一个命令，如果是0，就无限期等待，可以按任意键结束
cv.destroyAllWindows()
print("hello world")

#读取视频的一个函数
def get_video():
    capture=cv.VideoCapture(r"D:\BaiduNetdiskDownload\abc.flv")
    while(True):
        ret,frame=capture.read()#frame就是视频的帧
        frame=cv.flip(frame,1)
        cv.imshow("video",frame)
        c=cv.waitKey(50)
        if c ==27:
            break
get_video()读取video
