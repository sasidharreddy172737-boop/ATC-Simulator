from airport.runway import Runway
import threading
class Airport :
    
    def __init__ (self,airport_id,name):
        self.airport_id=airport_id
        self.name=name
        self.runways = []

        self.arrival_queue = []
        self.departure_queue = []
        self.lock = threading.Lock()

    def  add_runway(self,runway):
        self.runways.append(runway)

    def get_available_runway(self):
        for runway in self.runways:
            if runway.is_available():
                return runway
        return None
    
    def request_runway(self, aircraft):

        with self.lock:

            for runway in self.runways:

                if runway.reserve(aircraft):
                   return runway

            return None
    
    def release_runway(self, runway):
        runway.release()

    def __iter__(self):
        return iter(self.runways)


    def __str__(self):
        return (f"{self.airport_id} - {self.name}|Runways: {len(self.runways)}")