from abc import ABC, abstractmethod
# ABC is imported from the standard library since Python does not natively support abstract methods and classes.
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
    def __init__(self, _gpsPosition, _velocity, _weight, _velocityType, _weightType, _status):
        self.vehicleObject = Fleet()
        self.gpsPosition = _gpsPosition
        self.velocity = _velocity
        self.velocityType = _weight
        self.weightType = _velocityType
        self.weight = _weightType
        self.status = _status
        
class GroundVehicleInterface(ABC):
    '''Resource on Python interfaces. This is duck typed. https://realpython.com/python-interface/ Interfaces make a contract that a method must be implemented if an interface is inherited and allows differing implementations of the same method.'''
    @abstractmethod
    def travel(self):
        Vehicle.velocity = self.moveGroundVehicle
        print("Traveling")
        
class GroundVehicle(Vehicle, GroundVehicleInterface):

    @abstractmethod
    def __init__(self, volume):
        # default value set to true. Many ground vehicles will have trailers or train cars. Modified as needed
        self.isModular = True
        self.moveGroundVehicle = float(input())
        
class RoadVehicle(GroundVehicle):
    
    @abstractmethod
    def __init__(self, _axlecount):
        self.axleCount = _axlecount
    
class Train(GroundVehicle):
    def __init__(self, _noOfCarsAttached, _locomotiveCount):
        self.noOfCarsAttached = _noOfCarsAttached
        self.locomotiveCount = _locomotiveCount
        
    def displayCarCount(self):
        print(self.noOfCarsAttached)
    def displayLocomotiveCount(self):
        print(self.locomotiveCount)
    def travel(self):
        print("Speed 60mph, Direction E")
        
Train1 = Train(20, 2)

Train1.displayCarCount()
Train1.displayLocomotiveCount()

# At this point, my code should print out the values from the car count and the locomotive count. Further demonstration of abstract and concrete classes to follow.

# Always encapsulate parent constructors into child classes to make those variables available
class semi_Truck(RoadVehicle):
    def __init__(self, _noOfTrailersAttached):
        self.noOfTrailersAttached = _noOfTrailersAttached
    super(Vehicle.status,GroundVehicleInterface.travel())
        # Don't modify passed in values unless absolutely necessary
    def displayNoOfTrailersAttached(self):
        print(self.noOfTrailersAttached)
    def travel(self):
        print(Vehicle.status)
        
Semi_Truck1 = semi_Truck(f"This truck has {2} trailers attached.")

# Remember to be careful to check that you are running the method on an instance of the class, not on the class definition.
Semi_Truck1.displayNoOfTrailersAttached()


# Next - implement abstracted methods and constructor classes. Demonstrate use of super if Python supports it.