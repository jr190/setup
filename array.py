A = [5,2,4,6,1,3]
print(A)
for j in range(1,len(A)):
    key = A[j]  # Set to 2
    i = j-1     # Set to 1
    while i>=0 and A[i]<key:    # is 5 > 2?
        A[i+1] = A[i]   #2 = 5
        i = i-1     #0 
    A[i+1] = key
print(A)


