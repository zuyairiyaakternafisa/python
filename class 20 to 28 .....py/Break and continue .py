# ###  Break cstatement in python 
# i = 1 
# while i <= 100:
#     print (i)
#     i= i+1
#     if i == 88:
#         break
# print ("Hellow")

# ## Continue statement in python

# i=1
# while i <=100:
#     if i ==20:
#        continue

#     print (i)
#     i=(i+1)
#     print ("Hi")



for shop in range(1, 6):
    print("Shop", shop)

    if shop == 3:
        print("Product found!")
        continue