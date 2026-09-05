# Air Traffic Control Simulator

A Python-based Air Traffic Control Simulator that models aircraft, airspace, routes, simulation processing, conflict detection, and air traffic control decisions.

The project is built entirely with Python and focuses on applying Object-Oriented Programming and advanced Python concepts to a practical simulation system.

## Features

* Passenger, Cargo, and Emergency Aircraft
* Object-Oriented Programming
* Class inheritance
* Airport and runway management
* Airspace management
* Routes and waypoints
* Aircraft navigation
* Simulation engine
* Synchronous simulation
* Asynchronous simulation
* Multithreading
* Thread synchronization and locks
* Aircraft conflict detection
* ATC controller
* ATC instructions and execution
* Aircraft priority management
* Metaclasses and automatic aircraft registration
* Custom iterators
* Filtered aircraft processing
* Priority-based aircraft processing
* Interactive terminal menu
* Automated testing

## Python Concepts Used

This project focuses on important Python concepts including:

* Classes and Objects
* Encapsulation
* Inheritance
* Polymorphism
* Properties
* Magic methods
* Iterators
* `__iter__()` and `__next__()`
* Exception handling
* Multithreading
* Thread synchronization
* Locks
* Metaclasses
* Class registration
* Functions and modules
* Lists and dictionaries

## Project Structure

```text
ATC-Simulator/
│
├── main.py
├── test.py
│
├── aircraft/
│   ├── aircraft.py
│   ├── aircraft_meta.py
│   ├── passenger.py
│   ├── cargo.py
│   └── emergency.py
│
├── airport/
│   ├── airport.py
│   └── runway.py
│
├── airspace/
│   └── airspace.py
│
├── route/
│   ├── route.py
│   └── waypoint.py
│
├── conflict/
│   ├── conflict.py
│   └── detector.py
│
├── atc/
│   ├── controller.py
│   └── instruction.py
│
├── simulation/
│   └── engine.py
│
└── util/
    └── iterator.py
```

## How It Works

The simulator follows this general flow:

```text
Aircraft
   ↓
Airspace
   ↓
Routes & Waypoints
   ↓
Aircraft Navigation
   ↓
Simulation Engine
   ↓
Multithreaded Processing
   ↓
Conflict Detection
   ↓
ATC Controller
   ↓
ATC Instructions
   ↓
Instruction Execution
```

## Aircraft Types

### Passenger Aircraft

Represents aircraft carrying passengers.

Stores information such as:

* Aircraft ID
* Flight ID
* Altitude
* Speed
* Fuel
* Passenger count
* Position
* Heading

### Cargo Aircraft

Represents cargo aircraft and includes cargo weight information.

### Emergency Aircraft

Represents aircraft experiencing an emergency.

Emergency aircraft automatically receive:

```text
Status: EMERGENCY
Priority: CRITICAL
```

## Airspace

The airspace system manages aircraft currently operating within the simulated airspace.

Aircraft can be:

* Added
* Removed
* Iterated
* Filtered
* Processed according to priority

## Airport and Runway Management

The airport system manages runways and aircraft runway requests.

Runways can have states such as:

```text
AVAILABLE
OCCUPIED
MAINTENANCE
```

Aircraft can reserve and release runways.

## Routes and Navigation

Aircraft can follow routes consisting of multiple waypoints.

The simulation updates aircraft positions as they move toward their current waypoint.

When an aircraft reaches a waypoint, it advances to the next waypoint.

## Simulation Engine

The simulation engine controls the progression of the simulation using ticks.

Each tick can:

1. Process aircraft
2. Move aircraft
3. Complete routes
4. Detect conflicts
5. Generate ATC instructions
6. Execute instructions
7. Update simulation statistics

The simulator supports both normal and asynchronous execution.

## Multithreading

Aircraft can be processed concurrently using Python threads.

Each aircraft can be handled by a separate worker thread during simulation processing.

Thread synchronization is used to protect shared simulation state.

## Conflict Detection

The simulator checks aircraft positions and altitude separation to identify potential conflicts.

Detected conflicts can be classified according to severity and processed by the ATC controller.

## ATC Controller

The ATC controller processes detected conflicts and generates instructions for aircraft.

Example instruction types include:

```text
HOLD
CLIMB
DESCEND
TURN_LEFT
TURN_RIGHT
LAND
TAKEOFF
EMERGENCY_PRIORITY
```

The instructions are then executed against the aircraft state.

## Metaclass Aircraft Registry

The project uses a custom metaclass to automatically register aircraft subclasses.

Aircraft types such as:

```text
PassengerAircraft
CargoAircraft
EmergencyAircraft
```

are automatically registered when their classes are created.

This allows the simulator to inspect available aircraft types dynamically.

## Custom Iterators

The project implements custom Python iterators including:

```text
AircraftIterator
WaypointIterator
FilteredAircraftIterator
PriorityAircraftIterator
```

These iterators demonstrate Python's iterator protocol using:

```python
__iter__()
__next__()
```

and `StopIteration`.

## Interactive User Interface

The simulator provides a terminal-based menu.

Users can:

```text
1. Create Airspace
2. Add Passenger Aircraft
3. Add Cargo Aircraft
4. Add Emergency Aircraft
5. View All Aircraft
6. View Aircraft Registry
7. Filter Aircraft
8. View Aircraft by Priority
9. Run Simulation
10. Run Async Simulation
11. View Active Conflicts
12. View Simulation Statistics
13. Remove Aircraft
14. System Status
15. Exit
```

All aircraft and airspace information can be entered interactively through the terminal.

## Running the Project

Make sure Python is installed.

Open the project directory in a terminal and run:

```bash
python main.py
```

The interactive ATC Simulator menu will appear.

## Running Tests

The project also includes an automated test file.

Run:

```bash
python test.py
```

The test suite checks major components including:

* Aircraft creation
* Aircraft inheritance
* Aircraft status
* Aircraft equality
* Metaclass registration
* Airspace management
* Custom iterators
* Simulation engine
* Conflict detection
* Statistics
* Reset functionality
* Asynchronous simulation

## Example

A typical simulation can contain:

```text
Passenger Aircraft
Flight: AI101
Altitude: 10000 ft
Speed: 450 knots
Passengers: 180

Cargo Aircraft
Flight: CA202
Altitude: 12000 ft
Speed: 420 knots

Emergency Aircraft
Flight: EM303
Altitude: 8000 ft
Status: EMERGENCY
Priority: CRITICAL
```

The simulation processes these aircraft, monitors their positions, detects conflicts, and allows the ATC controller to generate and execute instructions.

## Project Objective

The main objective of this project is to build a complete simulation using Python while practicing advanced Python programming concepts in a realistic problem domain.

The project was developed as a structured multi-day learning project, progressing from basic Object-Oriented Programming to multithreading, conflict detection, ATC control, metaclasses, iterators, and final system integration.

## Technologies

```text
Python
Object-Oriented Programming
Inheritance
Iterators
Multithreading
Thread Synchronization
Metaclasses
Exception Handling
```

No external frameworks or databases are required.

## Author

Developed as a Python learning and portfolio project focused on Object-Oriented Programming and advanced Python concepts.

