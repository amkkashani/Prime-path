intialNodes = [0]
vertices = [(0, 1), (0, 2), (3, 1), (1, 3), (2, 3), (3, 4)]
verticesDictionary = {}
endNodes = [4]
numberOfTheNodes = 5

stack = []
results = []


def main():
    setupGraph()
    for i in range(numberOfTheNodes):
        DFS(i)
    removeSubpaths()

    print("prime paths")
    for element in results:
        print(element.passed)

    print("prime path and test path")
    for element in results:
        path = element.passed
        if path[0] in intialNodes and path[-1] in endNodes:
            print(path)


# this code is not popular dfs :)
# its custom dfs for finding all the ways
def removeSubpaths():
    i = 0
    while i < len(results):
        j = 0
        while j < len(results):
            if i >= j:
                j += 1
                continue
            if checkItsSubpath(results[i],
                               results[j]):  # deletion during iterations caueses  the complexity inside this block
                if len(results[i].passed) > len(results[j].passed):
                    results.remove(results[j])
                    if j < i:
                        j -= 1
                        i -= 1
                    else:
                        j -= 1

                else:
                    results.remove(results[i])
                    if i < j:
                        j -= 1
                        i -= 1
                    else:
                        i -= 1
                    break  # we change the main element and must break
            j += 1
        i += 1


def checkItsSubpath(path1, path2):
    listBig = path1.passed
    listLit = path2.passed

    if len(listBig) < len(listLit):
        temp = listLit
        listLit = listBig
        listBig = temp

    for i in range(len(listBig)):
        isSubpath = True
        for j in range(len(listLit)):
            if i + j > len(listBig) - 1 or listBig[i + j] != listLit[j]:
                isSubpath = False
                break
        if isSubpath:
            return True
    return False



def DFS(startIndex):
    startNode = path()
    _, startNode = startNode.addNodeToPath(startIndex)
    stack.append(startNode)

    while len(stack) != 0:
        currentNode = stack.pop()
        if currentNode.passed[-1] in verticesDictionary:
            canBeTheEndNod = False
            for nextNode in verticesDictionary[currentNode.passed[-1]]:
                cond, newPath = currentNode.addNodeToPath(nextNode)
                if cond:
                    stack.append(newPath)
                else:
                    if newPath != None:
                        results.append(newPath)
                    else:
                        canBeTheEndNod = True

            if currentNode.haveChild == False and canBeTheEndNod:
                results.append(currentNode)
        else:
            # in this case you are in end of path
            results.append(currentNode)


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
        self.haveChild = False  # this field show us that the Node have bigger child path or not

    def addNodeToPath(self, nodeNumber):
        if nodeNumber in self.collection:
            if self.passed[0] == nodeNumber:
                newPath = path()
                newPath.passed = self.passed.copy()
                newPath.collection = self.collection.copy()
                newPath.passed.append(nodeNumber)
                newPath.collection.add(nodeNumber)
                self.haveChild = True
                return False, newPath # loop with same node in start and end
            else:
                return False, None # loop (unwanted)
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
