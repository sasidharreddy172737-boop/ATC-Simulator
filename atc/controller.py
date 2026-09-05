from atc.instruction import ATCInstruction
class ATCController:

    def __init__(self):

        self.instructions = []
        self.resolved_conflicts = []

    def get_priority_value(self, aircraft):

        priority_values = {
        "NORMAL": 1,
        "HIGH": 2,
        "CRITICAL": 3,
        }

        return priority_values.get(
        aircraft.priority,
        1
    )

    def select_priority_aircraft(
    self,
    aircraft1,
    aircraft2,
    ):

        priority1 = self.get_priority_value(
        aircraft1
        )

        priority2 = self.get_priority_value(
        aircraft2
         )

        if priority1 > priority2:
            return aircraft1

        if priority2 > priority1:
            return aircraft2

        return None
    def create_instruction(
    self,
    aircraft,
    action,
    reason,
):

        instruction = ATCInstruction(
            aircraft=aircraft,
            action=action,
            reason=reason,
    )

        self.instructions.append(instruction)

        return instruction

    def resolve_conflict(self, conflict):

        aircraft1 = conflict.aircraft1
        aircraft2 = conflict.aircraft2

        priority_aircraft = (
        self.select_priority_aircraft(
            aircraft1,
            aircraft2,
        )
    )

        if priority_aircraft is aircraft1:

            instruction = self.create_instruction(
            aircraft2,
            "DESCEND",
            "Give priority to "
            f"{aircraft1.flight_id}",
        )

        elif priority_aircraft is aircraft2:

            instruction = self.create_instruction(
            aircraft1,
            "DESCEND",
            "Give priority to "
            f"{aircraft2.flight_id}",
        )

        else:

            instruction = self.create_instruction(
            aircraft2,
            "TURN_RIGHT",
            "Conflict avoidance",
        )

        self.resolved_conflicts.append(
        conflict
    )

        return instruction
    def process_conflicts(self, conflicts):

        instructions = []

        for conflict in conflicts:

            instruction = self.resolve_conflict(
            conflict
        )

            instructions.append(instruction)

        return instructions
    def get_instructions(self):

        return list(self.instructions)

    def get_resolved_conflicts(self):

        return list(
        self.resolved_conflicts
    )

    def execute_instruction(self, instructions):
        executed = []

        for instruction in instructions:

            if instruction.execute():

                executed.append(instruction)

        return instruction.execute()
    
