
from math import inf

class MTreeNode:
    def __init__(self, position, direction, radius, creator=0):
        self.position = position # Vector - position of node in local space
        self.direction = direction # Vector - direction of node in local space
        self.radius = radius # float - radius of node
        self.children = [] # list of TreeNode - the extremities of the node. First child is the continuity of the branch
        self.creator = creator # int - the id of the NodeFunction that created the node
        self.growth = 0 # float - when growing nodes it is useful to know how much they should grow. this parameter gives the length a node has grown since grow was called.
        self.growth_goal = 0 # float - How much the node should be grown.
        self.growth_radius = 0 # float - The radius of the node when it first started growing
        self.can_be_splitted = True # bool - if true the node can be splitted (can have more than 1 children)

    def get_grow_candidates(self, candidates, creator):
        '''
        recursively populate candidates with leafs of tree if a leaf has the right creator
        returns min and max height of found nodes
        '''
        max_height = -inf # initilizing max and min heights
        min_height = inf

        if len(self.children) == 0: # only extremities can be grown
            if self.creator == creator: # only grow node created by creator
                candidates.append(self)
                max_height = min_height = self.position.z # get height of node
            
        for child in self.children:
            min_h, max_h = child.get_grow_candidates(candidates, creator) # recursivelly call function to children
            min_height = min(min_height, min_h) # min height is now the min between istself and the min height of child
            max_height = max(max_height, max_h) # max height is now the max between istself and the max height of child
        
        return min_height, max_height