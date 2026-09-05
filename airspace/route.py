from utils.iterators import WaypointIterator
class Route:
    def __init__(self,route_id,name):

        self.route_id=route_id
        self.name=name
        self.waypoints=[]
        self.current_index=0

    def add_waypoints(self,waypoint):

        self.waypoints.append(waypoint)

    def get_current_waypoint(self):
        if  not self.waypoints:
            return None
        
        if self.current_index>=len(self.waypoints):
            return None
        
        return self.waypoints[self.current_index]
    def get_next_waypoint(self):
        next_index=self.current_index+1

        if next_index>=len(self.waypoints):

            return None
        return self.waypoints[next_index]
    
    def advance(self):
        if self.current_index>=len(self.waypoints):
            return False
        self.current_index+=1
        return True

    def is_complete(self):
        if self.current_index>=len(self.waypoints):
            return True
        else:
            return False
        
    def reset(self):
        self.current_index=0

    def __iter__(self):
        return WaypointIterator(self.waypoints)

    def __len__(self):
        return len(self.waypoints)

    def __str__(self):
        return (
            f"{self.route_id} - {self.name} | "
            f"Waypoints: {len(self.waypoints)}"
        )

        
