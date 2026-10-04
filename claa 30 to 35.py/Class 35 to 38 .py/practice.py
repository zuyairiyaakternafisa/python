# 9. 🛜 Wi-Fi Data Limit
# Monthly data limit = 100 GB.

# প্রতিদিন usage input নাও।

# যদি remaining:

# 50 GB → "Safe"

# 20–50 GB → "Warning"
# <20 GB → "Critica 
\


data = int(input("Enter a number :"))

# data = int(input("Enter a number: "))
if  data >50 :
    print ("safe your data")

elif data >= 20 or data <= 50:
    print("Warning")
else :
    print ("critical your data")