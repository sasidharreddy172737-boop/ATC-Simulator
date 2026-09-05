class AircraftMeta(type):

    registry = {}

    def __new__(mcls, name, bases, namespace):

        cls = super().__new__(
            mcls,
            name,
            bases,
            namespace
        )

        if name != "Aircraft":
            mcls.registry[name] = cls

        return cls

    @classmethod
    def get_aircraft_type(mcls, name):
        return mcls.registry.get(name)

    @classmethod
    def get_all_aircraft_types(mcls):
        return dict(mcls.registry)

    @classmethod
    def is_registered(mcls, name):
        return name in mcls.registry

    @classmethod
    def count_registered_aircraft(mcls):
        return len(mcls.registry)