from dataclasses import dataclass
from typing import Dict


@dataclass
class Node:
    name: str
    orbits_over: "Node" = None

    def is_origin(self) -> bool:
        return self.name.lower() == "com"

    def count_hops(self):
        counter = 0
        current = self
        while not current.is_origin():
            current = current.orbits_over
            counter += 1
        return counter


def main():
    with open("inputs/day06") as f:
        orbits = f.read().split()
    objects = dict()  # type: Dict[str, Node]
    for orbit in orbits:
        stator, rotor = orbit.split(")")
        stator = objects.get(stator, Node(name=stator))
        rotor = objects.get(rotor, Node(name=rotor))
        rotor.orbits_over = stator
        objects[stator.name] = stator
        objects[rotor.name] = rotor

    counter = 0
    for obj in objects.values():
        counter += obj.count_hops()

    print(counter)


if __name__ == "__main__":
    main()
