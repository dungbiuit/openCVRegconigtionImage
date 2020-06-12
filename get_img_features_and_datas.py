import cv2 as cv
import numpy as np
import glob

# Lay nhieu hinh tu 1 folder
day_path_jpg = glob.glob("sang/*.jpg")
day_path_png = glob.glob("sang/*.png")
night_path_jpg = glob.glob("toi/*.jpg")
night_path_png = glob.glob("toi/*.png")

# Gom cac hinh ban ngay vao 1 list
day_img = []
for img in day_path_jpg:
	n = cv.imread(img)
	day_img.append(n)
for img in day_path_png:
	n = cv.imread(img)
	day_img.append(n)

# Gom cac hinh ban dem vao 1 list
night_img = []
for img in night_path_jpg:
	n = cv.imread(img)
	night_img.append(n)
for img in night_path_png:
	n = cv.imread(img)
	night_img.append(n)

# List chua tat ca du lieu sau khi trich xuat
datas = []

# Vong lap trich xuat du lieu cua hinh ban ngay
for src in day_img:

	# Chuyen doi he mau tu RGB -> HSV
	if src.shape[2] == 3:
		hsv_img = cv.cvtColor(src, cv.COLOR_BGR2HSV)
	else:
		hsv_img = cv.cvtColor(src, cv.COLOR_BGRA2HSV)

	# Tinh trung binh cong va do lech chuan cua 3 kenh H,S,V
	mean, stddev = cv.meanStdDev(hsv_img)
	mean = mean.flatten()
	stddev = stddev.flatten()

	# Chuyen so lieu thanh 3 muc du lieu: low, medium, high
	mean_hue = ""
	stddev_hue = ""
	mean_sat = ""
	stddev_sat = ""
	mean_val = ""
	stddev_val = ""

	# Trung binh cong cua kenh H
	if mean[0] <= 45:
		mean_hue = "l"
	elif mean[0] <= 75:
		mean_hue = "m"
	else:
		mean_hue = "h"

	# Trung binh cong cua kenh S
	if mean[1] <= 65:
		mean_sat = "l"
	elif mean[1] <= 130:
		mean_sat = "m"
	else:
		mean_sat = "h"

	# Trung binh cong cua kenh V
	if mean[2] <= 100:
		mean_val = "l"
	elif mean[2] <= 180:
		mean_val = "m"
	else:
		mean_val = "h"

	# Do lech chuan cua kenh H
	if stddev[0] <= 20:
		stddev_hue = "l"
	elif stddev[0] <= 40:
		stddev_hue = "m"
	else:
		stddev_hue = "h"

	# Do lech chuan cua kenh S
	if stddev[1] <= 33:
		stddev_sat = "l"
	elif stddev[1] <= 67:
		stddev_sat = "m"
	else:
		stddev_sat = "h"

	# Do lech chuan cua kenh V
	if stddev[2] <= 33:
		stddev_val = "l"
	elif stddev[2] <= 67:
		stddev_val = "m"
	else:
		stddev_val = "h"

	# Luu du lieu vao list
	img_data = [mean_hue,stddev_hue,mean_sat,stddev_sat,mean_val,stddev_val,"s"]
	datas.append(img_data)

# Vong lap trich xuat du lieu cua hinh ban dem
for src in night_img:

	# Chuyen doi he mau tu RGB -> HSV
	if src.shape[2] == 3:
		hsv_img = cv.cvtColor(src, cv.COLOR_BGR2HSV)
	else:
		hsv_img = cv.cvtColor(src, cv.COLOR_BGRA2HSV)

	# Tinh trung binh cong va do lech chuan cua 3 kenh H,S,V
	mean, stddev = cv.meanStdDev(hsv_img)
	mean = mean.flatten()
	stddev = stddev.flatten()

	# Chuyen so lieu thanh 3 muc du lieu: low, medium, high
	mean_hue = ""
	stddev_hue = ""
	mean_sat = ""
	stddev_sat = ""
	mean_val = ""
	stddev_val = ""

	# Trung binh cong cua kenh H
	if mean[0] <= 45:
		mean_hue = "l"
	elif mean[0] <= 75:
		mean_hue = "m"
	else:
		mean_hue = "h"

	# Trung binh cong cua kenh S
	if mean[1] <= 65:
		mean_sat = "l"
	elif mean[1] <= 130:
		mean_sat = "m"
	else:
		mean_sat = "h"

	# Trung binh cong cua kenh V
	if mean[2] <= 100:
		mean_val = "l"
	elif mean[2] <= 180:
		mean_val = "m"
	else:
		mean_val = "h"

	# Do lech chuan cua kenh H
	if stddev[0] <= 20:
		stddev_hue = "l"
	elif stddev[0] <= 40:
		stddev_hue = "m"
	else:
		stddev_hue = "h"

	# Do lech chuan cua kenh S
	if stddev[1] <= 33:
		stddev_sat = "l"
	elif stddev[1] <= 67:
		stddev_sat = "m"
	else:
		stddev_sat = "h"

	# Do lech chuan cua kenh V
	if stddev[2] <= 33:
		stddev_val = "l"
	elif stddev[2] <= 67:
		stddev_val = "m"
	else:
		stddev_val = "h"

	# Luu du lieu vao list
	img_data = [mean_hue,stddev_hue,mean_sat,stddev_sat,mean_val,stddev_val,"t"]
	datas.append(img_data)

# Luu du lieu vao file datas.txt
with open("datas.txt", 'w') as f:
    for d in datas:
        f.write(str(d) + '\n')

