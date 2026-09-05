import threading
import time

from conflict.detector import ConflictDetector
from atc.controller import ATCController


class SimulationEngine:

    def __init__(self, airspace):

        self.running = False
        self.airspace = airspace

        self.tick_count = 0
        self.simulation_time = 0
        self.tick_duration = 1

        self.total_updates = 0

        self.simulation_thread = None

       
        self.stats_lock = threading.Lock()
        self.state_lock = threading.Lock()
        self.engine_lock = threading.Lock()

        
        self.conflict_detector = ConflictDetector()
        self.active_conflicts = []
        self.total_conflicts = 0
        self.atc_controller = ATCController()

   
    def start(self):

        with self.state_lock:

            if self.running:
                return

            self.running = True

        print("SIMULATION STARTED")

    def stop(self):

        with self.state_lock:
            self.running = False

        print("SIMULATION STOPPED")

    def is_running(self):

        with self.state_lock:
            return self.running

    
    def tick(self):

        if not self.is_running():
            return

        with self.engine_lock:

            self.tick_count += 1
            self.simulation_time += self.tick_duration

            current_tick = self.tick_count

        print(
            f"\n--- SIMULATION TICK "
            f"{current_tick} ---"
        )

        
        self.process_aircraft_concurrently()

        
        conflicts = self.detect_conflicts()

        self.process_atc(conflicts)

    

    def simulation_loop(self, ticks):

        for _ in range(ticks):

            if not self.is_running():
                break

            self.tick()

    

    def move_aircraft(self, aircraft):

        waypoint = aircraft.get_current_waypoint()

        if waypoint is None:
            return

        x, y = aircraft.position
        step = 10

        target_x, target_y = waypoint.position

       
        if x > target_x:
            x = max(x - step, target_x)

        elif x < target_x:
            x = min(x + step, target_x)

        
        if y > target_y:
            y = max(y - step, target_y)

        elif y < target_y:
            y = min(y + step, target_y)

        aircraft.position = (x, y)

       
        if self.has_reached_waypoint(aircraft):
            aircraft.advance_route()

    def has_reached_waypoint(self, aircraft):

        waypoint = aircraft.get_current_waypoint()

        if waypoint is None:
            return False

        return waypoint.position == aircraft.position

   
    def update_aircraft(self, aircraft):

        time.sleep(0.1)

        self.move_aircraft(aircraft)

        self.handle_route_completion(aircraft)

        
        with self.stats_lock:
            self.total_updates += 1

        print(
            f"{aircraft.flight_id} | "
            f"Position: {aircraft.position} | "
            f"Status: {aircraft.status}"
        )

    def aircraft_worker(self, aircraft):

        self.update_aircraft(aircraft)

    

    def process_aircraft_concurrently(self):

        threads = []

       
        for aircraft in self.airspace:

            thread = threading.Thread(
                target=self.aircraft_worker,
                args=(aircraft,),
                name=f"Aircraft-{aircraft.flight_id}"
            )

            threads.append(thread)

       
        for thread in threads:
            thread.start()

        
        for thread in threads:
            thread.join()

   
    def handle_route_completion(self, aircraft):

        if aircraft.route is None:
            return

        if aircraft.route.is_complete():

            if aircraft.status != "LANDED":

                aircraft.status = "LANDED"

                print(
                    f"{aircraft.flight_id} "
                    f"has landed."
                )

    
    def detect_conflicts(self):

        conflicts = (
            self.conflict_detector.detect_all(
                self.airspace
            )
        )

      
        self.active_conflicts = conflicts

        
        with self.stats_lock:
            self.total_conflicts += len(conflicts)

        
        for conflict in conflicts:

            print(
                f"⚠ {conflict}"
            )

        return conflicts

    def get_active_conflicts(self):

        return list(self.active_conflicts)

    

    def get_statistics(self):

        with self.stats_lock:

            total_updates = self.total_updates
            total_conflicts = self.total_conflicts

        with self.engine_lock:

            ticks = self.tick_count
            simulation_time = self.simulation_time

        return {
            "ticks": ticks,
            "simulation_time": simulation_time,
            "aircraft": len(self.airspace),
            "updates": total_updates,
            "conflicts": total_conflicts,
        }

    def run(self, ticks):

        self.start()

        for _ in range(ticks):

            if not self.is_running():
                break

            self.tick()

        self.stop()

    

    def start_async(self, ticks):

        with self.state_lock:

            if self.running:
                return

            self.running = True

        self.simulation_thread = threading.Thread(
            target=self.simulation_loop,
            args=(ticks,),
            name="SimulationThread"
        )

        self.simulation_thread.start()

    def wait_for_simulation(self):

        if self.simulation_thread is not None:

            self.simulation_thread.join()

    def reset(self):

        with self.state_lock:
            self.running = False

        with self.engine_lock:
            self.tick_count = 0
            self.simulation_time = 0

        with self.stats_lock:
            self.total_updates = 0
            self.total_conflicts = 0

        self.active_conflicts = []

        print("SIMULATION RESET")
    def process_atc(self, conflicts):

        if not conflicts:
            return []

        instructions = (
           self.atc_controller.process_conflicts(
            conflicts
        )
    )

        for instruction in instructions:

            print(f"✈ {instruction}")

        executed = (
        self.atc_controller.execute_instructions(
            instructions
        )
    )

        for instruction in executed:

            aircraft = instruction.aircraft

            print(
            f"✓ {aircraft.flight_id} updated | "
            f"Altitude: {aircraft.altitude} | "
            f"Heading: {aircraft.heading} | "
            f"Speed: {aircraft.speed} | "
            f"Status: {aircraft.status}"
        )

        return executed



