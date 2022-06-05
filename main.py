from exif import Image
import shutil
import os
import pandas as pd



class sortImage():
    def __init__(self):
        self.fromPath = r'C:\Users\matia\Desktop\backup\Mt\Fotos'
        #self.fromPath = r'C:\Users\matia\Desktop\backup\Mt\Fotos\Gopro rev'
    
    def checkPath(self):
        directory = os.fsencode(self.fromPath)
        for folder in next(os.walk(self.fromPath))[1]:
            directory = self.fromPath+'\\'+folder
            print("Ingresando a: ",directory)

            for file in os.listdir(directory):
                path = directory+'\\'+file
                print(path)
                try:
                    with open(path, "rb") as img:
                        img_exif = Image(img)
                    print(file,': ',img_exif.datetime)
                except:
                    pass
                    #print('Error')

        # print(var_japon.list_all())
                #shutil.move(fold+"\\"+filename,new+"\\"+filename)
        
    def getDirectories(self, df):
        for index, value in df.iterrows():
            path = value['path']
            if value['flag'] == 0:
                df.at[index, 'flag'] = 1
                for name in os.listdir(path):
                    if os.path.isdir(os.path.join(path, name)):
                        val = os.path.join(path, name)
                        df_length = len(df)
                        df.loc[df_length] = [val,0]
                        self.checkDir(df)
        return df
        
       


sort = sortImage()
lst = [r'C:\Users\matia\Desktop\backup\Mt\Fotos']
direct = pd.DataFrame({'path':lst, 'flag': 0})
list_directories = sort.getDirectories(direct)














