def selection_sort(f1):
    n=len(f1)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if f1[min_index]>f1[j]:
                min_index=j
                
        f1[i],f1[min_index]=f1[min_index],f1[i]
    return f1

f1=[5,416,54,21,6135,15,741]

print("Before Sorting:")
for num in f1:
    print(num, end=" ")
print("\n")

print("After Sorting:")
selection_sort(f1)
for num in f1:
    print(num, end=" ")