import csv
import glob
import numpy as np
from cv2 import cv2

DAY_IMG = []

NIGHT_IMG = []

# List chua tat ca du lieu sau khi trich xuat
# IMPORTANT
DATAS = []
# Lay nhieu hinh tu 1 folder
DAY_PATH_JPG = glob.glob("sang/*.jpg")
DAY_PATH_PNG = glob.glob("sang/*.png")
NIGHT_PATH_JPG = glob.glob("toi/*.jpg")
NIGHT_PATH_PNG = glob.glob("toi/*.png")

HEADER_TITLE = ['','mean_hue', 'stddev_hue', 'mean_sat', 'stddev_sat', 'mean_val', 'stddev_val', 'classification']
# GOM CAC HINH ban ngay vao 1 list
def addImageListAfterAddImage(imagePath, ListToAdd):
    for img in imagePath:
        n = cv2.imread(img)
        ListToAdd.append(n)

def appendDayImageToDAY_IMG():
    addImageListAfterAddImage(DAY_PATH_JPG, DAY_IMG)
    addImageListAfterAddImage(DAY_PATH_PNG, DAY_IMG)

def appendNightImageToNIGHT_IMG():
    addImageListAfterAddImage(NIGHT_PATH_JPG, NIGHT_IMG)
    addImageListAfterAddImage(NIGHT_PATH_PNG, NIGHT_IMG)

def returnHSV_ImageFromNormalImage(src):
    if src.shape[2] == 3:
        hsv_img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    else:
        hsv_img = cv2.cvtColor(src, cv2.COLOR_BGRA2HSV)
    return hsv_img

def returnMeanAndStddevFromHSV_Image(hsv_img):
    mean, stddev = cv2.meanStdDev(hsv_img)
    mean = mean.flatten()
    stddev = stddev.flatten()
    return mean, stddev

def returnMeanHueFromMean(mean):
    if mean <= 45:
        mean_hue = "l_avg"
    elif mean <= 75:
        mean_hue = "m_avg"
    else:
        mean_hue = "h_avg"
    return mean_hue

def returnMeanSatFromMean(mean):
    if mean <= 65:
        mean_sat = "l_avg"
    elif mean <= 130:
        mean_sat = "m_avg"
    else:
        mean_sat = "h_avg"
    return mean_sat

def returnMeanValFromMean(mean):
    if mean <= 100:
        mean_val = "l_avg"
    elif mean <= 180:
        mean_val = "m_avg"
    else:
        mean_val = "h_avg"
    return mean_val

def returnStdDevHueFromStdDev(stddev):
    if stddev <= 20:
        stddev_hue = "l_dev"
    elif stddev <= 40:
        stddev_hue = "m_dev"
    else:
        stddev_hue = "h_dev"
    return stddev_hue
                                                    
def returnStdDevSatFromStdDev(stddev):
    if stddev <= 33:
        stddev_sat = "l_dev"
    elif stddev <= 67:
        stddev_sat = "m_dev"
    else:
        stddev_sat = "h_dev"
    return stddev_sat

def returnStdDevValFromStdDev(stddev):
    if stddev <= 33:
        stddev_val = "l_dev"
    elif stddev <= 67:
        stddev_val = "m_dev"
    else:
        stddev_val = "h_dev"
    return stddev_val

def returnCalculateValueListOfEachImageFromImageList(imageList):
    for src in imageList:
        # Chuyen doi he mau tu RGB -> HSV
        hsv_img = returnHSV_ImageFromNormalImage(src)
        # Tinh trung binh cong va do lech chuan cua 3 kenh H,S,V
        mean, stddev = returnMeanAndStddevFromHSV_Image(hsv_img)
        # Chuyen so lieu thanh 3 muc du lieu: low, medium, high
        # Trung binh cong cua kenh H
        mean_hue = returnMeanHueFromMean(mean[0])
        # Do lech chuan cua kenh H
        stddev_hue = returnStdDevHueFromStdDev(stddev[0]) 
        # Trung binh cong cua kenh S
        mean_sat = returnMeanSatFromMean(mean[1]) 
        # Do lech chuan cua kenh S
        stddev_sat = returnStdDevSatFromStdDev(stddev[1]) 
        # Trung binh cong cua kenh V
        mean_val = returnMeanValFromMean(mean[2]) 
        # Do lech chuan cua kenh V
        stddev_val = returnStdDevValFromStdDev(stddev[2]) 
        # Luu du lieu vao list
        valueList = [mean_hue, stddev_hue, mean_sat, stddev_sat, mean_val, stddev_val, "s"]
        return valueList
def introduceSentences():
    print("\t\t\tĐỒ ÁN CUỐI KÌ KHAI PHÁ DỮ LIỆU ĐA PHƯƠNG TIỆN VÀ THỰC HÀNH CHUYÊN SÂU")
    print("\t\tSINH VIÊN: NGUYỄN TRÍ DŨNG - N16DCPT005 VÀ THẠCH HẢI ĐĂNG - N16DCPT007")

def functionalSentences():
    print("1.Rút trích dữ liệu và dữ liệu ảnh sáng")
    print("2.Rút trích dữ liệu và dữ liệu ảnh tối")
    print("3.Rút trích dữ liệu và dữ liệu ảnh sáng và tối")

def showMenu():
    introduceSentences()
    functionalSentences()

def returnSelection():
    selection = int(input("Mời bạn nhập lựa chọn: "))
    while selection < 1 or selection > 3:
        functionalSentences()
        selection = int(input("Sai lựa chọn mời bạn nhập lại: "))
    return selection

def returnDataListBySelection(selection):
    if selection == 1:
        appendDayImageToDAY_IMG()
        dataList = returnCalculateValueListOfEachImageFromImageList(DAY_IMG)
    elif selection == 2:
        appendNightImageToNIGHT_IMG()
        dataList = returnCalculateValueListOfEachImageFromImageList(NIGHT_IMG)
    else:
        appendDayImageToDAY_IMG()
        dataList = returnCalculateValueListOfEachImageFromImageList(DAY_IMG)
        appendNightImageToNIGHT_IMG()
        dataList += returnCalculateValueListOfEachImageFromImageList(NIGHT_IMG)
    return dataList

# Luu du lieu vao file datas.txt
def writeDataToCSVFile():
    with open("datas.csv", 'w') as f:
        headerRow = csv.writer(f)
        headerRow.writerow(HEADER_TITLE)
        for d in DATAS:
            f.write(str(d) + '\n')

def executeProgram():
    showMenu()
    selection = returnSelection()
    dataList = returnDataListBySelection(selection)
    DATAS.append(dataList)
    writeDataToCSVFile()

executeProgram()
