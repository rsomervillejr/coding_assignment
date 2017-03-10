#wild forest
#
#approach
#1. read file of 1st param into dictionary
#2. use the 2 child nodes from the 2nd param to recursively build 2 stacks to represent all ancestors
#3. for the smallest stack, starting with the lowest node, check for the existence of node in other stack until match is found (n*2 complexity)
#4. return match if found
#----------
#solution 1
#----------
import sys
def build_lineage(node,tree):
    lineage = []
    lineage.append(node)
    parent = tree[node]
    #print 'base node: %s parent: %s' % (node, parent)
    while parent != 'root':
        #print 'parent of: %s is: %s' % (parent, tree[parent])
        lineage.append(parent)
        parent = tree[parent]
    return lineage

if __name__ == '__main__':
#    main()
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
    node1_lineage = build_lineage(related_node1,tree)
    node2_lineage = build_lineage(related_node2,tree)
    #next line chooses shortest list to scan for match
    if len(node1_lineage) > len(node2_lineage):
        for child_node1 in node1_lineage:
            for child_node2 in node2_lineage:
                print 'child1: %s child2: %s' % (child_node1, child_node2)
                if child_node1 == child_node2:
                    print 'common ancestor: %s' % child_node1
                    exit(0) #successfully found common ancestor, so exit
    else:
        for child_node2 in node2_lineage:
            for child_node1 in node1_lineage:
                print 'child1: %s child2: %s' % (child_node1, child_node2)
                if child_node1 == child_node2:
                    print 'common ancestor: %s' % child_node1
                    exit(0) #successfully found common ancestor, so exit

    print 'no common ancestors for: %s and %s' % (related_node1,related_node2)
    exit(1) # return error in the case of no common ancestor
