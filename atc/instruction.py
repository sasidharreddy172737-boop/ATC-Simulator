class ATCInstruction:
    VALID_ACTIONS = {
        "HOLD",
        "CLIMB",
        "DESCEND",
        "TURN_LEFT",
        "TURN_RIGHT",
        "LAND",
        "TAKEOFF",
        "EMERGENCY_PRIORITY",
    }
    def __init__(self,aircraft,action,reason):
        if action not in self.VALID_ACTIONS:
            raise ValueError(f"Invalid ATC action: {action}")
        
        self.aircraft = aircraft
        self.action = action
        self.reason = reason
        self.executed = False

    def execute(self):
        if self.executed:
            return False


        aircraft = self.aircraft

        if self.action == "CLIMB":
            aircraft.altitude += 1000

        elif self.action == "DESCEND":
            aircraft.altitude -= 1000

        elif self.action == "TURN_LEFT":
            aircraft.heading=(aircraft.heading-10)%360

        elif self.action == "TURN_RIGHT":
            aircraft.heading =(aircraft.heading+10)%360

        elif self.action == "HOLD":
            aircraft.speed = 0

        elif self.action == "LAND":
            aircraft.status = "LANDING"

        elif self.action == "TAKEOFF":
            aircraft.status = "TAKEOFF"

        elif self.action == "EMERGENCY_PRIORITY":
            aircraft.priority = "CRITICAL"

        self.executed=True

        return True
        
    def __str__(self):

        return (
            f"ATC INSTRUCTION | "
            f"{self.aircraft.flight_id} | "
            f"Action: {self.action} | "
            f"Reason: {self.reason}"
        )

    def __repr__(self):

        return (
            f"ATCInstruction("
            f"{self.aircraft.flight_id!r}, "
            f"{self.action!r}"
            f")"
        )