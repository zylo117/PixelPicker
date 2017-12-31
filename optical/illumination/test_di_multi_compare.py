import datetime
import argparse
from optical.illumination.diagonal_illumination_distribution import *
import os

ap = argparse.ArgumentParser()

ap.add_argument("-ia", "--imageinputa", required=True, help="path to the raw image parent path")
ap.add_argument("-i", "--imageinputb", required=True, help="path to the raw image parent path")
ap.add_argument("-o", "--dataoutput", required=True, help="path to the output data")

args = vars(ap.parse_args())

time1 = datetime.datetime.now()

diag_list_a = []
diag_list_b = []
rootdir = args["imageinputa"]
list = os.listdir(rootdir)  # list out all file under this dir
for i in range(0, len(list)):
    path = rootdir + "\\" + list[i]
    if os.path.isfile(path):
        diag, back_diag = di(path)
        # addarray2csv(diag, args["dataoutput"])
        diag_list_a.append(diag)

draw_diag_illumination_list_compare(diag_list_a, diag_list_b)
time2 = datetime.datetime.now()
print(time2 - time1)
# draw_diag_illumination(di, back_di)