from matplotlib import pyplot as plt
import datetime
import math
#这个函数是计算那一堆值的
def func (x,y):
    x1=0.0;
    y1=0.0
    s1=0.0
    s2=0.0
    s3=0.0
    for i in x:
        x1+=i
        s1+=i*i
    for i in y:
        y1+=i;
        s2+=i*i
    x1=x1/len(x)
    y1=y1/len(y)
    n=len(x)
    s4=0.0
    s5=0.0
    for i in range(n):
        s3+=x[i]*y[i]
        s4+=(y[i]-y1)/y1
        s5+=math.fabs(y[i]-y1)
    r=(s3-n*x1*y1)/(math.sqrt(s1-n*x1*x1)*math.sqrt(s2-n*y1*y1))
    va=s5/n
    vr=va/y1
    v=s4/n
    return r,va,vr,v
y=[]
done=[]
name={}
cnt=0
ids=[]
for i in range(5):
    y.append([])
    done.append([])
    for j in range(1961,2011):
        y[i].append(0)
        done[i].append(0)
file=open('data.txt','r')
#略过首行数据，首行数据不是我们要的
file.readline()
#对于文件中的每一行进行处理：
for line in file:
    #规范数据格式
    line=line.replace('r','')
    line=line.replace('\n','')
    line=line.replace('\'','')
    line=line.replace('b','')
    #把一行按照空格切分成一个列表
    data=line.split(' ')
    id = eval(data[0])#eval（）是把字符串转化为数值
    year = eval(data[1])-1961#年份的最小值是1961，所以减去1961
    month = eval(data[2])
    day=eval(data[3])
    lowestTemp = eval(data[9])/10#气温的单位是0.1摄氏度所以要除以10得到真正气温
    #st代表上半年的终霜日，ed代表下半年的初霜日ed-st就能得到无霜日天数,flag代表找没找到ed
    #在每年的1月1日对其进行初始化
    if month==1 and day==1:
        st = datetime.date(1961 + year, 1, 1)
        ed = datetime.date(1961 + year, 12, 31)
        flag=0
    #这是将序列号映射到0,1,2,3,4,5，name[id]表示映射后的数字
    if id not in name.keys():#如果该id从未出现过，就给它分配一个映射值
        name[id]=cnt
        ids.append(id)
        cnt+=1
    #寻找st
    if lowestTemp<=2 and month<=6:
        st=datetime.date(1961+year,month,day)
    #寻找ed,一旦发现了一个有霜日，则该日期就是ed
    if lowestTemp<=2 and month>6 and flag==0:
        ed=datetime.date(1961+year,month,day)
        flag=1
    #如果到了一年里的最后一天，就把找到的st和ed之间的天数算出来填入作为该年的无霜日
    if month==12 and day==31:
        y[name[id]][year]=(ed-st).days
out=open('output.txt','w')
print("序列号","线性相关系数：","绝对变率:","相对变率:","降水距平百分比:")
#输出和画图处理：
for i in range(0,5):
    yy=[]
    st=-1
    ed=-1
    #这是为了找到无霜日不为0的一段年份，因为在初始化的时候是初始化了总的最大年份和最小年份的
    #差值，所以有的观测站的年份是不符合的，初始化的时候都为0
    for j in range(1961,2011):
        if y[i][j-1961]!=0:
            ed=j
            if st==-1:
                st=j
    #画图操作，画x与y的关系图
    x=range(st,ed+1)
    plt.plot(x,y[i][st-1961:ed-1961+1],'-')
    #输出到文件
    for j in range(st,ed+1):
        content=[]
        content.append(ids[i])
        content.append(j)
        content.append(y[i][j-1961])
        out.write(content[0].__str__()+" "+j.__str__()+" "+content[2].__str__()+"\n")
    r,va,vr,v=func(x,y[i][st-1961:ed-1961+1])
    print(ids[i],r,va,vr,v)
plt.show()
