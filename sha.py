import hashlib
import os
import pandas as pd
from multiprocessing import Pool, cpu_count
import numpy as np

def main():
    PATH = "C:\\Users\\matia\\Desktop\\M\\Fotos\\"
    df = getFileList(PATH)
    dfHash = parallelize_df(df, getHash, 16)
    dfDup, dfNotDup = checkDuplicated(dfHash)

    df = parallelize_df(dfDup, delteDuplicatedFiles, 16)

    dfDup.to_excel('deleted_images.xlsx')
    dfNotDup.to_excel('notDuplicated.xlsx')

    #dfHash.to_parquet("data.parquet")

def checkDuplicated(df):
    print("3. Getting duplicated files")

    df['dup'] = df.hash.duplicated()
    df = df.sort_values(by="hash").reset_index(drop = True)

    dfDup = df[ df['dup'] == True]
    dfNotDup = df[ df['dup'] == False]

    return dfDup, dfNotDup


def delteDuplicatedFiles(df):
    print("4. Deleting duplicated files.")
    
    for index, row in df.iterrows():
        fileName = row['ruta']
        os.remove(fileName)

    return df


def parallelize_df(df, func, n_cores):
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df


def getFileList(PATH):
    print("1. Generating list of files.")

    df = pd.DataFrame()
    for path, currentDirectory, files in os.walk(PATH):
        for file in files:
            df = pd.concat([df,pd.DataFrame([os.path.join(path, file)])])
    df = df.reset_index(drop = True)
    df = df.rename(columns={0: "ruta"})
    
    print(f"Total Files: {len(df.index)}")
    return df


def getHash(df):
    print("2. Calculating Hash")

    df['hash'] = df["ruta"].apply(lambda x: hashlib.md5(open(x,'rb').read()).hexdigest())
    return df



if __name__ ==  '__main__': 
    main()
