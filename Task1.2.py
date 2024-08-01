gadgets=[("Explosive batarangs",3,True),("Batarangs",5,True),("Smoke Pallets",0,False),("Tear Gas Grenades",2,True),("Night vision goggles",1,True),("Batclaws",0,False),("Grapple Gun",3,True),("Batsignal",0,False),("Utility Belt",1,True),("Batmobile Tiers",4,True)]

gadgets_sort1=sorted(gadgets,key=lambda x:x[0])
gadgets_sort2=sorted(gadgets_sort1,key=lambda x:x[1],reverse=True)
gadgets_sort3=sorted(gadgets_sort2,key=lambda x:x[2],reverse=True)
print("Thus the right order is as follows:")
print(gadgets_sort3)

# Thus the right order is as follows:
# [('Batarangs', 5, True), ('Batmobile Tiers', 4, True), ('Explosive batarangs', 3, True), ('Grapple Gun', 3, True), ('Tear Gas Grenades', 2, True), ('Night vision goggles', 1, True), ('Utility Belt', 1, True), ('Batclaws', 0, False), ('Batsignal', 0, False), ('Smoke Pallets', 0, False)]