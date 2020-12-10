from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Node:
    name: str
    orbits_over: "Node" = None

    def is_origin(self) -> bool:
        return self.name.lower() == "com"

    def count_hops(self):
        return len(self.chain()) - 1  # Not counting self but it's part of the chain

    def chain(self):
        chain = [self]
        current = self
        while not current.is_origin():
            current = current.orbits_over
            chain.append(current)
        return chain

    def common_chain(self, other: "Node") -> List["Node"]:
        chain = []
        for el1, el2 in zip(reversed(self.chain()), reversed(other.chain())):
            if el1 != el2:
                break
            chain.append(el1)
        return chain

    def __str__(self) -> str:
        if self.orbits_over:
            return f"{self.orbits_over.name}){self.name}"
        else:
            return self.name

    def __eq__(self, other: "Node") -> bool:
        return self.name == other.name


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

    me = objects["YOU"]
    santa = objects["SAN"]

    print(me.count_hops() + santa.count_hops() - 2 * len(me.common_chain(santa)))


if __name__ == "__main__":
    main()
