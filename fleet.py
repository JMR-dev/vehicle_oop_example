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
    
# vehicle1 = Fleet("car", 120, "ground", Fleet.vehicles[0])
  
# vehicle1.displayAllFleetMembers()

# addVehicle = Fleet("hovercraft", 50, "ground/water", 0)

# vehicle1.displayAllFleetMembers()
  
  

        
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
        
class GroundVehicleInterface(ABC):
    '''Resource on Python interfaces. This is duck typed. https://realpython.com/python-interface/'''
    @abstractmethod
    def travel(self):
        Vehicle.velocity = self.moveGroundVehicle
        
class GroundVehicle(Vehicle, GroundVehicleInterface):

    
    @abstractmethod
    def __init__(self, volume):
        # default value set to true. Many ground vehicles will have trailers or train cars. Modified as needed
        self.isModular = True
        self.moveGroundVehicle = float(input())
    
class Train(GroundVehicle):
    def __init__(self, noOfCarsAttached, locomotiveCount):
        self.noOfCarsAttached = 1
        self.locomotiveCount = 1
        
    def displayCarCount(self):
        print(self.noOfCarsAttached)
        
    def travel(self):
        print("Speed 60mph, Direction E")
        
Train1 = Train(20, 2)

Train1.displayCarCount()