#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Extravenza:
    n1=0
    list1=[]
    def function1(self):
        self.n1=int(input("ENter the no. students enrolled in extravenza club:"))
        for i in range(0,self.n1):
            s1=input("ENter the name of the Student:")
            (self.list1).append(s1)
        print("Extravenza club includes the following students",self.list1)
class Tez:
    n2=0
    list2=[]
    def function2(self):
        self.n2=int(input("ENter the no. students enrolled in tez club:"))
        for i in range(0,self.n2):
            s2=input("ENter the name of the Student:")
            (self.list2).append(s2)
        print("Tez club includes the following students",self.list2)


# In[2]:


class Test(Extravenza,Tez):
    set3=[]
    count=0
    total=0
    def function3(self):
        self.set1=set(self.list1)
        self.set2=set(self.list2)
        self.set3=set((self.set1).intersection(self.set2))
        print("Extravenza club includes the following students",self.set1)
        print("Tez club includes the following students",self.set2)
        print("Students enrolled in both the clubs are ",self.set3)
    def function4(self):
        for i in range (0,len(self.set3)):
            self.count=self.count+1
        print("NUmber of Students enrolled in both the clubs are :",self.count)
    def function5(self):
        self.total=len(self.set1)+len(self.set2)-self.count
        print("Number of students who are enrolled in at least one of the clubs are : ",self.total)
obj3=Test()
obj3.function1()
obj3.function2()
obj3.function3()
obj3.function4()
obj3.function5()



# In[ ]:




