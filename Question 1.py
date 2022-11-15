area=[
    [(1,'clean'),(2,'dirty'),(3,'dirty')],
    [(4,'clean'),(5,'clean'), (6,'clean')],
    [(7,'dirty'),(8,'dirty'),(9,'dirty')]
 
    ]

def writeline(str):
    print(str)

class vaccum:
    def __init__(self,loc):
        self.loc=loc
    def noop(self):
        return "Do Nothing"
    def suck(self):
        if area[self.loc[0]][self.loc[1]][1]=="dirty":
            area[self.loc[0]][self.loc[1]]=tuple([area[self.loc[0]][self.loc[1]][0],"clean"])
            return "Cleaning this Square :"+ str(area[self.loc[0]][self.loc[1]])
        else:
            return "Already clean :"+ str(area[self.loc[0]][self.loc[1]])
        
    def right(self):
        if self.loc[1]==2 :
            return "Cannot go anymore right"
        else:
            self.loc[1]+=1
            return "Going to(right):"+str(area[self.loc[0]][self.loc[1]])
    def left(self):
        if self.loc[1]==0:
            return "Cannot go anymore left"
        else:
            self.loc[1]-=1
            return "Going to(left):"+str(area[self.loc[0]][self.loc[1]])
    def up(self):
        if self.loc[0]==0:
            return "Cannot up anymore up"
        else:
            self.loc[0]-=1
            return "Going to(up) :"+str(area[self.loc[0]][self.loc[1]])
    def down(self):
        if self.loc[0]==2 :
            return "Cannot go anymore down"
        else:
            self.loc[0]+=1
            return "Going to(down) :"+str(area[self.loc[0]][self.loc[1]])


vaccum1=vaccum([0,0])
print("Starting from [0,0]")

while(1):  
    
    a=input("Exit: (y,n)")
    if a=="y":
        print("exiting...")
        break
    elif a!="n" and a!="y":
        print("unrecognized character")
        break
        

    b=input("Enter action: (left, right, up, down, suck ,noop)")
    try:
        b=eval("vaccum1."+ b +"()")
        writeline(b)
    except:
        print("unsupported function")
   
    
    
   




