from collections import deque

class Node:
    def __init__(self, state, parent=None, action=None):   # Corrected line
        self.state = state
        self.parent = parent
        self.action = action

    def get_path(self):
        path = []
        current = self
        while current.parent is not None:
            path.append(current.action)
            current = current.parent
        path.reverse()
        return path

    def is_goal(self, goal_state):
        return self.state == goal_state

def get_blank_index(state):
    return state.index(0)

def move_up(state):
    blank_index = get_blank_index(state)
    if blank_index not in [0, 1, 2]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]
        return new_state
    return None

def move_down(state):
    blank_index = get_blank_index(state)
    if blank_index not in [6, 7, 8]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
        return new_state
    return None

def move_left(state):
    blank_index = get_blank_index(state)
    if blank_index not in [0, 3, 6]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
        return new_state
    return None

def move_right(state):
    blank_index = get_blank_index(state)
    if blank_index not in [2, 5, 8]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
        return new_state
    return None

def expand_node(node):
    expanded_nodes = []
    state = node.state
    actions = ['Up', 'Down', 'Left', 'Right']
    move_functions = [move_up, move_down, move_left, move_right]

    for action, move_func in zip(actions, move_functions):
        new_state = move_func(state)
        if new_state is not None:
            new_node = Node(new_state, parent=node, action=action)
            expanded_nodes.append(new_node)

    return expanded_nodes

def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([Node(initial_state)])

    while queue:
        node = queue.popleft()
        if node.is_goal(goal_state):
            return node.get_path()

        visited.add(tuple(node.state))

        expanded_nodes = expand_node(node)
        for child_node in expanded_nodes:
            if tuple(child_node.state) not in visited:
                queue.append(child_node)

    return None

# Example usage
initial_state = [1, 2, 3, 0, 4, 6, 7, 5, 8]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

path = bfs(initial_state, goal_state)
if path is not None:
    print("Path found:", path)
else:
    print("Path not found.")
