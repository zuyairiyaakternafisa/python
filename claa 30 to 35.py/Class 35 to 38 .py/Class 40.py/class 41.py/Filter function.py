num = [ 1,2,3,15,4,5]
result = list (filter (lambda x : x%2 == 0, num))
print (result)

result = list ( filter (lambda x: x % 2 !=0,num))
print (result)

result = list (filter (lambda x : x >10, num))
print (result)

result = list(filter(lambda x : x>= 4,num ))
print (result)