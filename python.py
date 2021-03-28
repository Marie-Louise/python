a=[[1,2,3],[4,5,6],[7,8,9]]
b=[numbers for sublist in a for numbers in sublist]
print(b)
c=[numbers*11 for numbers in b]
print(c)
