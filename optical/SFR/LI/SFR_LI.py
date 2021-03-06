import datetime

from LI.crop_frame import cropFrame_LI
from LI.sfr_circle_ae import SFRCircle_AE
from read_bin import BinFile







if __name__ == "__main__":
    time1 = datetime.datetime.now()
    bin = BinFile("./1.bin")
    (width, height), bindata = bin.get_realdata(2)
    IDraw = bindata.reshape((height, width))

    IDcrop = cropFrame_LI(IDraw, "rggb", 10, "li", "oclb", False, False, True)
    output = SFRCircle_AE(IDcrop, 10)

    print(0)
