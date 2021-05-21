"""
In search.py, you will implement generic search algorithms
"""

import util
import copy


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


class Node:

    def __init__(self, cur_state, former_state, action, cost=0):
        """
        constructor of Node class.
        param cur_state: the current stae in the frienge.
        param former_state: the former state of this state.
        param action: the action to get to this state.
        """
        self.cur_state = cur_state
        self.action = action
        self.former_state = former_state
        self.cost = cost

    def get_cost(self):
        return self.cost

    def get_state(self):
        return self.cur_state

    def get_action(self):
        return self.action

    def get_former(self):
        return self.former_state


def tree_search(fringe, problem: SearchProblem):
    """
    a generic function to search in SearchProblem
    :param fringe; data structure for the search (queue, priority queue, stack)
    :param problem: SearchProblem to solve.
    :return: list of action to get the solution.
    None if there isnt.
    """
    closed = set()
    fringe.push(Node(problem.get_start_state(), None, None, 0))
    while not fringe.isEmpty():
        current = fringe.pop()

        if problem.is_goal_state(current.get_state()):
            actions = []
            while current.get_former() is not None:
                actions.append(current.get_action())
                current = current.get_former()
            return list(reversed(actions))

        elif current.get_state() not in closed:
            successors = problem.get_successors(current.get_state())

            for successor in successors:
                node = Node(successor[0], current, successor[1],
                            successor[2] + current.get_cost())
                fringe.push(node)
            closed.add(current.get_state())
    return None


def depth_first_search(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.
    use tree search with stack.
    """
    return tree_search(util.Stack(), problem)


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    use tree search with Queue.
    """
    return tree_search(util.Queue(), problem)


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    use tree search with PriorityQueueWithFunction
    """
    return tree_search(util.PriorityQueueWithFunction(lambda item: item.get_cost()),
                       problem)


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    return tree_search(util.PriorityQueueWithFunction(lambda item: item.get_cost() + heuristic(item.get_state(),
                                                      problem)),
                       problem)


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
