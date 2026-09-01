import json

class ElectricalComponent:
    def __init__(self, name):
        self.name = name


class Resistor(ElectricalComponent):
    def __init__(self, name, resistance):
        super().__init__(name)
        self.resistance = resistance

    def __str__(self):
        return f"Resistor: {self.name} ({self.resistance} Ohm)"


class Capacitor(ElectricalComponent):
    def __init__(self, name, capacitance):
        super().__init__(name)
        self.capacitance = capacitance

    def __str__(self):
        return f"Capacitor: {self.name} ({self.capacitance} F)"


class Inductor(ElectricalComponent):
    def __init__(self, name, inductance):
        super().__init__(name)
        self.inductance = inductance

    def __str__(self):
        return f"Inductor: {self.name} ({self.inductance} H)"


def add_resistor(components):
    name = input("Enter resistor name: ")
    resistance = float(input("Enter resistance: "))

    if resistance <= 0:
        print("Resistance must be greater than zero.")
        return

    resistor = Resistor(name, resistance)
    components.append(resistor)
    print("Resistor added successfully!")


def add_capacitor(components):
    name = input("Enter capacitor name: ")
    capacitance = float(input("Enter capacitance: "))

    if capacitance <= 0:
        print("Capacitance must be greater than zero.")
        return

    capacitor = Capacitor(name, capacitance)
    components.append(capacitor)
    print("Capacitor added successfully!")


def add_inductor(components):
    name = input("Enter inductor name: ")
    inductance = float(input("Enter inductance: "))

    if inductance <= 0:
        print("Inductance must be greater than zero.")
        return

    inductor = Inductor(name, inductance)
    components.append(inductor)
    print("Inductor added successfully!")


def show_components(components):
    if not components:
        print("No components found!")
        return

    print("====== Components ======")
    for component in components:
        print(component)


def search_component(components):
    name = input("Enter component name: ").lower()

    found = False

    for component in components:
        if component.name.lower() == name:
            print("Found:")
            print(component)
            found = True
            break

    if not found:
        print("Component not found!")


def save_to_json(components):
    data = []

    for component in components:

        if isinstance(component, Resistor):
            data.append({
                "type": "resistor",
                "name": component.name,
                "resistance": component.resistance
            })

        elif isinstance(component, Capacitor):
            data.append({
                "type": "capacitor",
                "name": component.name,
                "capacitance": component.capacitance
            })

        elif isinstance(component, Inductor):
            data.append({
                "type": "inductor",
                "name": component.name,
                "inductance": component.inductance
            })

    with open("component.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Components saved successfully!")


def load_from_json(components):
    try:
        with open("component.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("component.json not found!")
        return

    components.clear()

    for item in data:

        if item["type"] == "resistor":
            components.append(
                Resistor(item["name"], item["resistance"])
            )

        elif item["type"] == "capacitor":
            components.append(
                Capacitor(item["name"], item["capacitance"])
            )

        elif item["type"] == "inductor":
            components.append(
                Inductor(item["name"], item["inductance"])
            )

    print("Components loaded successfully!")


components = []

while True:

    print("\n====== Electrical Components Database ======")
    print("1. Add Resistor")
    print("2. Add Capacitor")
    print("3. Add Inductor")
    print("4. Show Components")
    print("5. Save to JSON")
    print("6. Load from JSON")
    print("7. Search Component")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_resistor(components)

        elif choice == 2:
            add_capacitor(components)

        elif choice == 3:
            add_inductor(components)

        elif choice == 4:
            show_components(components)

        elif choice == 5:
            save_to_json(components)

        elif choice == 6:
            load_from_json(components)

        elif choice == 7:
            search_component(components)

        elif choice == 8:
            print("Goodbye! :) ")
            break

        else:
            print("Please enter a number between 1 and 8.")

    except ValueError:
        print("Please enter a valid number.")