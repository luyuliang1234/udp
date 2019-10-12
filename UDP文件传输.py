from socket import *
import os
import time
s=socket(AF_INET,SOCK_DGRAM)
s.bind((gethostbyname(getfqdn(gethostname())),53))
print("本程序默认使用UDP53端口发送数据，便于通过防火墙")
print("本机IP是：",gethostbyname(getfqdn(gethostname())))
if(int(input("选择 1 发送\n选择 2 接收"))==1):
    ip=input("请输入要发送到计算机的IP地址：")
    port=53
    file=input("请输入文件名称：")
    try:
        f=open(file,mode="rb")
        size=os.path.getsize(file)
        s.sendto(str(size).encode('utf-8'),(ip,port))
        s.sendto(file.encode('utf-8'),(ip,port))
        e=f.read(1024)
        while (e!=b''):
            s.sendto(e,(ip,port))
            time.sleep(0.01)
            e=f.read(1024)
        print("已发送%d b数据"%size)
    except:
        print("发生错误，检查文件路径是否正确")
else:
    print("接收的文件将会放py相同的目录下")
    size=int(s.recv(1024))
    t=open(s.recv(1024).decode('utf-8'),"ab+")
    times=(size//1024)+1
    for i in range(0,times):
        print("写入次数",i)
        j=s.recv(1024)
        t.write(j)
    t.close()
    print("传输完成")
