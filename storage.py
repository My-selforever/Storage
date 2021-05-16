import dropbox
import os


class Cloudstore:
    def __init__(self,access):
        self.access = access

    def upload(self,source,destination):
        dbox = dropbox.Dropbox(self.access)

        for root,dirs,files in os.walk("C:\Users\todbh\Desktop\Aadrika\Folders\Story"):
            print(files,'file')
            print(dirs,'dir')
            print(root,'root')
            
        #f = open(source,'rb')
           # dbox.files_upload(f.read(),destination)


def main():
    accessToken = 'D3ZREW_OW-UAAAAAAAAAAXtHZnVlWGu-yZE72v3kdYhrlxvmNwVwS915SIk9LRcz'
    tData = Cloudstore(accessToken)
    Ffrom = "C:\Users\todbh\Desktop\Aadrika\Folders\Story"
    FTo = "/Test/Storyfiles"
    tData.upload(Ffrom,FTo)

main()