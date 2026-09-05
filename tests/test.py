from aircraft.passenger import PassengerAircraft
from aircraft.cargo import CargoAircraft
from aircraft.emergency import EmergencyAircraft

from aircraft.aircraft_meta import AircraftMeta

from airspace.airspace import Airspace

from simulation.engine import SimulationEngine

from utils.iterators import (
    AircraftIterator,
    WaypointIterator,
    FilteredAircraftIterator,
    PriorityAircraftIterator,
)


passed = 0
failed = 0


def header(title):
    print()
    print("=" * 70)
    print(f"{title:^70}")
    print("=" * 70)


def section(title):
    print()
    print("-" * 70)
    print(title)
    print("-" * 70)


def pass_test(message):
    global passed

    passed += 1

    print(
        f"[PASS] {message}"
    )


def fail_test(message, error=None):
    global failed

    failed += 1

    print(
        f"[FAIL] {message}"
    )

    if error:
        print(
            f"       Error: {error}"
        )


def create_test_aircraft():

    passenger = PassengerAircraft(
        aircraft_id="TEST001",
        flight_id="TEST-P01",
        altitude=30000,
        speed=450,
        fuel=8000,
        passenger_count=180,
        position=(0, 0),
        heading=90,
    )

    cargo = CargoAircraft(
        aircraft_id="TEST002",
        flight_id="TEST-C01",
        altitude=28000,
        speed=420,
        fuel=9000,
        cargo_weight=50000,
        position=(100, 100),
        heading=180,
    )

    emergency = EmergencyAircraft(
        aircraft_id="TEST003",
        flight_id="TEST-E01",
        altitude=15000,
        speed=400,
        fuel=5000,
        emergency_type="ENGINE FAILURE",
        position=(200, 200),
        heading=270,
    )

    return passenger, cargo, emergency


def test_aircraft_creation():

    section("AIRCRAFT CREATION")

    try:

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        if passenger.aircraft_type == "Passenger":
            pass_test(
                "PassengerAircraft creation"
            )
        else:
            fail_test(
                "PassengerAircraft creation"
            )

        if cargo.aircraft_type == "Cargo":
            pass_test(
                "CargoAircraft creation"
            )
        else:
            fail_test(
                "CargoAircraft creation"
            )

        if emergency.aircraft_type == "Emergency":
            pass_test(
                "EmergencyAircraft creation"
            )
        else:
            fail_test(
                "EmergencyAircraft creation"
            )

    except Exception as error:

        fail_test(
            "Aircraft creation",
            error
        )


def test_aircraft_status():

    section("AIRCRAFT STATUS")

    try:

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        if passenger.status == "SCHEDULED":
            pass_test(
                "Default aircraft status"
            )
        else:
            fail_test(
                "Default aircraft status"
            )

        emergency.declare_emergency(
            "ENGINE FAILURE"
        )

        if emergency.status == "EMERGENCY":
            pass_test(
                "Emergency status"
            )
        else:
            fail_test(
                "Emergency status"
            )

        if emergency.priority == "CRITICAL":
            pass_test(
                "Emergency priority"
            )
        else:
            fail_test(
                "Emergency priority"
            )

    except Exception as error:

        fail_test(
            "Aircraft status",
            error
        )


def test_aircraft_equality():

    section("AIRCRAFT EQUALITY")

    try:

        aircraft1 = PassengerAircraft(
            aircraft_id="EQ001",
            flight_id="EQ101",
            altitude=30000,
            speed=450,
            fuel=8000,
            passenger_count=100,
        )

        aircraft2 = PassengerAircraft(
            aircraft_id="EQ001",
            flight_id="EQ202",
            altitude=25000,
            speed=400,
            fuel=7000,
            passenger_count=120,
        )

        if aircraft1 == aircraft2:
            pass_test(
                "Aircraft equality by aircraft_id"
            )
        else:
            fail_test(
                "Aircraft equality by aircraft_id"
            )

    except Exception as error:

        fail_test(
            "Aircraft equality",
            error
        )


def test_metaclass():

    section("METACLASS REGISTRY")

    try:

        required_types = [
            "PassengerAircraft",
            "CargoAircraft",
            "EmergencyAircraft",
        ]

        for aircraft_type in required_types:

            if AircraftMeta.is_registered(
                aircraft_type
            ):
                pass_test(
                    f"{aircraft_type} registration"
                )
            else:
                fail_test(
                    f"{aircraft_type} registration"
                )

        passenger_class = (
            AircraftMeta.get_aircraft_type(
                "PassengerAircraft"
            )
        )

        if passenger_class is PassengerAircraft:
            pass_test(
                "Aircraft class lookup"
            )
        else:
            fail_test(
                "Aircraft class lookup"
            )

        registry = (
            AircraftMeta.get_all_aircraft_types()
        )

        if len(registry) >= 3:
            pass_test(
                "Aircraft registry contains classes"
            )
        else:
            fail_test(
                "Aircraft registry contains classes"
            )

    except Exception as error:

        fail_test(
            "Metaclass registry",
            error
        )


