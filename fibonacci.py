n = int(input("nhap so n: "))
def fibo(x):
    if 0<=x<2: return x #F0 = 0, F1=1 x=0 || x=1
    if x>=2:
        tmp = 0
        fi=[0,1] #khoi tao so Fi voi F0=0 F1=1
        for i in range (2,x+1):
            tmp = fi[0] +fi[1]
            fi=[fi[1], tmp]
        return fi[1]
print("Gia tri cua Fn la:",fibo(n))
