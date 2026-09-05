import threading
class Runway:

    VALID_STATUSES={
        "AVAILABLE",
        "OCCUPIED",
        "MAINTANACE"

    }

    def __init__(self,runway_id):
        self.runway_id=runway_id
        self._status="AVAILABLE"
        self.current_aircraft=None
        self.lock = threading.Lock()

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,value):
        if value not in self.VALID_STATUSES:
            raise ValueError(f"Invalid runway status: {value}")
        self._status=value

    def is_available(self):
        return self.status=="AVAILABLE"
    
    def  reserve(self,aircraft):
        with self.lock:
            if aircraft is None:
                return False

            if not self.is_available():
               return False
            self.status="OCCUPIED"
            self.current_aircraft=aircraft
            return True
        

    def release(self):
        with self.lock:
            self.status = "AVAILABLE"
            self.current_aircraft = None
            

    def __str__(self):
        aircraft = (
            self.current_aircraft.flight_id
            if self.current_aircraft
            else "None"
        )

        return (
            f"{self.runway_id} | "
            f"Status: {self.status} | "
            f"Aircraft: {aircraft}"
        )       
    





    




