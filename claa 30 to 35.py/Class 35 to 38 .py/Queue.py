from collections import deque
bank = deque ([ "Anis", "Karim","Bijoy"])
bank.popleft()
print (bank)

bank.popleft ()
bank.popleft ()

if not bank :
    print ("No person left")