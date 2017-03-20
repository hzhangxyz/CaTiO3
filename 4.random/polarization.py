def polarization(data):
    return [data[0][i]*4 +
            data[1][i]*2 -
            data[2][i]*2 -
            data[3][i]*2 -
            data[4][i]*2
            for i in range(3)]

def readfile(name):
    with open(name,"r") as f:
        d = f.read().split('\n')
    if d[8][0] == " ":
        data=map(lambda x:map(float,x.split()[:3]),d[8:13])
    else:
        data=map(lambda x:map(float,x.split()[:3]),d[9:14])
    return data

def main():
    for i in map(lambda x:x+"/CONTCAR","Ca Ti Ca-O Ti-O".split()):
        print i,polarization(readfile(i))

if __name__=="__main__":
    main()
