import os
import shutil
import datetime
from urllib.request import urlretrieve
from PIL import Image, ImageFile
import pytz

import win32api
import win32gui
import win32con
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal,QObject
from PyQt5.QtGui import QTextCursor
import sys
from WindowUI import Ui_MainWindow

#
class BackGroundWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(BackGroundWin, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.buttonclick)
        self.pushButton_3.clicked.connect(self.printf)


    def printf(self):
        localtime,localtimeBeijing=getNow()
        self.textBrowser.append("当前UTC时间为：")
        self.textBrowser.append(str(localtime))  # 在指定的区域显示提示信息
        self.textBrowser.append("当前北京时间为：")
        self.textBrowser.append(str(localtimeBeijing))
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

    def printSuccess(self,info):
        self.textBrowser.append(info)


    def buttonclick(self):
        a=self.comboBox.currentIndex()
        b=self.comboBox_2.currentIndex()
        self.set_thread = SetThread(a,b)
        self.set_thread.start()
        self.set_thread.setBegin.connect(self.printSuccess)
        self.set_thread.setSuccess.connect(self.printSuccess)

#创建多进程类
class SetThread(QThread):
    setBegin=pyqtSignal(str)
    setSuccess=pyqtSignal(str)


    def __init__(self,a,b):
        super(SetThread, self).__init__()
        self.img=a
        self.update=b
    def run(self):
        if self.update == 1:
            Update_time = 600
        elif self.update == 2:
            Update_time = 1800
        elif self.update == 3:
            Update_time = 3600
        else:
            Update_time = 9999999

        Activate = True
        while Activate:
            self.setBegin.emit("开始设置背景......")
            set_bg(self.img)
            if Update_time != 9999999:
                self.setSuccess.emit("背景设置成功")
                time.sleep(Update_time)
            else:
                Activate = False
                self.setSuccess.emit("背景设置成功")

#设置背景
def set_bg(Select_quality):
    if Select_quality == 0:
        Img_quality = 1
    elif Select_quality == 1:
        Img_quality = 2
    elif Select_quality == 2:
        Img_quality = 4
    elif Select_quality == 3:
        Img_quality = 8
    else:
        Img_quality = 1
    setDir()
    get_pic(Img_quality)
    paste_pic(Img_quality)
    filepath = os.path.split(os.path.realpath(__file__))[0]
    image_name = 'background.png'
    image_path = filepath + '\\' + image_name
    setWallpaper(image_path)


#创建图片存储文件夹
def setDir():
    filepath='./earthbackground/'
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath)
        os.mkdir(filepath)


#获取当前时间
def getNow():
    UTC = pytz.timezone('UTC')
    localTime = datetime.datetime.now(UTC).strftime('%Y-%m-%d %H:%M:%S')
    Beijing=pytz.timezone('Asia/Shanghai')
    localTimeBeing = datetime.datetime.now(Beijing).strftime('%Y-%m-%d %H:%M:%S')
    return  localTime,localTimeBeing

#获取url中时间信息数据
def getDate():
    tz_London = pytz.timezone('UTC')
    localTime = datetime.datetime.now(tz_London)-datetime.timedelta(minutes=30)
    time1_str = datetime.datetime.strftime(localTime, '%Y/%m/%d')
    time1_str2 = datetime.datetime.strftime(localTime, '%H')
    time1_str3 = datetime.datetime.strftime(localTime, '%M')[0]+'0'
    datatime=time1_str+'/'+time1_str2+time1_str3+'00'
    #print(time1_str,time1_str2,time1_str3,datatime)
    return datatime

#下载图片
def get_pic(a):
    basic_url='https://himawari8-dl.nict.go.jp/himawari8/img/D531106/'
    data=getDate()
    for i in range(0,a):
        for j in range(0,a):
            Basic_url = F"{basic_url}{a}d/550/{data}_"
            #print(Basic_url)
            item=F'{i}_{j}.png'
            image_url=Basic_url+item
            urlretrieve(image_url, f'./earthbackground/bg{i}_{j}.png')
        # print(image_url)

#将下载图片拼接
def paste_pic(a):
    earth = Image.new('RGB', size=(a * 550, a * 550))
    imagelist=[]
    boxs=[]
    for i in range(0,a):
        for j in range(0,a):
            f= open(f'./earthbackground/bg{i}_{j}.png', "rb")
            fp=Image.open(f)
            imagelist.append(fp)
            box=(i * 550,j * 550, (i + 1) * 550, (j + 1) * 550)
            boxs.append(box)
    for index, bo in enumerate(boxs):  # 待黏贴的图片序号和位置
        # print(index, bo)
        earth.paste(imagelist[index], bo)
        earth.save('background.png')

#设置为壁纸
def setWallpaper(image_path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "6")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, 1 + 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    myWin=BackGroundWin()
    myWin.show()
    sys.exit(app.exec_())  # 在主线程中退出



