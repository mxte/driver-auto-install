import os

for d in os.listdir("./"):
    try:
        for f in os.listdir(d):
            if f[-3:] == "inf":
                os.system(f'C:\\Windows\\System32\\PNPUTIL.exe -i -a {d}/{f}')
                
    except Exception as e:
        print(e)
        pass