# minimal unit element for 
class room:
    def __init__(self, id, name):
        self.id = id                     # room id
        self.name = name                 # room name    
   
        self._roomType = 0              # 0==chitchen-basic / 1==chitchen-lusso / 2==bathroom-basic / 3==bathroom-lusso
        self._roomName = "cucina base" 
        # cucina -> fisso 800eu / 1000eu    
        # 

        self._squareMeter = 10                          # dimensioni bagno (std==10mq)
        self._standardPriceForTenSquareMeters = 800.0   
        self._standardPriceForSanitary = 250.0 
        self._standardPriceForH2O = 120.0 
        self._sizeTot=0                                 # costo parziale per dimensioni bagno        

        self._h2oPointsNum = 0           # numero punti acqua (120-150 eu cad)
        self._sanitaryNum = 0            # numero sanitari
        self._totMaterialCosts = 0.0     # sum of materials costs

        self._total=0.0                  # sum
   
    # square meters for bath and standard price for 10 square meters (default==800Euro)
    def bath(self, roomType, squareMeters, standardPriceForTenSquareMeters, h2oPointsNum, sanitaryNum):
        self._roomType=roomType
        if self._roomType==3:
            self._roomName = "bagno lusso" 
            k=1.5
        else:
            self._roomName = "bagno base" 
            k=1.0
        self._squareMeter=squareMeters
        self._standardPriceForTenSquareMeters=standardPriceForTenSquareMeters
        self._sizeTot=(standardPriceForTenSquareMeters/10*k)*squareMeters

        self._h2oPointsNum=h2oPointsNum
        self._sanitaryNum=sanitaryNum

        self._sizeTot+=k*self._standardPriceForH2O*self._h2oPointsNum 
        self._sizeTot+=k*self._sanitaryNum*self._standardPriceForSanitary 
        pass
 
    def chitchen(self, roomType):
        if self._roomType==roomType:
            self._roomName = "cucina base" 
            self._sizeTot=800.0
        else:
            self._roomName = "cucina lusso" 
            self._sizeTot=900.0
        pass


    def report(self):
#        self.total()

        print("room[" + str(self._roomType) + "]<" + self._roomName + ">--------------------------------------------------------------------------BEGIN")
        if(self._roomType==2 or self._roomType==3):
            print("Dimensione metri quadrati:<" + str(self._squareMeter) + ">  TOT:" + str(self._sizeTot) + " eu")

        if(self._roomType==0 or self._roomType==1):
            print("Preverntivo cucina:" + str(self._sizeTot) + " eu")

        print("room[" + str(self._roomType) + "]<" + self._roomName +
 ">--------------------------------------------------------------------------END")
        pass

