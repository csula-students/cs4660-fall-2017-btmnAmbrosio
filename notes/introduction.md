# Introduction to AI

Welcome to introduction to AI course!

## Agenda

* [Syllabus](../SYLLABUS.md)
* Introduction to AI
* Set up environment
    * Wrap up Python exercise

## Metrics

* Environment setup
* Concept of Artificial Intelligence

### Introduction to Artificial Intelligence

Before we talk about Artificial Intelligence, we will need to define intelligence.

#### What is Artificial Intelligence?

There are eight definitions of AI, laid out along two dimensions:

| | Thinking | Acting |
| :-- | :-- | :--
| Humanly | "The exciting new effort to make computers think ... machines with minds, in the full and literal sense" (Haugeland, 1985)  
"[The automation of] activities that we associate with human thinking, activities such as decision-making, problem solving, learning ..." (Bellman, 1978) |
"The art of creating machines that perform functions that require intelligence when performed by people." (Kurzweil, 1990)  
"The study of how to make computers do things at which, at the moment, people are better." (Rich and Knight, 1991) |
| Rationally | "The study of mental faculties through the use of computational models." (Charniak and McDermott, 1985)  
"The study of the computations that make it possible to perceive, reason, and act." (Winston, 1992) |
"Computational Intelligence is the study of the design of intelligent agents." (Poole et al., 1998)  
"AI ... is concerned with intelligent behavior in artifacts." (Nilsson, 1998) |

> Figure 1.1 from Artificial Intelligence A Modern Approach (3rd edition)

Most well known field comes from "Acting humanly" dimension -- The Turing Tests
(proposed by Alan Turing (1950).

The Turing Tests was designed to provide a satisfactory operational definition
of intelligence. It's all about a computer acting like human by a human
interrogator. In specific, human is interacting with computer by asking a
couple questions and computer will try to answer them. At the end of test, this
human will need to judge the other side being human or computer.

The Turing Tests implies that computer would need the following capabilities to
pass the test:

* Natural language processing
* Knowledge representation
* Automated reasoning
* Machine learning
* Computer vision
* Robotics

In which, Alan Turing predicts many of the problems in next 50 years. In other
word, many of the above fields are still actively being studied now.

In this course, we will focus on the "Acting Rationally" to create the rational
agents that maximize the chance of success.

#### Rational Agents (Intelligent Agents)

In earlier section, we went over the concept of rational agents as central to
our course. In this section, we will make more concrete explanation to rational
agents. Moreover, we will go over a small set of design principles for building
successful agents -- systems that can reasonably be called intelligent.

An **agent** is anything that makes decisions based on information perceived by
its environment with its *sensors* and use *actuators* to mutate the
environment. An example of the intelligent agent would be *financial agent*.
They can get the stock market information (**sensors**) and use it to make
trades (**actuators**).

The **decisions** it involves between the information from sensors to actions of
actuators is the key of AI.

This entire loop of sensors getting information to making decisions from AI algorithm
and to actions of actuators is often called **Perception-Action cycle**.

*Perception-Action cycle* is what we (Artificial Intelligence developers) are usually
interested of implementing.

#### Omniscience vs Rationality

#### PEAS

Performance, Environment, Actuators, Sensors.

#### Environments

Following terminologies will be focus on the environment types:

* Fully vs partially observables
  * Fully means your agent can fully observe all variables of environment (e.g. chess)
  * Partially observables means your agent can only observe part of the environment (e.g. Starcraft, self-driving car)
* Deterministic vs stochastic
  * Deterministic means haves no random effects (like chess -- each moves determines next state deterministically)
  * Stochastic means having some random outcomes (like games involves dices rolling)
* Discrete vs continuous
  * Number of states in games is countable (discrete) and not-countable (continuous)
* Benign vs adversarial
  * Environment goes against you (benign) like Chess (environment -- your opponent -- is trying to defeat you)
  * Or environment is just there (like weather effect for selv-driving car)

#### Summary

AI can often be seen as an uncertainty management.

In other word, "what would you do when you don't know what to do?"

In example, we cant possibly create an imperative program that predicts every single
state for self-driving car or Go.

But how do our agents handle the situation it hasn't seen or programmed to do?

Artificial intelligence is to create such algorithm to do general problem solving.

#### Recommended reading

* https://en.wikipedia.org/wiki/Intelligent_agent

### Environment setup

Follow the note to set up Python -- https://github.com/csula/Utilities/blob/master/setups/python-setup.md

And follow the note to set up Git/Github -- https://github.com/csula/Utilities/blob/master/setups/git-github-notes.md

### Wrap Up Python Exercise

Once you set up the above two dependencies, please do this wrap up exercise to
test your local environment setup!

Since not everyone has experience of using Github/Git before, we will go over
in class exercise to demonstrate how you should submit your assignment in future.

The goal of this exercise is to review mainly two concepts (File IO &
Object Oriented Programming).

You may start reading through the source code folder for some starting point of the project.

1. Fork/clone repository
2. Code, Commit & pass unit test  
> Note 1: You can run `python -m unittest discover` to check if you passed the provided unit tests right away locally  
> Note 2: DO NOT MODIFY ANY EXISTING TEST CODES

3. Pull request & review comments  
> Note that in the pull request, you will see the build result immediately in the pull request status. Please make sure you at least pass the unit tests as they are one of the grading criteria.

If you have trouble pushing to your own repository under your workspace

```bash
git remote set-url origin {Your repository url} # https://github.com/csula/cs4660-fall-2017-exercise-1-rcliao.git for example
git commit -a # will open text editor for you to enter commit message
git push # push to origin server (which will be your repository)
```

Click here to set your repository -- https://classroom.github.com/a/5llmpWhz

1. Push your code to that repository.
2. Paste link to CSNS "Your repository" section

