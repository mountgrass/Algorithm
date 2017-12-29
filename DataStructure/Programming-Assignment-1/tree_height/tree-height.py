# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class NodeDepth:
    def __init__(self, key, depth):
        self.key = key
        self.depth = depth
     
    
class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.nodes = []
                for i in range(0,self.n):
                    t = []
                    self.nodes.append(t)
                self.root = -1
        def buildTree(self):
                for i in range(0, self.n):
                    parent = self.parent[i]
                    if parent==-1:
                        self.root = i
                    else:
                        self.nodes[parent].append(i)
                #print(self.nodes)
                            
        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                if len(self.nodes)==0:
                    maxHeight = 0
                    return maxHeight
                    
                traverseQueue = []                    
                traverseQueue.append( NodeDepth(self.root, 0) )
                
                while len(traverseQueue) > 0:
                    currentNode = traverseQueue.pop();
                    childNodes = self.nodes[currentNode.key]
                    if len(childNodes) == 0:
                        if maxHeight < currentNode.depth:
                            maxHeight = currentNode.depth
                        continue
                    for i in range(0, len(childNodes)):
                        traverseQueue.append( NodeDepth(childNodes[i], currentNode.depth+1) )

                return maxHeight+1
                    

def main():
  tree = TreeHeight()
  tree.read()
  tree.buildTree()
  print(tree.compute_height())

threading.Thread(target=main).start()
