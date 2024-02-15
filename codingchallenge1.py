u = input("enter text (end sentences and dont start with a space):") 
g = u.count(".") #used lines 2 to 7 for all the possible endings of a sentence
h = u.count("!")
i = u.count("?")
m = u.count("'")
n = u.count("\"")
q = u.count(",")
v = g+h+i# variable for number of sentences.
p = u.count(" ")
b=p+1#variable for words. adding plus one to compensate for one lesser space at the end of a sentence.
l = len(u)
a = l-p-v-m-q-n-n#subtracted everthing that would count as an extracharacter which aren't letters. leftover output are number of letters
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