area=[
    [(1,'clean'),(2,'dirty'),(3,'dirty'),(4,'dirty'),(5,'dirty')],
    [(6,'clean'),(7,'clean'), (8,'clean'), (9,'dirty'), (10,'clean')],
    [(11,'dirty'),(12,'dirty'),(13,'dirty'),(14,'clean'),(15,'dirty')],
    [(6,'clean'),(17,'clean'),(18,'dirty'),(19,'dirty'),(20,'clean')],
    [(21,'dirty'),(22,'dirty'),(23,'dirty'),(24,'clean'),(25,'clean')]
 
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
        if self.loc[1]==4 :
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
        if self.loc[0]==4 :
            return "Cannot go anymore down"
        else:
            self.loc[0]+=1
            return "Going to(down) :"+str(area[self.loc[0]][self.loc[1]])

    #added automation function to question 1
    def automation(self): 
        if self.loc[0]==0 or self.loc[0]==2 or self.loc[0]==4:
            for i in range(5):
                if self.right!="Cannot go anymore right":
                    print(self.suck())
                    print(self.right())
                    
            
        else:
            for i in range(4, -1, -1):
                if self.left!="Cannot go anymore left":
                    
                    print(self.suck())
                    print(self.left())
                    
        
        if self.down()!="Cannot go anymore down":
            self.automation()

          


vaccum1=vaccum([0,0])
vaccum1.automation()
print(area)


    