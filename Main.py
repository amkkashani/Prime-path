

intialNodes = [0]
vertices = [(0,1),(0,2),(3,1),(1,3),(2,3),(3,4)]
verticesDictionary = {}
endNodes = [4]
numberOfTheNodes = 5

stack = []
results = set()

def main():
    setupGraph()
    print(verticesDictionary)
    DFS(0)
    print(results)
    # for i in range(numberOfTheNodes):
    #     DFS(i)


#this code is not popular dfs :)
#its custom dfs for finding all the ways
def DFS(startIndex):
    startNode = path()
    _,startNode = startNode.addNodeToPath(startIndex)
    stack.append(startNode)

    while len(stack)!= 0:
        currentNode = stack.pop()
        if currentNode.passed[-1] in verticesDictionary:
            canBeTheEndNod = False
            for nextNode in verticesDictionary[currentNode.passed[-1]]:
                #todo check conditions
                cond , newPath = currentNode.addNodeToPath(nextNode)
                if cond:
                    stack.append(newPath)
                else:
                    if newPath !=None:
                        results.add(newPath)
                    else:
                        canBeTheEndNod = True

            if currentNode.haveChild == False and canBeTheEndNod:
                results.add(currentNode)
        else:
            # in this case you are in end of path
            results.add(currentNode)

def setupGraph():
    for tup in vertices:
        if tup[0] in verticesDictionary:
            verticesDictionary[tup[0]].append(tup[1])
        else:
            verticesDictionary[tup[0]] = [tup[1]]


class path:
    def __init__(self):
        self.passed = []
        self.collection = set()
        self.haveChild = False # this field show us that the Node have bigger child path or not


    def addNodeToPath(self,nodeNumber):
        if nodeNumber in self.collection:
            if self.passed[0] == nodeNumber:
                newPath = path()
                newPath.passed = self.passed.copy()
                newPath.collection = self.collection.copy()
                newPath.passed.append(nodeNumber)
                newPath.collection.add(nodeNumber)
                self.haveChild = True
                return False , newPath
            else:
                return False , None
        else:
            newPath = path()
            newPath.passed = self.passed.copy()
            newPath.collection = self.collection.copy()
            newPath.passed.append(nodeNumber)
            newPath.collection.add(nodeNumber)
            self.haveChild = True
            return True, newPath




if __name__ == '__main__':
    main()