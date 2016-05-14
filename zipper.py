__author__ = 'Jubin & Raghava'
import os
import zipfile
import shutil


def zipFun(src, dst):
    if not os.path.exists(os.getcwd() + "/output"):
        os.makedirs(os.getcwd() + "/output")
    zf = zipfile.ZipFile("temp.zip", "w")
    zf.write(src, os.path.basename(src))
    zf.close()
    with open('output/' + os.path.basename(dst), 'wb') as wfd:
        for f in [dst, 'temp.zip']:
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10)
        fseek = str(os.path.getsize(dst))
        fseek = (8 - len(fseek)) * "0" + fseek
        wfd.write(fseek)
    os.remove('temp.zip')


def unzipFun(src):
    if not os.path.exists(os.getcwd() + "/output"):
        os.makedirs(os.getcwd() + "/output")
    shutil.copy2(src, 'test.zip')
    temp = open('test.zip', "rb+")
    temp.seek(-8, 2)
    size = int(temp.read(8))
    temp.seek(-8, 2)
    temp.truncate()
    tempzip = open(os.getcwd() + "/temp2.zip", "wb")
    buffer_size = 1024 * 1024
    temp.close()
    temp = open('test.zip', "rb")
    temp.seek(size)
    while True:
        copy_buffer = temp.read(buffer_size)
        if not copy_buffer:
            break
        tempzip.write(copy_buffer)
    # shutil.copyfileobj(temp,tempzip,1024 * 1024 * 10)
    temp.close()
    tempzip.close()
    zip_ref = zipfile.ZipFile(os.getcwd() + "/temp2.zip", 'r')
    zip_ref.extractall(os.getcwd() + "/" + "output")
    zip_ref.close()
    os.remove('test.zip')
    os.remove('temp2.zip')
