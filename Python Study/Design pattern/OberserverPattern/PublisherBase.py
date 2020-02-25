from DataModel import DataModel
class PublisherBase:
    def __init__(self,name):
        self.Name = name
        self.ClientList = []
    def AddClient(self,client):
        if(not client in self.ClientList):
            self.ClientList.append(client)
    def RemoveClient(self,client):
        if(client in self.ClientList):
            self.ClientList.remove(client)

    def Publish(self,title):
        for c in self.ClientList:
            c.Receive(DataModel(self.Name,title))