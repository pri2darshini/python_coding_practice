class Node:
    def __init__(self, item):
        self.item = item
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # Insert an element into the tree
    def insert(self, item):
        if self.root == None:
            self.root = Node(item)
            return

        currentNode = self.root
        prev = None
        while (currentNode != None):
            prev = currentNode
            if(currentNode.item < item):
                currentNode = currentNode.right
            elif(currentNode.item >= item):
                currentNode = currentNode.left

        if(prev.item < item):
            prev.right = Node(item)
        else:
            prev.left = Node(item)

        return

    # Display the contents of the tree
    def showTree(self, node):
        if(node == None):
            return
        self.showTree(node.left)
        print(node.item)
        self.showTree(node.right)

    def getSortedArray(self, node):
        elementList = []
        if(node==None):
            return elementList
        elementList+=self.getSortedArray(node.left)
        elementList.append(node.item)
        elementList+=self.getSortedArray(node.right)
        return elementList


    # Return the number of elements in the tree
    def getNodeCount(self, node):
        if(node == None):
            return 0
        return (self.getNodeCount(node.left) + self.getNodeCount(node.right) + 1)

    # Check for existence of an element in the tree
    def isExists(self, key):
        node = self.root
        while(node != None):
            if(node.item == key):
                return True
            elif(node.item < key):
                node = node.right
            else:
                node = node.left
        return False

    # Calculate the height of the tree.
    def getHeight(self, node):
        if(node == None):
            return 0
        lHeight = self.getHeight(node.left)
        rHeight = self.getHeight(node.right)

        if(lHeight > rHeight):
            return lHeight + 1
        else:
            return rHeight + 1

    # Get minimum value in the tree.
    def getMin(self, root):
        node = root
        if(node == None):
            return None
        while (node.left != None):
            node = node.left
        return node.item

    # Get max value in the tree.
    def getMax(self, root):
        node = root
        if(node == None):
            return None
        while (node.right != None):
            node = node.right
        return node.item

    # Delete value from tree.
    def deleteValue(self, key, root):
        if(root == None):
            return None

        node = root
        while(node.item != None):
            if(node.item == key):
                item = self.getMax(node.left)
                if(item == None):
                    item = self.getMin(node.right)
                if(item==None):
                    node.item = item
                    return self.deleteValue(item, node.right)
                else:
                    node.item = item
                    return self.deleteValue(item, node.left)
                
            elif(node.item < key):
                node = node.right
            else:
                node = node.left
            prev = node

        return


    def inorderIterative(self, node):

        if(node==None):
            return None
        
        if(node.left==node.right==None):
            return node
        
        fakeStack = []
        inOrder = []
        curr = node.left
        fakeStack.append(node)
        while(len(fakeStack)>0):
            if(curr==None):
                curr = fakeStack.pop()
                inOrder.append(curr)
                curr = curr.right
                 
            if(curr!=None):
                fakeStack.append(curr)
                prev=curr
                curr = curr.left

        return inOrder
        
        
        


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
    nodes = myTree.inorderIterative(myTree.root)
    for node in nodes:
        print(node.item)
    print("#############################################")
    print("MY TREE IS")
    myTree.showTree(myTree.root)
    print("#############################################")
    print("NO OF NODES IS :")
    print(myTree.getNodeCount(myTree.root))
    print("#############################################")
    print("DOES THIS NODE EXIST IN MY TREE")
    print(myTree.isExists(12))
    print(myTree.isExists(1))
    print("#############################################")
    print("THE MINIMUM & MAXIMUM VALUE IN THE TREE")
    print(myTree.getHeight(None))
    print(myTree.getMin(myTree.root))
    print(myTree.getMax(myTree.root))
    print("#############################################")
    print("MY TREE AFTER DELETING A NODE")
    myTree.deleteValue(233, myTree.root)
    myTree.showTree(myTree.root)
    print("#############################################")
    print("CREATE A NEW TREE")
    newTree = Tree()
    newTree.insert(1)
    newTree.insert(2)
    newTree.insert(3)
    newTree.insert(4)
    print("---------")
    print(newTree.getSortedArray(newTree.root))
    newTree.deleteValue(1, newTree.root)
    print(newTree.showTree(newTree.root))
