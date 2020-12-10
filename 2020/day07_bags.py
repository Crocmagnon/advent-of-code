import re
from typing import List

import networkx as nx


def main(filename: str, expected_part_1: int = None, expected_part_2: int = None):
    print(f"\n+ Running on {filename}")
    with open(filename) as f:
        rules = f.read().strip().split("\n")  # type: List[str]

    graph_part_1 = nx.DiGraph()
    graph_part_2 = nx.DiGraph()
    for rule in rules:
        edges = extract_edges_from_rule(rule, container_first=False)
        graph_part_1.add_weighted_edges_from(edges)
        edges = extract_edges_from_rule(rule, container_first=True)
        graph_part_2.add_weighted_edges_from(edges)

    counter_part_1 = solve_part_1(graph_part_1)
    counter_part_2 = solve_part_2(graph_part_2)

    print(f"1. Found {counter_part_1}")
    if expected_part_1:
        assert expected_part_1 == counter_part_1

    print(f"2. Found {counter_part_2}")
    if expected_part_2:
        assert expected_part_2 == counter_part_2


def extract_edges_from_rule(rule: str, container_first: bool):
    if "no other bags" in rule:
        return []
    container, contained = rule.split(" bags contain")
    contained = contained.split(", ")
    edges = []
    spec_regex = re.compile(r"^(?P<quantity>\d+) (?P<name>\w+ \w+) bags?\.?$")
    for specification in contained:
        specification = specification.strip()
        match = spec_regex.match(specification)
        assert match, f"Spec '{specification}' must match regex '{spec_regex}'"
        groups = match.groupdict()
        if container_first:
            edges.append((container, groups["name"], int(groups["quantity"])))
        else:
            edges.append((groups["name"], container, int(groups["quantity"])))
    return edges


def solve_part_1(graph: nx.DiGraph):
    res = set()
    to_see = {"shiny gold"}
    while to_see:
        next_node = to_see.pop()
        linked_nodes = set(graph[next_node])
        res.update(linked_nodes)
        to_see.update(linked_nodes)
    return len(res)


def solve_part_2(graph: nx.DiGraph):
    bag_weight = 0
    to_see = [{"name": "shiny gold", "weight": 1}]
    while to_see:
        current_node = to_see.pop()
        linked_nodes = graph[current_node["name"]]
        for node_name, data in linked_nodes.items():
            multiplier = current_node["weight"] * data["weight"]
            bag_weight += multiplier
            to_see.append({"name": node_name, "weight": multiplier})
    return bag_weight


if __name__ == "__main__":
    main("inputs/day07-test1", 4, 32)
    main("inputs/day07-test2", None, 126)
    main("inputs/day07", 378)
