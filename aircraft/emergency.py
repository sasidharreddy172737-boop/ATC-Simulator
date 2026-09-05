from aircraft.aircraft import Aircraft


class EmergencyAircraft(Aircraft):
    def __init__(
        self,
        aircraft_id,
        flight_id,
        altitude,
        speed,
        fuel,
        emergency_type,
        position=(0, 0),
        heading=0,
    ):
        super().__init__(
            aircraft_id=aircraft_id,
            flight_id=flight_id,
            aircraft_type="Emergency",
            altitude=altitude,
            speed=speed,
            fuel=fuel,
            status="EMERGENCY",
            priority="CRITICAL",
            position=position,
            heading=heading,
        )

        self.emergency_type = emergency_type

    def get_priority(self):
        return "CRITICAL"