from abc import ABC, abstractmethod
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

vehicle1.displayAllFleetMembers()
  
  
class Vehicle(ABC):
    '''Defines the properties of vehicles'''
    
    # https://www.geeksforgeeks.org/inheritance-and-composition-in-python/
    @abstractmethod
    def __init__(self, gpsPosition, velocity, weight, velocityType, weightType):
        self.vehicleObject = Fleet()
        self.gpsPosition = [0,0]
        self.velocity = 0
        self.velocityType = "kph"
        self.weightType = "kg"
        self.weight = 0
        
class GroundVehicle:(ABC, Vehicle)
'''Doc string goes here'''
    
    # @abstractmethod
    # def __init__(self):