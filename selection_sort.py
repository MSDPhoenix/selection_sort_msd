# WITH EACH STEP PRINTED

x=[5,1,4,2,8,9,8,7,6,4,5,3,2,1]
y=[5,1,4,2,8]

def selectionSort(arr):
    print("starting     ",arr)
    for j in range(len(arr)):
        min=arr[j]
        for i in range(1+j,len(arr)):
            print("comparing index",j,"with index",i,arr)
            if min>arr[i]:
                min=arr[i]
                arr[j],arr[i]=arr[i],arr[j]
                print(arr[j],"swapped with",arr[i])
    print("finished     ", arr)

selectionSort(y)



# WITHOUT ONLY IMPORTANT STEPS PRINTED

x=[5,1,4,2,8,9,8,7,6,4,5,3,2,1]
y=[5,1,4,2,8]

def selectionSort(arr):
    print("starting     ",arr)
    for j in range(len(arr)):
        min=arr[j]
        for i in range(1+j,len(arr)):
            if min>arr[i]:
                print("comparing index",j,"with index",i,arr)
                min=arr[i]
                arr[j],arr[i]=arr[i],arr[j]
                print(arr[j],"swapped with",arr[i])
    print("finished     ", arr)

selectionSort(y)

# MINIMAL

x=[5,1,4,2,8,9,8,7,6,4,5,3,2,1]
y=[5,1,4,2,8]

def selectionSort(arr):
    print("starting     ",arr)
    for j in range(len(arr)):
        min=arr[j]
        for i in range(1+j,len(arr)):
            if min>arr[i]:
                min=arr[i]
                arr[j],arr[i]=arr[i],arr[j]
    print("finished     ", arr)

selectionSort(x)





