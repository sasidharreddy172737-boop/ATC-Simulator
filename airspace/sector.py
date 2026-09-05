class Sector:
    def __init__(self,sector_id,name,x_min,x_max,y_min,y_max):

        self.sector_id=sector_id

        self.name=name

        self.x_min=x_min
        self.x_max=x_max
        self.y_min=y_min
        self.y_max=y_max

        self.aircraft = []

    def contains_position(self,position):
        x,y=position

        if self.x_min <= x <=self.x_max and self.y_min<= y <= self.y_max:
            return True
        else:
            return False

    def add_aircraft(self,aircr):

        if aircr not in self.aircraft:
            self.aircraft.append(aircr)

    def remove_aircraft(self,aircr):

        if  aircr in self.aircraft:
            self.aircraft.remove(aircr)

    def contain_aircraft(self,aircraft):

        if  aircraft in self.aircraft:
            return True
        else:
            return False
        
    def __iter__(self):
        return iter(self.aircraft)
    
    def __len__(self):
        return len(self.aircraft)
    
    def __str__(self):
        return (
            f"{self.sector_id} - {self.name} | "
            f"Aircraft: {len(self.aircraft)}"
        )


