
class Item:
    def __init__(self, itemID, slot, name, source, location, obtained, bis):
        self.itemID = itemID
        self.slot = slot
        self.name = name
        self.source = source
        self.location = location
        self.obtained = obtained
        self.bis = bis

    def getID(self):
        return self.itemID

    def printItem(self):
        return(self.itemID +'\t'+ self.slot 
                +'\t'+ self.name 
                +'\t'+ self.source 
                +'\t'+ self.location 
                +'\t'+ self.obtained 
                +'\t'+ self.bis)

    def writeItem(self):
        return(self.itemID + ',' +
                self.name + ',' +
                self.source + ',' +
                self.location + ',' +
                self.bis)