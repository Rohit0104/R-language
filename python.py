#!/usr/bin/env python
# coding: utf-8

# In[32]:


import math


# In[33]:


math


# In[34]:


help(math)


# In[35]:


math.sqrt(2)


# In[36]:


math.pow(2,3)


# In[37]:


pip install bs4


# In[38]:


import bs4


# In[39]:


print("Rohit")


# In[40]:


x=int(input("pls enter 1st number "))
y=int(input("pls enter 2nd number "))
z=int(input("pls enter 3rd number "))
print("maximum number is")
print(max(x,y,z))


# In[41]:


x=input("pls enter name ")
print ("name : ", x)


# In[42]:


2|5


# In[43]:


x=5
x is 5


# In[44]:


a=[]


# In[45]:


a=['a','b','d']


# In[46]:


a


# In[47]:


a.append('Rohit')


# In[48]:


a


# In[49]:


a.remove('Rohit')


# In[50]:


a


# In[51]:


b=[12,15,18]


# In[52]:


a.extend(b)


# In[53]:


a


# In[54]:


a+b


# In[55]:


a


# In[56]:


b


# # forward index start from 0and revers index strat from -1

# In[57]:


a[1:3]  #[n:n-1]


# In[58]:


a[1:5]


# In[59]:


a[0:]


# In[60]:


a[-1:-6] # [n:n+1]


# In[61]:


a[-6:-1]


# In[62]:


c=a[2]+a[4]


# In[63]:


d=['a','s','d','f']


# In[64]:


d


# In[65]:


e=d[1]+d[2]


# In[66]:


e


# In[67]:


string = 'python'


# In[68]:


string[2:7]


# In[69]:


string[-4:]


# In[70]:


string[-1]+string[1]


# In[71]:


string.find('thon')


# In[72]:


string.replace('py','p')


# In[73]:


str = 'python is, a good, language'


# In[74]:


str.split(',')


# In[75]:


str.count('o')


# In[76]:


a.pop()


# In[77]:


a.insert(2,'b')


# In[78]:


a


# In[79]:


myDict = {1:'apple', 2:'ball'}


# In[80]:


myDict[2] #key value


# In[81]:


myDict.get(2) # key VALUE


# In[84]:


n = float (input("Number ? "))
if n>= 0:
    print("the absolute value of ",n,"is", n)
else:
    print("The absolute value of ",n, "is ",-n)
sumofnum=50+60
print(sumofnum)


# In[85]:


name = "Rohit"
print(name)
if name == "Rohit":
    print("the name entered is", name)
elif name == "john":
    print("the name entered is", name)
elif name == "tim":
    print("the name entered is", name)
else:
    print("not valid")


# In[86]:


name = "animals"
animalname = "4dog"
if name == "animals":
    if animalname == "2dog":
     print("valid animal")
     print("name entered is animal")
    else:
        print("i have given up")
        print("abc")
else:
    print("the name entered is not valid")


# In[87]:


a=0
while a<5:
    print(a, "First Value")
    a=a+1
    print(a,"second value")


# In[88]:


a=0
while a<5:
    print(a, "First Value")
    a=a+1
print(a,"second value")


# In[89]:


a=1
b=0
c=0
print("enter number to add sum")
print("enter 0 to quit")
while a!= 0 :
    print("current sum:", c)
    a = float(input("enter a number?:"))
    c=c+a
print("total sum = ", c)    


# In[90]:


for <variable> in sequence:
    statements


# In[91]:


for variable in range(0,10,2): # min max intervale
    print(variable)


# In[92]:


#solve the above proble
list_example = [0,1,2,3,4,5,6]

for index in range(0,len(list_example)):
    list_example[index] = list_example[index]+2


# In[93]:


list_example


# In[94]:


list_ex2 = ["apple","banana","citric", "dog","D"]
for item in list_ex2:
    if(item == "dog"):
        print("##hello##")
    else:
        print(item)


# In[95]:


summation =0
for num in range(9,10):
    summation = summation +num
print(summation) 


# In[96]:


ex = "notseperatedstring"
#if we want seperate char from above stine
list_ex = []
for char in ex:
    list_ex.append(char)
print(list_ex)
#using list comprehensive
print([char for char in ex])
list_ex


# In[97]:


def studentName(name,score):
    print("Name:", name, ",score:",score)
   


# In[98]:


studentName("Rohit",85)


# In[99]:


import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)


# In[100]:


from datetime import date
today = date.today()
print("Current Year:", today.year)


# In[101]:


today = date.today()
print(today)


# In[102]:


from datetime import date
timestamp = date.fromtimestamp(10123456789)
print("date:", timestamp)


# # extracting time

# In[103]:


a = time(11, 34, 56)

print("hour = ", a.hour)
print("minute = ", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)


# # datetime.timedelta

# In[106]:


from datetime import datetime, date
t1 = date(year = 2022, month = 7, day = 17)
t2 = date(year = 1654, month = 7, day = 17)
t3 = t1-t2
print("t3=", t3)


# In[107]:


print("type of t3 =", type(t3))


# # to get the days from timedelta

# In[108]:


t3.days


# In[109]:


t3.total_seconds()


# In[110]:


t5 = datetime(year = 2022, month = 7, day = 17, hour = 15, minute =30, second = 45)
t6 = datetime(year = 1654, month = 7, day = 17, hour = 10, minute =50, second = 55)
t7 = t5-t6
print("t7=", t7)


# In[113]:


from datetime import datetime

now = datetime.now()
print(now)


# In[114]:


datetime.strftime(now,'%Y')


# In[115]:


datetime.strftime(now,'%M')


# In[116]:


datetime.strftime(now,'%D')


# In[120]:


# Extracting from timestamp
from datetime import datetime

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)

