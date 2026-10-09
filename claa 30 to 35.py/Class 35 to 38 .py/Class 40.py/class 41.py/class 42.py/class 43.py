names = [ "Nafisa","Saba","Laviba", "Allo"]
ages= [ 1,2,3,4]
print (list (zip(names,ages)))

a = [1,2,3,4,5]
b= [6,5,4,7,8]
for x, y in zip (a,b):
    print (x,y)

for x,y in zip (a,b) :
    print (x+y)