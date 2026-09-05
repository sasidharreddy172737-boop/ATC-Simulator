
class Waypoint:

    def __init__(self,waypoint_id,name,position,altitude):
        self.waypoint_id=waypoint_id
        self.name=name
        self.position=position
        self.altitude=altitude

    def __str__(self):
        return (f"{self.waypoint_id} - {self.name} | "
            f"Position: {self.position} | "
            f"Altitude: {self.altitude} ft"
            )
    
    def __repr__(self):
        return (
            f"Waypoint("
            f"waypoint_id={self.waypoint_id!r}, "
            f"name={self.name!r}, "
            f"position={self.position!r}, "
            f"altitude={self.altitude!r}"
            f")"
        )