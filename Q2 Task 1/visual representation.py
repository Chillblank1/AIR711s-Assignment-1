#!/usr/bin/env python
# coding: utf-8

import numpy as np
import heapq
import matplotlib.pyplot as plt  # Importing pyplot from matplotlib

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def is_obstacle(self, x, y):
        return (x, y) in self.obstacles


class Robot:
    def __init__(self, environment, start_position, target_position, charging_station):
        self.environment = environment
        self.position = start_position
        self.target = target_position
        self.charging_station = charging_station

    def actions(self, state):
        x, y = state
        possible_actions = []

        # Define possible movements (forward, backward, left, right)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.environment.width and 0 <= new_y < self.environment.height:
                if not self.environment.is_obstacle(new_x, new_y):
                    possible_actions.append((new_x, new_y))

        return possible_actions

    def cost(self, state1, state2):
        # Simple unit cost for each movement
        return 1

    def heuristic(self, state):
        # Manhattan distance heuristic
        x1, y1 = state
        x2, y2 = self.target
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star_search(self):
        frontier = [(self.heuristic(self.position), self.position)]
        came_from = {}
        cost_so_far = {self.position: 0}

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == self.target:
                break

            for next_state in self.actions(current):
                new_cost = cost_so_far[current] + self.cost(current, next_state)
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    priority = new_cost + self.heuristic(next_state)
                    heapq.heappush(frontier, (priority, next_state))
                    came_from[next_state] = current

        # Reconstruct path
        path = []
        current = self.target
        while current != self.position:
            path.append(current)
            current = came_from[current]
        path.append(self.position)
        path.reverse()

        return path

    def hill_climbing(self):
        # Placeholder implementation of hill climbing, just returning A* search path
        return self.a_star_search()


def visualize_tsp(nodes, tsp_path):
    plt.figure(figsize=(8, 6))

    # Plotting nodes
    for node in nodes:
        plt.scatter(node[1], node[0], color='blue')  # node[1] -> x-coordinate, node[0] -> y-coordinate
        plt.text(node[1], node[0], node[2], fontsize=8)  # node[2] -> name of the place

    # Plotting TSP path
    for i in range(len(tsp_path) - 1):
        node1 = tsp_path[i]
        node2 = tsp_path[i + 1]
        plt.plot([node1[1], node2[1]], [node1[0], node2[0]], color='orange', linestyle='--')

    # Connecting the last node to the first to complete the loop
    node1 = tsp_path[-1]
    node2 = tsp_path[0]
    plt.plot([node1[1], node2[1]], [node1[0], node2[0]], color='orange', linestyle='--')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Travelling Salesman Problem Visualization')
    plt.grid(visible=True)
    plt.show()

# Define nodes (format: (y-coordinate, x-coordinate, name))
nodes = [(10, 0.3, 'Khomasdal'), (8, 4, 'Zoo Park'), (6, 3.6, 'Namibia Craft Centre'),
         (9.5, 4.7, 'National Museum'), (7.5, 5, 'ChristusKirche'),
         (0, 4.2, 'Heroes Acre')]

env = Environment(10, 10)
env.add_obstacle(2, 2)
env.add_obstacle(3, 2)
env.add_obstacle(4, 2)

robot = Robot(env, (0, 0), (9, 9), (5, 5))
path = robot.a_star_search()
print("Optimal path:", path)

# Generate TSP path using hill climbing algorithm
path = robot.hill_climbing()

# Visualize TSP path
visualize_tsp(nodes, path)
