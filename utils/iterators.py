class AircraftIterator:
    def __init__(self,aircraft):
        self.aircraft=aircraft
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>=len(self.aircraft):
            raise StopIteration
        
        aircraft = self.aircraft[self.index]

        self.index += 1

        return aircraft
    
class WaypointIterator:
    def __init__(self,waypoints):
        self.waypoints=waypoints
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index>=len(self.waypoints):
            raise StopIteration
        waypoint=self.waypoints[self.index]

        self.index+=1

        return waypoint
    
class FilteredAircraftIterator:
    def __init__(self,aircraft,condition):
        self.aircraft=aircraft
        self.condition=condition
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index<len(self.aircraft):

            aircraft=self.aircraft[self.index]
            self.index+=1

            if  self.condition(aircraft):
                return aircraft
            
        raise StopIteration
class PriorityAircraftIterator:

    def __init__(self,aircraft,priority):
        self.aircraft=aircraft
        self.priority=priority
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.aircraft):

            aircraft=self.aircraft[self.index]

            self.index+=1

            if aircraft.priority==self.priority:
                return aircraft
        raise StopIteration






















