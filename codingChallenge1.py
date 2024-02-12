u = input("enter text:") 
g = u.count(".")
h = u.count("!")
i = u.count("?")
m = u.count("'")
n = u.count("\"")
q = u.count(",")
v = g+h+i
p = u.count(" ")
b=p+1
l = len(u)
a = l-p-v-m-q
def grade_level(L,S): #first function for the grade
    index= 0.0588*L-0.296*S-15.8
    return index

def average_L(q,r): # second function for average letters
    al=q/r*100 
    return al
al=average_L(a,b)

def average_s(s,w):#third function for average sentences
    ak=s/w*100 
    return ak
ak=average_s(v,b)

i=grade_level(al,ak)
o=int(i)
r=abs(o)
print("Grade is:",r)