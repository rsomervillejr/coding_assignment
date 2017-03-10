#wild forest
#
#approach
#1. read file of 1st param into dictionary
#2. use the 1st child node from the 2nd param to recursively build a stack to represent all ancestors
#3. for the 2nd child node from the 2nd param, check for the existence of each node in stack of 1st child node (closer to n log n complexity)
#4. return match if found
#----------
#solution 2
#----------
import sys

tree_file = sys.argv[1]
related_node1,related_node2 = sys.argv[2].split()
tree={}
pair=[]
with open(tree_file) as fp:
    for line in fp:
        pair = line.split()
        if len(pair) == 2:
            child,ancestor = pair
        else:
            child = pair[0]
            ancestor = 'root'
        tree[child] = ancestor
lineage1 = []
lineage1.append(related_node1)
parent = tree[related_node1]
#print 'base node: %s parent: %s' % (related_node1, parent)
while parent != 'root':
    #print 'parent of: %s is: %s' % (parent, tree[parent])
    lineage1.append(parent)
    parent = tree[parent]
print 'lineage1:' + str(lineage1)

parent = tree[related_node2]
#print 'base node: %s parent: %s' % (related_node1, parent)
while parent != 'root':
    #print 'parent of: %s is: %s' % (parent, tree[parent])
    for child_node1 in lineage1:
        #print 'child1: %s child2: %s' % (child_node1, child_node2)
        if child_node1 == parent:
            print 'common ancestor: %s' % child_node1
            exit(0) #successfully found common ancestor
    parent = tree[parent]
print 'no common ancestors for: %s and %s' % (related_node1,related_node2)
exit(1) # return error in the case for no common ancestor
