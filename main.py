from aircraft.passenger import PassengerAircraft
from aircraft.cargo import CargoAircraft
from aircraft.emergency import EmergencyAircraft

from aircraft.aircraft_meta import AircraftMeta

from airspace.airspace import Airspace

from simulation.engine import SimulationEngine

from utils.iterators import (
    AircraftIterator,
    FilteredAircraftIterator,
    PriorityAircraftIterator,
)


airspace = None
engine = None


def print_line():
    print("=" * 70)


def print_header(title):
    print()
    print_line()
    print(f"{title:^70}")
    print_line()


def print_section(title):
    print()
    print("-" * 70)
    print(title)
    print("-" * 70)


def pause():
    input("\nPress ENTER to continue...")


def create_airspace():
    global airspace
    global engine

    if airspace is not None:
        print("\nAirspace already exists.")

        choice = input(
            "Do you want to replace it? (y/n): "
        ).strip().lower()

        if choice != "y":
            return

    print_header("CREATE AIRSPACE")

    airspace_id = input(
        "Enter airspace ID: "
    ).strip()

    name = input(
        "Enter airspace name: "
    ).strip()

    if not airspace_id or not name:
        print("Airspace ID and name cannot be empty.")
        return

    airspace = Airspace(
        airspace_id,
        name
    )

    engine = SimulationEngine(
        airspace
    )

    print("\nAirspace created successfully.")


def get_common_aircraft_data():

    aircraft_id = input(
        "Aircraft ID: "
    ).strip()

    flight_id = input(
        "Flight ID: "
    ).strip()

    altitude = int(
        input("Altitude (ft): ")
    )

    speed = int(
        input("Speed (knots): ")
    )

    fuel = int(
        input("Fuel: ")
    )

    x = int(
        input("Position X: ")
    )

    y = int(
        input("Position Y: ")
    )

    heading = int(
        input("Heading (0-359): ")
    )

    return (
        aircraft_id,
        flight_id,
        altitude,
        speed,
        fuel,
        (x, y),
        heading,
    )


def add_passenger_aircraft():

    if airspace is None:
        print("\nCreate an airspace first.")
        return

    print_header("ADD PASSENGER AIRCRAFT")

    try:

        (
            aircraft_id,
            flight_id,
            altitude,
            speed,
            fuel,
            position,
            heading,
        ) = get_common_aircraft_data()

        passenger_count = int(
            input("Passenger count: ")
        )

        aircraft = PassengerAircraft(
            aircraft_id=aircraft_id,
            flight_id=flight_id,
            altitude=altitude,
            speed=speed,
            fuel=fuel,
            passenger_count=passenger_count,
            position=position,
            heading=heading,
        )

        airspace.add_aircraft(
            aircraft
        )

        print(
            f"\n{flight_id} added successfully."
        )

    except ValueError as error:

        print(
            f"\nInvalid input: {error}"
        )


def add_cargo_aircraft():

    if airspace is None:
        print("\nCreate an airspace first.")
        return

    print_header("ADD CARGO AIRCRAFT")

    try:

        (
            aircraft_id,
            flight_id,
            altitude,
            speed,
            fuel,
            position,
            heading,
        ) = get_common_aircraft_data()

        cargo_weight = int(
            input("Cargo weight: ")
        )

        aircraft = CargoAircraft(
            aircraft_id=aircraft_id,
            flight_id=flight_id,
            altitude=altitude,
            speed=speed,
            fuel=fuel,
            cargo_weight=cargo_weight,
            position=position,
            heading=heading,
        )

        airspace.add_aircraft(
            aircraft
        )

        print(
            f"\n{flight_id} added successfully."
        )

    except ValueError as error:

        print(
            f"\nInvalid input: {error}"
        )


def add_emergency_aircraft():

    if airspace is None:
        print("\nCreate an airspace first.")
        return

    print_header("ADD EMERGENCY AIRCRAFT")

    try:

        (
            aircraft_id,
            flight_id,
            altitude,
            speed,
            fuel,
            position,
            heading,
        ) = get_common_aircraft_data()

        emergency_type = input(
            "Emergency type: "
        ).strip()

        aircraft = EmergencyAircraft(
            aircraft_id=aircraft_id,
            flight_id=flight_id,
            altitude=altitude,
            speed=speed,
            fuel=fuel,
            emergency_type=emergency_type,
            position=position,
            heading=heading,
        )

        airspace.add_aircraft(
            aircraft
        )

        print(
            f"\nEmergency flight "
            f"{flight_id} added successfully."
        )

    except ValueError as error:

        print(
            f"\nInvalid input: {error}"
        )


