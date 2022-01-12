from tree import *

def checkPair(firstArray, secondArray, key):
    
    for item in firstArray:
        i = 0
        j = 0
        while (0<=i<len(secondArray) and (j<len(secondArray))):
            j=j+1
            if (item+secondArray[i]==key):
                return True
            elif (item+secondArray[i]<key):
                i = i+1
            else:
                i = i-1

    return False    


if __name__ == "__main__":
    FirstTree = Tree()
    FirstTree.insert(10)
    FirstTree.insert(10)
    FirstTree.insert(5)
    FirstTree.insert(11)
    FirstTree.insert(233)
    FirstTree.insert(-4)
    FirstTree.insert(11)
    FirstTree.insert(123)
    FirstTree.insert(77)
    FirstTree.insert(22)
    FirstTree.insert(1)

    firstArray = FirstTree.getSortedArray(FirstTree.root)

    SecondTree = Tree()
    SecondTree.insert(12)
    SecondTree.insert(8)
    SecondTree.insert(10)
    SecondTree.insert(5)
    SecondTree.insert(4)
    SecondTree.insert(6)
    SecondTree.insert(9)
    
    secondArray = SecondTree.getSortedArray(SecondTree.root)

    print(checkPair(firstArray, secondArray, 243))
