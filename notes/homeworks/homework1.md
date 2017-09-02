# Homework 1 - Graph Representation

## Due Date Time

### 09/16/2017 Midnight (23:59:59)

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
correctly. Eventually, you will implement methods to use these variables.

You will need to implement/modify three classes (AdjancencyList,
AdjancencyMatrix & ObjectOriented) under `graphes.py`.

In these three classes, you will be implementing similar methods for graph
(e.g. `adjacent`, `neighbors` or `addNode` ... etc.) but with different
underlying data structure.

Please review the note from knowledge representation for theoretical differences
of these three ways of representing graph.

## Input format

```
4
0:3:4
1:2:1
2:3:4
3:1:2
```

First line is the total number of nodes.

> In this homework, we will create node with unique id starting from 0  
> In other word, if we have four nodes; they are node 0, 1, 2, 3

Starting from second line, you will get `{fromNode}:{toNode}:{value}` for each
edge (line).

Your job is to parse these lines of edges and add them into graph.

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