def view_aircraft():

    if airspace is None:
        print("\nCreate an airspace first.")
        return

    print_header("AIRCRAFT IN AIRSPACE")

    if airspace.get_aircraft_count() == 0:
        print("No aircraft currently in airspace.")
        return

    iterator = AircraftIterator(
        airspace.aircraft
    )

    count = 0

    for aircraft in iterator:

        count += 1

        print(f"\n[{count}]")

        print(
            f"Aircraft ID : {aircraft.aircraft_id}"
        )

        print(
            f"Flight ID   : {aircraft.flight_id}"
        )

        print(
            f"Type        : {aircraft.aircraft_type}"
        )

        print(
            f"Altitude    : {aircraft.altitude} ft"
        )

        print(
            f"Speed       : {aircraft.speed} knots"
        )

        print(
            f"Fuel        : {aircraft.fuel}"
        )

        print(
            f"Position    : {aircraft.position}"
        )

        print(
            f"Heading     : {aircraft.heading}"
        )

        print(
            f"Status      : {aircraft.status}"
        )

        print(
            f"Priority    : {aircraft.priority}"
        )


def view_registry():

    print_header("AIRCRAFT METACLASS REGISTRY")

    registry = (
        AircraftMeta.get_all_aircraft_types()
    )

    if not registry:
        print("No aircraft classes registered.")
        return

    print(
        f"Registered types: "
        f"{AircraftMeta.count_registered_aircraft()}"
    )

    print()

    for name in registry:
        print(f"✓ {name}")


def filter_aircraft():

    if airspace is None:
        print("\nCreate an airspace first.")
        return

    print_header("FILTER AIRCRAFT")

    print("1. Passenger")
    print("2. Cargo")
    print("3. Emergency")

    choice = input(
        "\nChoose type: "
    ).strip()

    aircraft_type = None

    if choice == "1":
        aircraft_type = "Passenger"

    elif choice == "2":
        aircraft_type = "Cargo"

    elif choice == "3":
        aircraft_type = "Emergency"

    else:
        print("Invalid choice.")
        return

    iterator = FilteredAircraftIterator(
        airspace.aircraft,
        lambda aircraft:
            aircraft.aircraft_type == aircraft_type
    )

    print()

    found = False

    for aircraft in iterator:

        found = True

        print(
            f"{aircraft.flight_id} | "
            f"{aircraft.aircraft_type} | "
            f"{aircraft.altitude} ft | "
            f"{aircraft.status}"
        )

    if not found:
        print(
            f"No {aircraft_type} aircraft found."
        )


def view_priority_aircraft():

    if airspace is None:
        print("\nCreate an airspace first.")
        return

    print_header("AIRCRAFT BY PRIORITY")

    print("1. NORMAL")
    print("2. HIGH")
    print("3. CRITICAL")

    choice = input(
        "\nChoose priority: "
    ).strip()

    priority_map = {
        "1": "NORMAL",
        "2": "HIGH",
        "3": "CRITICAL",
    }

    priority = priority_map.get(choice)

    if priority is None:
        print("Invalid choice.")
        return

    iterator = PriorityAircraftIterator(
        airspace.aircraft,
        priority
    )

    found = False

    print()

    for aircraft in iterator:

        found = True

        print(
            f"{aircraft.flight_id} | "
            f"{aircraft.aircraft_type} | "
            f"Priority: {aircraft.priority}"
        )

    if not found:
        print(
            f"No {priority} priority aircraft found."
        )


def run_simulation():

    global engine

    if airspace is None:
        print("\nCreate an airspace first.")
        return

    if airspace.get_aircraft_count() == 0:
        print("\nNo aircraft available.")
        return

    print_header("RUN SIMULATION")

    try:

        ticks = int(
            input(
                "Number of simulation ticks: "
            )
        )

        if ticks <= 0:
            print(
                "Ticks must be greater than zero."
            )
            return

        engine = SimulationEngine(
            airspace
        )

        engine.run(ticks)

        print(
            "\nSimulation completed."
        )

    except ValueError as error:
        print(
            f"\nInvalid input: {error}"
        )