def test_airspace():

    section("AIRSPACE")

    try:

        airspace = Airspace(
            "TEST-AS01",
            "Test Airspace"
        )

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        airspace.add_aircraft(
            passenger
        )

        airspace.add_aircraft(
            cargo
        )

        airspace.add_aircraft(
            emergency
        )

        if airspace.get_aircraft_count() == 3:
            pass_test(
                "Aircraft added to airspace"
            )
        else:
            fail_test(
                "Aircraft added to airspace"
            )

        if len(list(airspace)) == 3:
            pass_test(
                "Airspace iteration"
            )
        else:
            fail_test(
                "Airspace iteration"
            )

        airspace.remove_aircraft(
            cargo
        )

        if airspace.get_aircraft_count() == 2:
            pass_test(
                "Aircraft removal"
            )
        else:
            fail_test(
                "Aircraft removal"
            )

    except Exception as error:

        fail_test(
            "Airspace",
            error
        )


def test_aircraft_iterator():

    section("AIRCRAFT ITERATOR")

    try:

        aircraft = [
            "A",
            "B",
            "C",
        ]

        iterator = AircraftIterator(
            aircraft
        )

        result = []

        for item in iterator:
            result.append(item)

        if result == aircraft:
            pass_test(
                "AircraftIterator traversal"
            )
        else:
            fail_test(
                "AircraftIterator traversal"
            )

        try:

            next(iterator)

            fail_test(
                "AircraftIterator StopIteration"
            )

        except StopIteration:

            pass_test(
                "AircraftIterator StopIteration"
            )

    except Exception as error:

        fail_test(
            "AircraftIterator",
            error
        )


def test_waypoint_iterator():

    section("WAYPOINT ITERATOR")

    try:

        waypoints = [
            "W1",
            "W2",
            "W3",
        ]

        iterator = WaypointIterator(
            waypoints
        )

        result = list(iterator)

        if result == waypoints:
            pass_test(
                "WaypointIterator traversal"
            )
        else:
            fail_test(
                "WaypointIterator traversal"
            )

    except Exception as error:

        fail_test(
            "WaypointIterator",
            error
        )


def test_filtered_iterator():

    section("FILTERED AIRCRAFT ITERATOR")

    try:

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        aircraft = [
            passenger,
            cargo,
            emergency,
        ]

        iterator = FilteredAircraftIterator(
            aircraft,
            lambda item:
                item.aircraft_type == "Passenger"
        )

        result = list(iterator)

        if len(result) == 1:

            if result[0] is passenger:

                pass_test(
                    "FilteredAircraftIterator"
                )

            else:

                fail_test(
                    "FilteredAircraftIterator result"
                )

        else:

            fail_test(
                "FilteredAircraftIterator result"
            )

    except Exception as error:

        fail_test(
            "FilteredAircraftIterator",
            error
        )


def test_priority_iterator():

    section("PRIORITY AIRCRAFT ITERATOR")

    try:

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        aircraft = [
            passenger,
            cargo,
            emergency,
        ]

        iterator = PriorityAircraftIterator(
            aircraft,
            "CRITICAL"
        )

        result = list(iterator)

        if len(result) == 1:

            if result[0] is emergency:

                pass_test(
                    "PriorityAircraftIterator"
                )

            else:

                fail_test(
                    "PriorityAircraftIterator result"
                )

        else:

            fail_test(
                "PriorityAircraftIterator result"
            )

    except Exception as error:

        fail_test(
            "PriorityAircraftIterator",
            error
        )


def test_simulation():

    section("SIMULATION ENGINE")

    try:

        airspace = Airspace(
            "TEST-AS02",
            "Simulation Test Airspace"
        )

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        airspace.add_aircraft(
            passenger
        )

        airspace.add_aircraft(
            cargo
        )

        airspace.add_aircraft(
            emergency
        )

        engine = SimulationEngine(
            airspace
        )

        engine.run(2)

        statistics = (
            engine.get_statistics()
        )

        if statistics["ticks"] == 2:
            pass_test(
                "Simulation tick processing"
            )
        else:
            fail_test(
                "Simulation tick processing"
            )

        if statistics["aircraft"] == 3:
            pass_test(
                "Simulation aircraft count"
            )
        else:
            fail_test(
                "Simulation aircraft count"
            )

    except Exception as error:

        fail_test(
            "Simulation engine",
            error
        )


def test_conflicts():

    section("CONFLICT DETECTION")

    try:

        airspace = Airspace(
            "TEST-AS03",
            "Conflict Test Airspace"
        )

        aircraft1 = PassengerAircraft(
            aircraft_id="CON001",
            flight_id="CON101",
            altitude=30000,
            speed=450,
            fuel=8000,
            passenger_count=100,
            position=(0, 0),
            heading=90,
        )

        aircraft2 = CargoAircraft(
            aircraft_id="CON002",
            flight_id="CON202",
            altitude=30000,
            speed=440,
            fuel=8000,
            cargo_weight=30000,
            position=(10, 10),
            heading=270,
        )

        airspace.add_aircraft(
            aircraft1
        )

        airspace.add_aircraft(
            aircraft2
        )

        engine = SimulationEngine(
            airspace
        )

        conflicts = engine.detect_conflicts()

        if isinstance(conflicts, list):

            pass_test(
                "Conflict detector execution"
            )

        else:

            fail_test(
                "Conflict detector execution"
            )

    except Exception as error:

        fail_test(
            "Conflict detection",
            error
        )


