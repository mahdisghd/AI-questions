import math

class Node:
    list1=[]
    

    def __init__(self,father,node):
        self.father=father
        self.node=node
        

    def NodeAsDict(self):
        flag=False
        if len(Node.list1)==0:
            Node.list1.append(
                {"father": self.father,
                "node":self.node}
                )
      
        else:
            for i in Node.list1:
                if self.father is not None and (self.father == i["node"] or self.father == i["father"]):
                    flag=True
                    break
            if flag==True:
                Node.list1.append(
                {"father": self.father,
                "node":self.node}
                )
            else:
                return "Error"


        return Node.list1
    
    def depth(self):
        if self.father is None:
            return 1

        for i in Node.list1:
            if self.father==i["node"]:
                self=Node(i["father"],i["node"])
                return self.depth()+1
            
                
        
    
    
n= int(input("enter the number of overall nodes: "))
root=input("enter the root: ")
root=Node(None,root)
root.NodeAsDict()
for i in range(n-1):
    father=input("enter the father: ")
    root=input("enter the node: ")
    node=Node(father,root)
    print(node.NodeAsDict())

print(node.depth())









