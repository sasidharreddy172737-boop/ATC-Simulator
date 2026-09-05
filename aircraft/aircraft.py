from aircraft.aircraft_meta import AircraftMeta
class Aircraft:
    AIRCRAFT_COUNT=0

    VALID_STATUSES = {
    "SCHEDULED",
    "TAXIING",
    "TAKEOFF",
    "CLIMBING",
    "CRUISING",
    "DESCENDING",
    "APPROACH",
    "LANDING",
    "LANDED",
    "EMERGENCY",
} 
    VALID_TRANSITIONS = {
    "SCHEDULED": {"TAXIING", "EMERGENCY"},
    "TAXIING": {"TAKEOFF", "EMERGENCY"},
    "TAKEOFF": {"CLIMBING", "EMERGENCY"},
    "CLIMBING": {"CRUISING", "DESCENDING", "EMERGENCY"},
    "CRUISING": {"DESCENDING", "EMERGENCY"},
    "DESCENDING": {"APPROACH", "EMERGENCY"},
    "APPROACH": {"LANDING", "EMERGENCY"},
    "LANDING": {"LANDED", "EMERGENCY"},
    "LANDED": set(),
    "EMERGENCY": {"LANDING", "LANDED"},
}
    
    def __init__(self,aircraft_id,flight_id,aircraft_type,altitude,speed,fuel,status="SCHEDULED"
                 ,position=(0,0),heading=0, priority="NORMAL"):
        self.aircraft_id = aircraft_id
        self.flight_id = flight_id
        self.aircraft_type = aircraft_type
        self.altitude = altitude
        self.speed = speed
        self.fuel = fuel
        self.position=position
        self.heading=heading
        self._status = None
        self.status = status
        self.priority=priority
        self.route = None

        Aircraft.AIRCRAFT_COUNT += 1

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,value):
        if value not in self.VALID_STATUSES:
            raise ValueError(f"Invalid aircraft status: {value}")
        
        self._status=value

    def change_status(self, new_status):

        if new_status  not in self.VALID_STATUSES:
             raise ValueError(f"Invalid aircraft status: {new_status}")
        
        allowed= self.VALID_TRANSITIONS[self.status]
        
        if new_status not in allowed:
            raise ValueError(
            f"Cannot change status from "
            f"{self.status} to {new_status}"
        )
             
        self.status = new_status

    def assign_route(self, route):
        self.route = route

    def get_current_waypoint(self):
        if self.route is None:
             return None
        return self.route.get_current_waypoint()
    
    def get_next_waypoint(self):

        if self.route is None:
            return None

        return self.route.get_next_waypoint()
    def advanced_route(self):

        if self.route is None:
                    return False
         
         
        return self.route.advance()  
         
          


         




    def __str__(self):
         return (
            f"{self.flight_id} | "
            f"{self.aircraft_type} | "
            f"{self.altitude} ft | "
            f"{self.speed} knots | "
            f"{self.status}|"
            f"{self.priority}|"
        )
    def __repr__(self):
        return (
            f"Aircraft("
            f"aircraft_id={self.aircraft_id!r}, "
            f"flight_id={self.flight_id!r}, "
            f"aircraft_type={self.aircraft_type!r}"
            f")"
        )
    
    def __eq__(self,other):
        if not isinstance(other,Aircraft):
            return NotImplemented

        return self.aircraft_id==other.aircraft_id
    
    def request_landing(self):
        return f"{self.flight_id} requests landing"

    def request_takeoff(self):
        return f"{self.flight_id} requests takeoff"

    def declare_emergency(self, emergency_type):
        self.status = "EMERGENCY"
        self.priority = "CRITICAL"

        return (
        f"{self.flight_id} declared emergency: "
        f"{emergency_type}"
        )


