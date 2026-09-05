from aircraft.aircraft import Aircraft

class PassengerAircraft(Aircraft):
    def __init__(self,aircraft_id,flight_id,altitude,speed,fuel,passenger_count,position=(0, 0),heading=0,):

        super().__init__(aircraft_id=aircraft_id,flight_id=flight_id,
            aircraft_type="Passenger",
            altitude=altitude,
            speed=speed,
            fuel=fuel,
            position=position,
            heading=heading,
        )
        self.passenger_count=passenger_count

    def get_priority(self):
        return "NORMAL"


