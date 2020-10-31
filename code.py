import pandas as pd 
import numpy as np

def load_data():
    df= pd.read_excel(r'C:/Users/janh/Desktop/hackayuva/dataset.xlsx')
    data= df.drop(['S. No.'], axis=1)
    #print(data)
    return data


def career(sk1, sk2, sk3):
    data=load_data()
   
    y=data['career']
    r= len(data)
    c= len(data.columns)
    d= data.to_numpy()

    x=[sk1, sk2, sk3]
    f=0
    fl=[]

    #print(r,c)

    for i in range(r):
        f=0
        for j in range(1,c):
            for skill in x:
                if d[i][j]==skill:
                    f+=1
        fl.append(f)

    max = fl[0]
    pos=[0,]

    for i in range(1,r):
        if max<fl[i]:
            max= fl[i]
            pos[0]=i

    for i in range(1,r):
        if max==fl[i] and i!=pos[0]:
            pos.append(i)

    #ret=['career',]
    #in=0
    for i in pos:
        career= d[i][0]
        #ret[in++]= d[i][0]
        print(career)
        print("Remaining skills required to be acquired to pursue the career are:")
        for i in range(r):
            if career==y[i]:
                for j in range(1,c):
                    skill= d[i][j]
                    if skill not in x:
                        print(skill)

    print(fl)
    #return ret


def skillset(career):
    data=load_data()
    y=data['career']
    skills= []

    r= len(data)
    c= len(data.columns)
    d= data.to_numpy()

    for i in range(r):
        if career==y[i]:
            for j in range(1,c):
                skills.append(d[i][j])