import pickle
d ={
    1:[1,1,1,1,1],
    }
def downInfo(info):
    f = open("userInfo.txt","wb")
    pickle.dump(info,f)
    f.close()
downInfo(d)