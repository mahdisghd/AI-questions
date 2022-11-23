from treelib import Node, Tree

tree=Tree()
root=input("enter the root of the tree:")
tree.create_node(root,root)
list1=[{
    "parent": None,
    "value": root
    }]
childno=input("enter the no. of children:")
for i in range(int(childno)):
    child=input("enter the value of node: ")
    try:
        parent=input("enter the parent of node:")
        tree.create_node(child,child,parent)
        list1.append(
            {
                "parent": parent,
                "value":child
                }
            )
    except:
        continue
    
tree.show()
print(list1)