def run_async_simulation():

    global engine

    if airspace is None:
        print("\nCreate an airspace first.")
        return

    if airspace.get_aircraft_count() == 0:
        print("\nNo aircraft available.")
        return

    print_header("ASYNC SIMULATION")

    try:

        ticks = int(
            input(
                "Number of simulation ticks: "
            )
        )

        if ticks <= 0:
            print(
                "Ticks must be greater than zero."
            )
            return

        engine = SimulationEngine(
            airspace
        )

        print(
            "\nStarting asynchronous simulation..."
        )

        engine.start_async(ticks)

        engine.wait_for_simulation()

        print(
            "\nAsynchronous simulation completed."
        )

    except ValueError as error:
        print(
            f"\nInvalid input: {error}"
        )


def view_conflicts():

    if engine is None:
        print(
            "\nRun a simulation first."
        )
        return

    print_header("ACTIVE CONFLICTS")

    conflicts = (
        engine.get_active_conflicts()
    )

    if not conflicts:
        print(
            "No active conflicts."
        )
        return

    print(
        f"Active conflicts: "
        f"{len(conflicts)}"
    )

    print()

    for conflict in conflicts:
        print(conflict)


def view_statistics():

    if engine is None:
        print(
            "\nRun a simulation first."
        )
        return

    print_header("SIMULATION STATISTICS")

    statistics = (
        engine.get_statistics()
    )

    for key, value in statistics.items():

        print(
            f"{key:<25}: {value}"
        )


def remove_aircraft():

    if airspace is None:
        print("\nCreate an airspace first.")
        return

    if not airspace.aircraft:
        print("\nNo aircraft available.")
        return

    print_header("REMOVE AIRCRAFT")

    aircraft_id = input(
        "Enter aircraft ID to remove: "
    ).strip()

    target = None

    for aircraft in airspace:

        if aircraft.aircraft_id == aircraft_id:

            target = aircraft
            break

    if target is None:
        print(
            "\nAircraft not found."
        )
        return

    airspace.remove_aircraft(
        target
    )

    print(
        f"\nAircraft "
        f"{target.aircraft_id} removed."
    )


def system_status():

    print_header("SYSTEM STATUS")

    if airspace is None:

        print(
            "Airspace: NOT CREATED"
        )

    else:

        print(
            f"Airspace ID   : "
            f"{airspace.airspace_id}"
        )

        print(
            f"Airspace Name : "
            f"{airspace.name}"
        )

        print(
            f"Aircraft      : "
            f"{airspace.get_aircraft_count()}"
        )

    print()

    print(
        "Registered aircraft types: "
        f"{AircraftMeta.count_registered_aircraft()}"
    )

    if engine is None:

        print(
            "Simulation Engine: NOT CREATED"
        )

    else:

        print(
            "Simulation Engine: CREATED"
        )

        print(
            f"Running: "
            f"{engine.is_running()}"
        )


def show_menu():

    print()
    print_line()

    print(
        "AIR TRAFFIC CONTROL SIMULATOR"
    )

    print_line()

    print("1.  Create Airspace")
    print("2.  Add Passenger Aircraft")
    print("3.  Add Cargo Aircraft")
    print("4.  Add Emergency Aircraft")
    print("5.  View All Aircraft")
    print("6.  View Aircraft Registry")
    print("7.  Filter Aircraft")
    print("8.  View Aircraft by Priority")
    print("9.  Run Simulation")
    print("10. Run Async Simulation")
    print("11. View Active Conflicts")
    print("12. View Simulation Statistics")
    print("13. Remove Aircraft")
    print("14. System Status")
    print("15. Exit")

    print_line()


def menu():

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":
            create_airspace()

        elif choice == "2":
            add_passenger_aircraft()

        elif choice == "3":
            add_cargo_aircraft()

        elif choice == "4":
            add_emergency_aircraft()

        elif choice == "5":
            view_aircraft()

        elif choice == "6":
            view_registry()

        elif choice == "7":
            filter_aircraft()

        elif choice == "8":
            view_priority_aircraft()

        elif choice == "9":
            run_simulation()

        elif choice == "10":
            run_async_simulation()

        elif choice == "11":
            view_conflicts()

        elif choice == "12":
            view_statistics()

        elif choice == "13":
            remove_aircraft()

        elif choice == "14":
            system_status()

        elif choice == "15":

            print_header(
                "EXITING SIMULATOR"
            )

            print(
                "Thank you for using the "
                "Air Traffic Control Simulator."
            )

            print(
                "Simulation terminated."
            )

            break

        else:

            print(
                "\nInvalid choice."
            )

        pause()


if __name__ == "__main__":

    try:

        menu()

    except KeyboardInterrupt:

        print(
            "\n\nSimulator interrupted by user."
        )

    except Exception as error:

        print(
            "\nUnexpected error:"
        )

        print(error)