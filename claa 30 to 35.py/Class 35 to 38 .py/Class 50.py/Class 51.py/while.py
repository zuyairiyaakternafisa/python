digit = int (input ("Enter a number:"))
count = 0
while digit> 0:
    digit = digit //10
    count = count +1
print ("Total digit =" , count)