d= date_time.strftime("%d, %b, %Y")
print("output3:", d)
      
d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)   

d =date_time.strftime("%I%p")
print("Output:", d)


# In[5]:


print("Current month:", today.month)


# In[6]:


print("current day:", today.day)


# In[7]:


from datetime import time
#time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
#time(hour, minute and second)
b= time(11, 34, 56)
print("b =", b)
#time(hour, minute, second)
c=time(hour= 11, minute = 34, second= 56)
print("c =", c)
#time(hour,minute,second,microsecond)
d= time(11, 34, 56, 234566)
print("d =", d)


#  # create file 

# In[ ]:


#w = create the file & write data
#r = read the content from the file
#w+ = create the file & write & read
#r+ = read & write 
#a = append


# In[5]:


fh = open('E:\\abc1234.xlx', 'w')
fh.writelines("This is line no.1")
fh.writelines("                 ")
fh.writelines("This is line no. 2")
fh.close()


# In[4]:


fh = open('E:\\abc1234.txt', r')
print(fh.read())
fh.close()


# In[6]:


import bs4 as bs
import uurllib.request
sauce = urllib.request.urlopen()
soup =bs.BeautifulSoup(sauce,title)
print(sauce)
print(soup)
print(soup.title)


# In[9]:


get_ipython().system('pip install bs4')


# In[7]:


# lambda function :- lambda argument : logic


# In[8]:


double = lambda x: x*2
print(double(10))


# In[13]:


def double(x):
    return x * 2
print(double(3))


# # filter

# In[12]:


my_list = [1,2,3,4,5,6,7,8,9]
my_newlist =list(filter(lambda x : (x%2 == 0), my_list))
print(my_newlist)


# In[14]:


#map
my_list = [1,2,3,4,5,6,7,8,9]
my_newlist =list(map(lambda x : (x%2 == 0), my_list))
print(my_newlist)


# In[15]:


my_list = [1,2,3,4,5,6,7,8,9]
my_newlist =list(map(lambda x : x*2, my_list))
print(my_newlist)


# In[20]:


import re

NameAge ='''
Rohit is 222 and Jhony is 45 daksh 25
Gabriel is 288 and joy is 85 Sunder 36'''
ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*', NameAge)

print(ages)
print(names)

ageDict = {}

x= 0

for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1
print(ageDict)    
    


# In[22]:


import re

phone = "423-456-987"
if re.search("\d{3}-\d{3}-\d{3}", phone):
             print("its a phone number")
else:
    print("its not a valid phone number")


# In[29]:


#\w [a-zA-Z0=9]



phone = "425-4556-9873"
if re.search("\d{3}-\d{3}-\d{3}", phone):
    print("its a phone number")
else:
    print("its not a valid phone number")


# In[32]:


import urllib.request
from re import findall
url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)
html = response.read()
htmlstr = html.decode()
#print(htmlstr)

pdata = findall("\(\d{3}\) \d{3}-\d{4}", htmlstr)
for item in pdata:
    print(item)


# # Numpy

# In[33]:


import numpy as np
a = np.array(([2,3,4], [5,6,7]))
print(a)
print(a.shape)


# In[34]:


a = np.array(([2,3,4,6], [5,6,7,9]))
print(a)
print(a.shape)


# In[39]:


#reshape
####a = np.array([([1,2])])
a = np.array(((1,2,3,4),(5,6,7,8)))
print(a)
print(a.shape)
a = a.reshape(4,2)
print(a)


# In[40]:


print(a)

a = a.repeat(4,0)  #axis 0
print(a)
print(a.shape)


# In[41]:


a = a.repeat(4,1)  #axis 1
print(a)
print(a.shape)


# In[42]:


a= ([0,2],[3,4],[5,6])
print(a[1:2])


# In[43]:


b= np.array([(1,2),(2,3)])
print(b)


# In[45]:


c= np.array([(1,2,3),(2,3,7),(3,8,0)])
print(c)


# In[48]:


#a = np.array([1,2,3])
#a = np.array([1,2,3],[4,5,6])

a = np.array([(1,2,3),(2,3,4)])
#print(a.ndim)
#print(a)
print(a.shape)
print("max value of array a is ", a.max())
print("minn value of array a is", a.min())
print("sum of array 'a' is", a.sum())


# In[50]:


print(a)


# In[49]:


#summing on rows & columne for row sum use axis 1 for col and sum use axis 0 for row
print(a.sum(axis = 0)) # col
print(a.sum(axis = 1)) # row


# In[51]:


import numpy as np
a= np.array([(1,2,3,4),(3,4,5,6),(6,7,8,9)])
b= np.array([(2,3,4,5),(6,7,8,9),(9,8,5,4)])
print(a)
print(b)
#sqroot
print(np.sqrt(a))
print(np.std(a))
#matrix arthmatic function
print(a+b)
#print(a)
#print(b)
#print(a-b)
#print(a*b)
#print(a/b)


# In[ ]:


numpy.


# In[53]:


# H stacking
print(a)
print(b)
print(np.shape(a))
print(np.shape(b))

print(np.hstack((a,b)))
print(np.hstack((a,b)).shape)


# In[54]:


# v stacking

print(a)
print(b)
print(np.shape(a))
print(np.shape(b))

print(np.vstack((a,b)))
print(np.vstack((a,b)).shape)


# In[56]:


import numpy as np
a = np.arange(10)
print(a)
s = slice(2,7,2)
print(a[s]


# In[57]:


import numpy as np
a = np.arange(10)
print(a)
s = slice(2,7,2)
print(a[s])
print(s)


# In[58]:


import numpy as np
a = np.arange(10)
print(a.shape)

print(a)

b = a[2:9:3]
print(b.shape)
print(b)


# In[ ]:




