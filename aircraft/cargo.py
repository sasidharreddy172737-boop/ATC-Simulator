from aircraft.aircraft import Aircraft

class CargoAircraft(Aircraft):
    def __init__(self,
        aircraft_id,
        flight_id,
        altitude,
        speed,
        fuel,
        cargo_weight,
        position=(0, 0),
        heading=0):

        super().__init__(aircraft_id=aircraft_id,
            flight_id=flight_id,
            aircraft_type="Cargo",
            altitude=altitude,
            speed=speed,
            fuel=fuel,
            position=position,
            heading=heading,)
        
        self.cargo_weight=cargo_weight
        
    def get_priority(self):
        return "NORMAL"
 