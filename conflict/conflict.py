
class Conflict:

    VALID_SEVERITIES = {
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    }

    def __init__(self,aircraft1,aircraft2,horizontal_distance,vertical_separation ,severity):

        if severity not in self.VALID_SEVERITIES:

            raise ValueError(
                f"Invalid conflict severity: {severity}"
            )
        
        self.aircraft1=aircraft1
        self.aircraft2=aircraft2
        self.horizontal_distance = horizontal_distance
        self.vertical_separation = vertical_separation
        self.severity=severity

    def __str__(self):

        return (
            f"CONFLICT | "
            f"{self.aircraft1.flight_id} <-> "
            f"{self.aircraft2.flight_id} | "
            f"Horizontal: "
            f"{self.horizontal_distance:.2f} | "
            f"Vertical: "
            f"{self.vertical_separation} ft | "
            f"Severity: {self.severity}"
        )

    def __repr__(self):

        return (
            f"Conflict("
            f"{self.aircraft1.flight_id!r}, "
            f"{self.aircraft2.flight_id!r}, "
            f"severity={self.severity!r}"
            f")"
        )
    def __eq__(self, other):

        if not isinstance(other, Conflict):
            return NotImplemented

        return {
        self.aircraft1.aircraft_id,
        self.aircraft2.aircraft_id,
    } == {
        other.aircraft1.aircraft_id,
        other.aircraft2.aircraft_id,
    }

