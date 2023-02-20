s ="""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
#print(s.find("better"))
#Better
a=0
s2=s.find("better")
while s2!=-1:
    a+=1
    s=s.replace("better","   ",1)
    s2=s.find("better")
print (f"better:{a}")   


#Never

s2=s.find("never")
a=0 
while   s2!=-1:
    a+=1 
    s=s.replace("never","   ",1)
    s2=s.find("never") 
print (f"never:{a}")


#Is
s2=s.find("is")
a=0 
while   s2!=-1:
    a+=1 
    s=s.replace("is","   ",1)
    s2=s.find("is") 
print (f"is:{a}")

#Upper

s_Upper="""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""".upper()
print(s_Upper)

#replace i,&
s_rep="""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
s_replace=s_rep.replace("i","&")
print(s_replace)


# 3456
num=input()
s=str(num)
lis=[]
b=0;dob=1

for i in range(0, len(s)) :
  c=int(s[b])
  b+=1
  dob*=c
  lis.append(c)
  print(dob)  
print(lis)  
rev=lis.reverse()
print(lis)
lis.sort()
print(lis)




#3

a1=11
a2=54
print(f"a1:{a1},a2:{a2}")
a1+=a2
a2=a1-a2
a1-=a2    
print(f"a1:{a1},a2:{a2}")