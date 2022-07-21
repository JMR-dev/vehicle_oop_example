from abc import ABC, abstractmethod
import random
import enum
# ABC is imported from the standard library since Python does not natively support abstract methods and classes.
class Fleet():
    
    fleet_members = []
    
    def __init__(self, vehicleid):
        self.uuid = vehicleid
            
            
    def displayAllFleetMembers(self):
        for i in self.fleet_members:
            print(i)
        
    def addVehicle(self, newVehicleId):
        self.fleet_members.append(newVehicleId)
    
class Vehicle(ABC):
    '''Defines the properties of vehicles'''
    # _fuelType = ("Diesel", "Gasoline", "Aviation Gas", "Electricity", "Nuclear", "100LL")
    
    # https://www.geeksforgeeks.org/inheritance-and-composition-in-python/
    @abstractmethod
       
    def __init__(self, _gpsPosition, _velocity, _weight, _velocityType, _weightType, _status, vehicleid, _fuelType ):
        self.vehicleObject = Fleet(vehicleid)
        self.gpsPosition = _gpsPosition
        self.velocity = _velocity
        self.velocityType = _velocityType
        self.weight = _weight
        self.weightType = _weightType
        self.status = _status
        self.fuelType = _fuelType
    
    def loadCargo(self, _weight):
        self.status = "loading cargo"
        print(self.status)
        
class fuelTypes(enum.Enum):
    Diesel = 1
    Gasoline = 2
    Aviation_Kerosene = 3
    Electricity = 4
    Nuclear = 5
    Aviation_Gas = 6
class VehicleTypes(enum.Enum):
# This enum exists to provide easy access to the user creating a new object type
    semi_Truck = 1
    train = 2
    truck = 3
    van = 4
    car = 5
    hovercraft = 6
    barge = 7
    ship = 8
    airplane = 9
    helicopter = 10
    
class GroundVehicleInterface(ABC):
    '''Resource on Python interfaces. This is duck typed. https://realpython.com/python-interface/ Interfaces make a contract that a method must be implemented if an interface is inherited and allows differing implementations of the same method.'''
    @abstractmethod
    def travel(self):
        pass
        
class GroundVehicle(Vehicle):

    @abstractmethod
    def __init__(self, _isModular, _moveGroundVehicle, _gpsPosition, _velocity, _weight, _velocityType, _weightType, _status,vehicleid, _fuelType):
        super().__init__(_gpsPosition, _velocity, _weight, _velocityType, _weightType, _status,vehicleid, _fuelType)
        self.isModular = _isModular
        # modifier to GPS position
        self.moveGroundVehicle = _moveGroundVehicle
        
class RoadVehicle(GroundVehicle):
    
    @abstractmethod
    def __init__(self, _axlecount, _isModular, _moveGroundVehicle, _gpsPosition, _velocity, _weight, _velocityType, _weightType, _status, vehicleid, _fuelType):
        super().__init__(_isModular, _moveGroundVehicle, _gpsPosition, _velocity, _weight, _velocityType, _weightType, _status, vehicleid, _fuelType)
        self.axleCount = _axlecount
    
class Train(GroundVehicle, GroundVehicleInterface):
    def __init__(self, _noOfCarsAttached, _locomotiveCount):
        self.noOfCarsAttached = _noOfCarsAttached
        self.locomotiveCount = _locomotiveCount
        
    def displayCarCount(self):
        print(f"The train has {self.noOfCarsAttached} cars attached.")
    def displayLocomotiveCount(self):
        print(f"The train has {self.locomotiveCount} locomotives attached.")
    def travel(self):
        print("Speed 60mph, Direction E")
    def loadCargo(self, _weight, _noOfCarsAttached):
            super().loadCargo(_weight)
            self.weight = _weight + input(f"Enter cargo weight (integer values only).")
            try:
                weight = int(weight)
            except ValueError:
                self.weight = _weight + input(f"That entry was not an integer. Enter cargo weight in integers only.")
        
        
   # Pattern used for loadCargo - https://stackoverflow.com/questions/38987072/how-to-force-integer-input-in-python-3-x     
        
# Train1 = Train(20, 2)

# Train1.displayCarCount()
# Train1.displayLocomotiveCount()

# At this point, my code should print out the values from the car count and the locomotive count. Further demonstration of abstract and concrete classes to follow.

