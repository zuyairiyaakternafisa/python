matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
total = 0
for row in matrix :
  for col in row :
      if col % 2 == 0:
       print (col)