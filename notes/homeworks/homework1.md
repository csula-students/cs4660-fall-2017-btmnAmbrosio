# Homework 1 - Graph Representation

## Due Date Time

### 09/23/2017 Midnight (23:59:59)

## Performance Measure

* Being able to read from file (File IO)
* Being able to pass unit tests of graph classes
* Github Pull Request (be sure to pass all unit tests)

:no_entry_sign: DO NOT MODIFY ANY EXISTING TEST CODES :no_entry_sign:

> A successful Pull Request is required (only containing the changes needed) for
> submission. In other word, files changed section should be minimum for your
> homework related changes.

## Grading Rubric

* Pass unit tests [10 pts]
* Bonus Question - see bonus questions above [2 pts]

## Description

In this homework, you will start your assignment just like exercise before. You
will need to read from file, parse information line by line and store them
correctly. Next, you will implement methods to use these data in the graph
classes (AdjacencyList, AdjacencyMatrix & ObjectOriented).

In these three classes, you will be implementing similar methods for graph
(e.g. `adjacent`, `neighbors` or `addNode` ... etc.) but with different
underlying data structure (see [course note on knowledge representation][1]).

## Tasks

- [ ] Understand input file format
- [ ] Implement `construct_graph_from_file` method
- [ ] Implement `add_node` and `add_edge` method to confirm `construct_graph_file` is working
- [ ] Implement each graph representation separately
    - [ ] Implement `adjacent` method
    - [ ] Implement `neighbors` method
    - [ ] Implement `remove_node` method
    - [ ] Implement `remove_edge` method

> Tip: you can run `python -m unittest test.test_graph.TestAdjacencyMatrix` to
> to test individual graph representation

### Input format

The starting point for the homework is by looking at the input file like below:

```
4
0:3:4
1:2:1
2:3:4
3:1:2
```

First line is *the total number of nodes* while each node contains the number
data as simplification of actual node.

> In this homework, we will create node with unique id starting from 0
> In other word, if we have four nodes; they are node 0, 1, 2, 3

Starting from second line, you will get format of `{fromNode}:{toNode}:{value}`
for each line representing an edge. From second line and onward, the program
should parse the line and add such edge back to the graph like pseudocode below:

```
for line in each_line:
    edge = parse_line_to_edge(line)
    graph.add_edge(edge)
```

## Bonus

Answer the following questions in plain text format

1. Explain with the runtime analysis on each method you have implemented in each of
the representation using Big-O notation
2. Consider Chess, what is the performance measure, environment, actuator and sensor?
3. Same with Chess, formulate the problem in 5 components (initial state, possible
actions, transition model, goal test, and path cost)
4. Define Chess environment type, is it fully observable or partially observable,
is it deterministic or stochastic, is it discrete or continuous, is it benign or
adversarial?


[1]: ../graph-representation.md#3-ways-to-represent-graph-in-programming
