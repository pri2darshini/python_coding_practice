from tree import *

def catchAnomaly1(node):
    if(node == None):
        return None

    if(node.left==node.right==None):
        return node

    l = curr = node.left
    m = node
    r = node.right

    stack = []
    anomaly = []
    stack.append(m)
    while(len(stack)>0):
        if(curr==None):
            curr = stack.pop()
            m = curr
            l = curr.left
            curr = curr.right
            r = curr

            if(l!=None and l.item>m.item):
                anomaly.append(l)

            if(r!=None and m.item>r.item):
                anomaly.append(r)
        

        if(curr!=None):
            stack.append(curr)
            m = curr
            r = curr.right
            curr = curr.left
            l = curr

            if(l!=None and l.item>m.item):
                anomaly.append(l)

            if(r!=None and m.item>r.item):
                anomaly.append(r)
        
    return anomaly


def catchAnomaly2(node):

    if node==None:
        return None

    if (node.left==node.right==None):
        return node
    
    stack = [node]
    curr = node.left
    sortedNodes = []
    faultyNodes = []
    while(len(stack)>0):
        if(curr==None):
            curr = stack.pop()
            sortedNodes.append(curr)
            curr = curr.right
        
        if(curr!=None):
            stack.append(curr)
            curr = curr.left
        
    for i in range(len(sortedNodes)-1):
        if(sortedNodes[i].item>sortedNodes[i+1].item):
            faultyNodes.append(i)

    if(len(faultyNodes)<2):
        temp = sortedNodes[faultyNodes[0]].item
        sortedNodes[faultyNodes[0]].item = sortedNodes[faultyNodes[0]+1].item
        sortedNodes[faultyNodes[0]+1].item = temp
        return [sortedNodes[faultyNodes[0]], sortedNodes[faultyNodes[0]+1]]
    else: 
        temp = sortedNodes[faultyNodes[0]].item
        sortedNodes[faultyNodes[0]].item = sortedNodes[faultyNodes[1]].item
        sortedNodes[faultyNodes[1]].item = temp
        return [sortedNodes[faultyNodes[0]], sortedNodes[faultyNodes[1]]]

    

if __name__ == "__main__":

    myTree = Tree()
    myTree.insert(10)
    myTree.insert(5)
    myTree.insert(11)
    myTree.insert(233)
    myTree.insert(-4)
    myTree.insert(11)
    myTree.insert(123)
    myTree.insert(77)
    myTree.insert(22)
    myTree.insert(1)

    temp = myTree.root.item
    myTree.root.item = myTree.root.left.item
    myTree.root.left.item = temp

    newTree = Tree()    
    newTree.insert(10)
    newTree.insert(5)
    newTree.insert(11)
    temp = newTree.root.item
    newTree.root.item = newTree.root.left.item
    newTree.root.left.item = temp
    #
    
    nodes = catchAnomaly2(myTree.root)
    #for node in nodes:
        #print(node.item)

    myTree.showTree(myTree.root)
