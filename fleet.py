class Fleet():
    vehicles = ["7E19H2", "N9460G32581A3", "BN4681"]
    
    def __init__(self, vtype, movspeed, travelmed, vehicleid):
        self.vehicletype = vtype
        self.movementspeed = movspeed
        self.travelmedium = travelmed
        self.uuid = vehicleid
            
            
    def displayAllFleetMembers(self):
        for i in self.vehicles:
            print(i)
            
    def displayVehicleType(self):
        print(self.vehicletype)
        
    def addVehicles(self, newVehicleId):
        self.vehicles.append(newVehicleId)
    
vehicle1 = Fleet("car", 120, "ground", Fleet.vehicles[0])
  
vehicle1.displayAllFleetMembers()

addVehicle = Fleet("hovercraft", 50, "ground/water", 0)

addVehicle.addVehicles(str(input("Enter vehicle identifier")))

vehicle1.displayAllFleetMembers()
  