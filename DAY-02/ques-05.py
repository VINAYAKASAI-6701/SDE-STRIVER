def sort012(arr):
    n=len(arr)
    l=0
    m=0
    h=n-1
    while m<=h:
        if arr[m]==0:
            arr[l],arr[m]=arr[m],arr[l]
            l+=1
            m+=1
        elif arr[m]==1:
            m+=1
        else:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1
    return arr
    
arr=[2,0,1,2,2,0,1]
res=sort012(arr)
print(res)