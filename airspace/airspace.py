from utils.iterators import AircraftIterator
class Airspace:
    def __init__(self, airspace_id, name):

        self.airspace_id = airspace_id

        self.name = name

        self.sectors=[]

        self.active_aircrafts=[]

    def add_sectors(self,aircraft):
        self.sectors.append(aircraft)

    def add_aircrafts(self,aircraft):
        if  aircraft not in self.active_aircrafts:
            self.active_aircraft.append(aircraft)

    def  remove_aircrafts(self,aircraft):
        if  aircraft in self.active_aircrafts:
            self.active_aircrafts.remove(aircraft) 
    
    def find_sector(self, position):
        for sector in self.sectors:
            if sector.contains_position(position):
                return sector

        return None
    def assign_aircraft_to_sector(self, aircraft):
        sector = self.find_sector(aircraft.position)

        if sector is None:
            return None

        sector.add_aircraft(aircraft)

        return sector
    
    def __iter__(self):
        return AircraftIterator(self.active_aircraft)

    def __len__(self):
        return len(self.active_aircraft)

    def __str__(self):
        return f"{self.airspace_id} - {self.name}"