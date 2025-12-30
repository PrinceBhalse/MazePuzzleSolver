# A* Pathfinding Algorithm in Python

This repository contains a Python implementation of the **A*** (A-star) **pathfinding algorithm** applied to a grid-based maze environment. The project demonstrates how heuristic-based search algorithms can efficiently compute the shortest path between two points, a concept widely used in **AI, game development, robotics, and routing systems**.

---

## 📌 Project Overview

The A* algorithm is an informed search algorithm that combines:

* **g-cost**: the actual cost from the start node to the current node
* **h-cost (heuristic)**: an estimated cost from the current node to the goal

By minimizing the total cost `f = g + h`, A* guarantees the **optimal shortest path** when an admissible heuristic is used.

In this project, a maze is generated using the `pyamaze` library, and an intelligent agent navigates from the start cell to the goal cell using A* search.

---

## 🚀 Features

* Implementation of **A*** search algorithm from scratch in Python
* Uses **Priority Queue (min-heap)** for efficient node expansion
* **Manhattan Distance heuristic** for grid-based path estimation
* Visual simulation of agent movement inside a maze
* Clean and modular code structure

---

## 🧠 Concepts Covered

* Graph traversal and shortest path algorithms
* Heuristic-based search and optimization
* Priority Queues and cost evaluation (g-cost, f-cost)
* Artificial Intelligence search techniques
* Problem-solving using Data Structures and Algorithms (DSA)

---

## 🛠️ Tech Stack

* **Programming Language**: Python
* **Libraries Used**:

  * `queue` (PriorityQueue)
  * `pyamaze` (maze generation and visualization)

---

## 📂 Project Structure

```
.
├── maze.py             # Main Python script containing A* implementation
├── README.md           # Project documentation
```

---

## ▶️ How to Run the Project

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/a-star-pathfinding-python.git](https://github.com/PrinceBhalse/MazePuzzleSolver.git
   cd MazePuzzleSolver
   ```

2. Install dependencies

   ```bash
   pip install pyamaze
   ```

3. Run the script

   ```bash
   python maze.py
   ```

A maze window will open showing the agent navigating the shortest path from start to goal.

---

## 📊 Example Use Cases

* Game AI (NPC pathfinding)
* Robotics navigation and motion planning
* GPS and routing systems
* Autonomous agents and simulations

---

## 📈 Future Enhancements

* Support for weighted graphs
* Comparison with BFS, DFS, and Dijkstra’s algorithm
* Dynamic obstacle handling
* Performance and time complexity analysis

---

## 👤 Author

**Prince Bhalse**

* LinkedIn: [https://linkedin.com/in/prince-bhalse](https://www.linkedin.com/in/prince-bhalse-050470271)
* GitHub: [https://github.com/PrinceBhalse](https://github.com/PrinceBhalse)

---

## ⭐ Acknowledgements

* Inspired by classical AI search algorithms
* Visualization powered by the `pyamaze` Python library

---

If you find this project useful, feel free to ⭐ star the repository!