# Always encapsulate parent constructors into child classes to make those variables available
class semi_Truck(RoadVehicle, GroundVehicleInterface):
    def __init__(self, _noOfTrailersAttached, _axlecount, _isModular, _moveGroundVehicle, _gpsPosition, _velocity, _weight, _velocityType, _weightType, _status, vehicleid, _fuelType):
        self.noOfTrailersAttached = _noOfTrailersAttached
        # super in Python returns an object representing the parent class and 
        super().__init__(_axlecount, _isModular, _moveGroundVehicle, _gpsPosition, _velocity, _weight, _velocityType, _weightType, _status, vehicleid, _fuelType)
        # Don't modify passed in values unless absolutely necessary
    def displaySemiAttributes(self):
        print(f"The semi has {self.noOfTrailersAttached} trailers attached", f"and {self.axleCount} axles.")
    def travel(self):
        print(self.status)
    def loadCargo(self, _weight):
        super().loadCargo(_weight)
        # How do I access the set value in the init above?
        try:
            self.weight = _weight + int(input(f"Enter cargo weight (integer values only)."))
            print(f"The semi truck is {self.status}.", f"Cargo weight is {self.weight}.")
        except ValueError:
            self.weight = _weight + int(input(f"That entry was not an integer. Enter cargo weight in integers only."))
            print(f"The semi truck is {self.status}.", f"Cargo weight is {self.weight}.")

# https://realpython.com/factory-method-python/
# Factory method patterns, both standard and polymorphic - https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html#preventing-direct-creation
class VehicleSerializer():
    Vehicle(object)
    def vehicleGen(n):
        for i in range(n):
            yield random.choice([semi_Truck, Train])
            
    def factory(type, vehicleGen):
        try:
            for vehicle in VehicleTypes:
                if type == vehicle:
                    vehicleGen()
                elif type == False:
                      "Bad vehicle creation: " + type            
            
        except TypeError:   
            assert 0, "Bad vehicle creation: " + type
        finally:
            "Unexpected object creation error"


    
# Create object first before asking for input. Then insert object
    
 
# STruck = semi_Truck(2, 4, True, [40.0000, 40.0000], [56.0000, 89.0000], 60, 90000, "mph", "lbs,", "Ready", "1F8HNG7", "diesel")       

# When possible, build your argument requirements from the top down so that by the time you implement your concrete classes, you know all the data points that you need to include.
# Remember to be careful to check that you are running the method on an instance of the class, not on the class definition.
# STruck.displaySemiAttributes()

# STruck.loadCargo(90000)



# Next - implement abstracted methods and constructor classes. Demonstrate use of super if Python supports it.
# Use these values in instances and show that values can be accessed regardless of what level they live on.
# Make vehicle objects, add them to the fleet, and then have displayAllVehicles show the newly added vehicle. Stretch/further off, have different types of vehicles travel regardless of type.

    ''' 
    Code scratchpad

    For the travel method implemented from the interface

    Vehicle.velocity = self.moveGroundVehicle
            print("Traveling")
            
    Object implementation

    Semi_Truck1 = semi_Truck(f"This truck has {2} trailers attached", f"and {4} axles.", True, [49.8900000, 50.900000])

    # vehicle1 = Fleet("car", 120, "ground", Fleet.vehicles[0])
    
    # vehicle1.displayAllFleetMembers()

    # addVehicle = Fleet("hovercraft", 50, "ground/water", 0)

    # vehicle1.displayAllFleetMembers()

    Error message
        Enter cargo weight (integer values only).70000
    Traceback (most recent call last):
    File "/Users/jason.ross/workspace/python_oop_practice/vehicle_oop_example/fleet.py", line 126, in <module>
        STruck.loadCargo(90000)
    File "/Users/jason.ross/workspace/python_oop_practice/vehicle_oop_example/fleet.py", line 113, in loadCargo
        self.weight = _weight + input(f"Enter cargo weight (integer values only).")
    TypeError: unsupported operand type(s) for +: 'int' and 'str'


    Scrapped factory class

    def inputFunc(self, user_input, listVehicleTypes):
            def _listVtypes():
                listVehicleTypes = print(map(VehicleTypes))
                return listVehicleTypes
            user_input = [input("Enter vehicle weight"), ]
            return listVehicleTypes, user_input
        
        def serialize(self, user_input, inputFunc):
            serializer = inputFunc(user_input, VehicleTypes)
            return serializer(user_input)
    '''