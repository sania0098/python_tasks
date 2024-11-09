class Appliance:
    """Base class for all appliances."""
    pass

class KitchenAppliance(Appliance):
    """Derived class for kitchen appliances."""
    pass

class CleaningAppliance(Appliance):
    """Derived class for cleaning appliances."""
    pass

class Microwave(KitchenAppliance):
    """Further subclass for a microwave."""
    pass

class Vacuum(CleaningAppliance):
    """Further subclass for a vacuum cleaner."""
    pass

# List of all classes for comparison
classes = [Appliance, KitchenAppliance, CleaningAppliance, Microwave, Vacuum]

# Printing results in a table-like format
print(f"{'Class':<20}", end="")
for cls in classes:
    print(f"{cls.__name__:<20}", end="")
print()

for cls1 in classes:
    print(f"{cls1.__name__:<20}", end="")
    for cls2 in classes:
        is_subclass = issubclass(cls1, cls2)
        print(f"{'Yes' if is_subclass else 'No':<20}", end="")
    print()

