
def merge(LeftList,RightList,MainList):
    sortedlist=[]
    lengthLeft=int(len(MainList)/2)
    lengthRight=len(MainList)-lengthLeft
    l=0
    r=0
    i=0

    while l<lengthLeft and r<lengthRight:
        
        if LeftList[l] <= RightList[r]:
            sortedlist.append(LeftList[l])
            i+=1
            l+=1
            
        else:
            sortedlist.append(RightList[r])
            i+=1
            r+=1
    while l<lengthLeft:
         sortedlist.append(LeftList[l])
         i+=1
         l+=1
    while r<lengthRight:
         sortedlist.append(RightList[r])
         i+=1
         r+=1
    return sortedlist


def MergeSort(MainList):
    length=len(MainList)
    if length<=1:
        return MainList
    
    middle=int(length/2)

    LeftList = MergeSort(MainList[:middle])
    RightList = MergeSort(MainList[middle:])

    return merge(LeftList,RightList,MainList)
    

def BinarySearch(List1,x,min,max):
    mid=(min+max)//2
    if x==List1[mid]:
        return mid
    elif x>List1[mid]:
        min=min+1
        return(BinarySearch(List1, x, min, max))
    elif x<List1[mid]:
        min=min-1
        return(BinarySearch(List1, x, min, max))
    else:
        return False
            

list1=[14,5,7,2,1,56,8,10]
list1=MergeSort(list1)
print(list1)
print(BinarySearch(list1, 7, 0, 7))

