import cv2
import dropbox
import time
import random


starttime=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        starttime=time.time
        result=False
    return imageName
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

import dropbox

class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    def uploadfile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        with open(filefrom,'rb')as f:
            dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
def othermain(imageName):
    accesstoken="sl.A-pnntYWpiYchupAPf5hXoqnKKZ2gfkjBGtdmT_cq14AcXeVIkm-AVhrk_7g1N_kKem50ZK4dHI6s7c9OTWpJAgwPy2PJO5AYHyMIPTwfes9cS6v2SM_oKCYjfEtPPWmvvbagHgHOdw"
    transferData=TransferData(accesstoken)
    filefrom=imageName
    fileto="/a/"+imageName
    transferData.uploadfile(filefrom,fileto)
    print("file move was succesful")



def main():
    while(True):
        if((time.time()-starttime)>=30):
            name=takeSnapshot()
            othermain(name)
main()