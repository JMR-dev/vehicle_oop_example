def main():
    class Fleet():
        vehicles = {"7E19H2", "N9460G32581A3", "BN4681"}
        def __init__(self, vtype, movspeed, travelmed, vehicleid):
            self.vehicletype = vtype
            self.movementspeed = movspeed
            self.travelmedium = travelmed
            self.uuid = vehicleid
            
        def displayAllFleetMembers(vehicles):
            map(print(vehicles))