def test_statistics():

    section("STATISTICS")

    try:

        airspace = Airspace(
            "TEST-AS04",
            "Statistics Test Airspace"
        )

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        airspace.add_aircraft(
            passenger
        )

        airspace.add_aircraft(
            cargo
        )

        airspace.add_aircraft(
            emergency
        )

        engine = SimulationEngine(
            airspace
        )

        statistics = (
            engine.get_statistics()
        )

        required_keys = [
            "ticks",
            "simulation_time",
            "aircraft",
            "updates",
            "conflicts",
        ]

        for key in required_keys:

            if key in statistics:

                pass_test(
                    f"Statistics key: {key}"
                )

            else:

                fail_test(
                    f"Statistics key: {key}"
                )

    except Exception as error:

        fail_test(
            "Statistics",
            error
        )


def test_engine_reset():

    section("ENGINE RESET")

    try:

        airspace = Airspace(
            "TEST-AS05",
            "Reset Test Airspace"
        )

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        airspace.add_aircraft(
            passenger
        )

        engine = SimulationEngine(
            airspace
        )

        engine.run(2)

        engine.reset()

        statistics = (
            engine.get_statistics()
        )

        if statistics["ticks"] == 0:
            pass_test(
                "Engine tick reset"
            )
        else:
            fail_test(
                "Engine tick reset"
            )

        if statistics["simulation_time"] == 0:
            pass_test(
                "Simulation time reset"
            )
        else:
            fail_test(
                "Simulation time reset"
            )

    except Exception as error:

        fail_test(
            "Engine reset",
            error
        )


def test_async_simulation():

    section("ASYNC SIMULATION")

    try:

        airspace = Airspace(
            "TEST-AS06",
            "Async Test Airspace"
        )

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        airspace.add_aircraft(
            passenger
        )

        airspace.add_aircraft(
            cargo
        )

        airspace.add_aircraft(
            emergency
        )

        engine = SimulationEngine(
            airspace
        )

        engine.start_async(2)

        engine.wait_for_simulation()

        statistics = (
            engine.get_statistics()
        )

        if statistics["ticks"] == 2:

            pass_test(
                "Asynchronous simulation"
            )

        else:

            fail_test(
                "Asynchronous simulation"
            )

    except Exception as error:

        fail_test(
            "Asynchronous simulation",
            error
        )


def test_string_representation():

    section("STRING REPRESENTATION")

    try:

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        passenger_text = str(
            passenger
        )

        cargo_text = str(
            cargo
        )

        emergency_text = str(
            emergency
        )

        if passenger.flight_id in passenger_text:
            pass_test(
                "Passenger __str__"
            )
        else:
            fail_test(
                "Passenger __str__"
            )

        if cargo.flight_id in cargo_text:
            pass_test(
                "Cargo __str__"
            )
        else:
            fail_test(
                "Cargo __str__"
            )

        if emergency.flight_id in emergency_text:
            pass_test(
                "Emergency __str__"
            )
        else:
            fail_test(
                "Emergency __str__"
            )

    except Exception as error:

        fail_test(
            "String representation",
            error
        )


def test_invalid_status():

    section("STATUS VALIDATION")

    try:

        passenger, cargo, emergency = (
            create_test_aircraft()
        )

        try:

            passenger.status = "INVALID_STATUS"

            fail_test(
                "Invalid status validation"
            )

        except ValueError:

            pass_test(
                "Invalid status validation"
            )

    except Exception as error:

        fail_test(
            "Status validation",
            error
        )


def run_all_tests():

    global passed
    global failed

    passed = 0
    failed = 0

    header(
        "AIR TRAFFIC CONTROL SIMULATOR"
    )

    print(
        "FINAL PROJECT TEST SUITE"
    )

    test_aircraft_creation()

    test_aircraft_status()

    test_aircraft_equality()

    test_metaclass()

    test_airspace()

    test_aircraft_iterator()

    test_waypoint_iterator()

    test_filtered_iterator()

    test_priority_iterator()

    test_simulation()

    test_conflicts()

    test_statistics()

    test_engine_reset()

    test_async_simulation()

    test_string_representation()

    test_invalid_status()

    header(
        "FINAL TEST RESULTS"
    )

    print(
        f"Tests Passed : {passed}"
    )

    print(
        f"Tests Failed : {failed}"
    )

    print(
        f"Total Checks : {passed + failed}"
    )

    print()

    if failed == 0:

        print(
            "✓ ALL TESTS PASSED"
        )

        print(
            "✓ PROJECT IS WORKING CORRECTLY"
        )

    else:

        print(
            "✗ SOME TESTS FAILED"
        )

        print(
            "Review the failed tests above."
        )


if __name__ == "__main__":

    try:

        run_all_tests()

    except KeyboardInterrupt:

        print(
            "\nTest execution interrupted."
        )

    except Exception as error:

        print(
            "\nUnexpected test error:"
        )

        print(error)