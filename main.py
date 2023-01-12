from exif import Image
import shutil
import os
import pandas as pd
import timeit



class sortImage():
    def __init__(self):
        self.fromPath = r'C:\Users\matia\Desktop\backup\Mt\Fotos'
        #self.fromPath = r'C:\Users\matia\Desktop\backup\Mt\Fotos\Gopro rev'

    def creteFolders(self):
        years = [*range(2000,2022)]
        months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio' , 'Julio', 'Agosto', 'Septiembre', 'Noviembre', 'Diciembre']
        path = r'C:\Users\matia\Desktop\Fotos_Finales'
        
        for year in years: 
            newPath = path+'\\'+str(year)
            isExist = os.path.exists(newPath)
            print(isExist)
            if not isExist:
                os.makedirs(newPath)

                for month in months:
                    newPath2 = newPath +'\\'+month
                    isExist = os.path.exists(newPath2)
                    if not isExist:
                        os.makedirs(newPath2)
                    print(newPath2)

    def checkPath(self, df):
        df = df['path']
        df2 = pd.DataFrame()
        for index in df:
            
            for file in os.listdir(index):
                path = index+'\\'+file
                
                try:
                    with open(path, "rb") as img:
                        img_exif = Image(img)
                    variable = img_exif.datetime
                    year  = variable.split(sep=':')[0]
                    month  = variable.split(sep=':')[1]
                    #print(file,': ',img_exif.datetime)
                    #print(year)
                    #print(month)
                    new_row = {'path':path,'year': year, 'month': month}
                    df2 = df2.append(new_row, ignore_index=True)
                except:
                    pass
                    #print('Error')}
        return df2

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
                        self.getDirectories(df)
        return df
        
       


sort = sortImage()
sort.creteFolders()
# lst = [r'C:\Users\matia\Desktop\backup\Mt\Fotos']
# direct = pd.DataFrame({'path':lst, 'flag': 0})
# list_directories = sort.getDirectories(direct)
# df2 = sort.checkPath(list_directories)
# print(df2)
# column = df2["year"]
# max_value = column.max()
# min_value = column.min()
# print(min_value, max_value)












