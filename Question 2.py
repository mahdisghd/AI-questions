class connector:
    def __init__(self,word,list1):
        self.word=word
        self.list1=list1

    def add(self):
        if self.word == "question":
            a=input("enter the word:")
            return bool(self.list1.count(a))
        self.list1.append(self.word)
        return self.list1

list1=[]
while 1: 
    a=input("enter a word or string: ")
    connect=connector(a,list1) 
    print(connect.add())