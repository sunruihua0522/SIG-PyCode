class OberserverBase:
    def __init__(self,name):
        self.Name = name
    def Receive(self,data):
        print("%s接收到了%s的%s文章"%(self.Name, data.Author, data.Title))