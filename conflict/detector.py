import math

from conflict.conflict import Conflict
class  ConflictDetector:
    def __init__(self,horizontal_limit=20,vertical_limit=1000):

        self.horizontal_limit=horizontal_limit

        self.vertical_limit=vertical_limit
    def calculate_horizontal_distance(self,aircraft1,aircraft2,):
        x1, y1 = aircraft1.position

        x2, y2 = aircraft2.position

        return math.sqrt((x2 - x1) ** 2 +(y2 - y1) ** 2)

    def calculate_vertical_separation(self,aircraft1,aircraft2,):

       return abs(aircraft1.altitude - aircraft2.altitude)

    def is_conflict(self,aircraft1,aircraft2):
        horizontal_diff=(self.calculate_horizontal_distance(aircraft1,aircraft2))

        vertical_diff=(self.calculate_vertical_separation(aircraft1,aircraft2))

        return (horizontal_diff <=
        self.horizontal_limit
        and
        vertical_diff <=
        self.vertical_limit
        )
    

    def determine_severity(self,horizontal_distance,vertical_separation):
        if (
        horizontal_distance <= 5
        and
        vertical_separation <= 200
        ):
            return "CRITICAL"

        if (
        horizontal_distance <= 10
        and
        vertical_separation <= 500
        ):
            return "HIGH"

        if (
        horizontal_distance <= 15
        and
        vertical_separation <= 750
        ):
            return "MEDIUM"
    
        return "LOW"
    def detect(self,aircraft1,aircraft2):

        horizontal_distance = (
            self.calculate_horizontal_distance(
            aircraft1,
            aircraft2,
            )
        )

        vertical_separation = (
            self.calculate_vertical_separation(
            aircraft1,
            aircraft2,
            )
        )

        if (
        horizontal_distance >
        self.horizontal_limit
        ):
            return None

        if (
        vertical_separation >
        self.vertical_limit
        ):
            return None

        severity = self.determine_severity(
        horizontal_distance,
        vertical_separation,
       )

        return Conflict(
        aircraft1=aircraft1,
        aircraft2=aircraft2,
        horizontal_distance=horizontal_distance,
        vertical_separation=vertical_separation,
        severity=severity,
    )
    def detect_all(self, aircraft_list):

        conflicts = []

        for i in range(len(aircraft_list)):

            for j in range(i + 1, len(aircraft_list)):

                aircraft1 = aircraft_list[i]
                aircraft2 = aircraft_list[j]

                conflict = self.detect(
                aircraft1,
                aircraft2,
            )

                if conflict:
                    conflicts.append(conflict)

        return conflicts







