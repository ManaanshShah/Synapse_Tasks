Kevin={"Halsey","Taylor Swift","Mitski","Joji","Shawn Mendes","Sabrina Carpenter","Nicky Minaj","Conan Grey","One Direction","Justin Bieber"}
print(type(Kevin))
Stuart={"Kendrick Lamar","Steve Lacy","Tyler the Creator","Joji","TheWeekend","Coldplay","Kaney West","Travis Scott","Frank Ocean","Brent Faiyaz"}
print(type(Stuart))
Bob={"Conan grey","Joji","Dove Cameron","Mitski","Arctic Monkeys","Steve Lacy","Kendrick Lamar","Isabel LaRosa","Shawn Mendes","Coldplay"}
print(type(Bob))
Edith={"Metallica","Billie Eilish","TheWeekend","Mitski","NF","Conan Grey","Kendrick Lamar","Nicky Minaj","Kanye West","Coldplay"}
print(type(Edith))
# Function to find length of individual playlists
def lenghts(Kevin,Stuart,Bob,Edith):
    leng=[len(Kevin),len(Stuart),len(Bob),len(Edith)]
    return leng
leng=lenghts(Kevin,Stuart,Bob,Edith)
print("Length of each DJ's playlist are:")
print(leng)
k,s,b,e=leng
import itertools
data=["Kevin","Stuart","Bob","Edith"]
comb=itertools.combinations(data,2)
print(list(comb))


# Function to find the Length of intersection playlists
def Inter(name1,name2):
    p=name1.intersection(name2)
    return len(p)
KIS=Inter(Kevin,Stuart)
print(KIS)
KIB=Inter(Kevin,Bob)
print(KIB)
KIE=Inter(Kevin,Edith)
print(KIE)
SIB=Inter(Stuart,Bob)
print(SIB)
SIE=Inter(Stuart,Edith)
print(SIE)
BIE=Inter(Bob,Edith)
print(BIE)

def Overlap(l1,l):
    percentage=(l1/l)*100
    return percentage

List1=[("Kevin&Stuart",Overlap(KIS,k)),("Kevin&Bob",Overlap(KIB,k)),("Kevin&Edith",Overlap(KIE,k)),("Stuart&Bob",Overlap(SIB,k)),("Stuart&Edith",Overlap(SIE,k)),("Bob&Edith",Overlap(BIE,k))]
print(List1)
print("\n")
SortList1=sorted(List1,key=lambda x:x[1])
SortList1.reverse()
print("Pair of DJ's with overlapping percentage: ")
print(SortList1)
Og30=[]
for item in SortList1:
    if item[1]>=30:
        Og30.append(item)
print("The following are the possible DJ pairs with their overlap percentage: ")
print(Og30)


# PS D:\Users\manaa\OneDrive\Desktop\Python> python -u "d:\Users\manaa\OneDrive\Desktop\Python\Task1.1.py"
# <class 'set'>
# <class 'set'>
# <class 'set'>
# <class 'set'>
# Length of each DJ's playlist are:
# [10, 10, 10, 10]
# [('Kevin', 'Stuart'), ('Kevin', 'Bob'), ('Kevin', 'Edith'), ('Stuart', 'Bob'), ('Stuart', 'Edith'), ('Bob', 'Edith')]
# 1
# 3
# 3
# 4
# 3
# 3
# [('Kevin&Stuart', 10.0), ('Kevin&Bob', 30.0), ('Kevin&Edith', 30.0), ('Stuart&Bob', 40.0), ('Stuart&Edith', 30.0), ('Bob&Edith', 30.0)]


# Pair of DJ's with overlapping percentage:

# [('Stuart&Bob', 40.0), ('Bob&Edith', 30.0), ('Stuart&Edith', 30.0), ('Kevin&Edith', 30.0), ('Kevin&Bob', 30.0), ('Kevin&Stuart', 10.0)]

# The following are the possible DJ pairs with their overlap percentage:

# [('Stuart&Bob', 40.0), ('Bob&Edith', 30.0), ('Stuart&Edith', 30.0), ('Kevin&Edith', 30.0), ('Kevin&Bob', 30.0)]