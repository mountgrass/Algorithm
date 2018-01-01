#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Tree:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if self.n ==0:
      return self.result

    stack = []
    current = 0
    while True:
      if current!=-1:
        stack.append(current)
        current = self.left[current]
      else:
        if stack:
          current = stack.pop()
          self.result.append(self.key[current])
          current = self.right[current]
        else:
          break
    
    return self.result

  def IsBinarySearchTree(self):
    # Implement correct algorithm here
    inOrderArray = self.inOrder()
    #print(inOrderArray)
    for i in range(0, len(inOrderArray)-1):
      if inOrderArray[i] > inOrderArray[i+1]:
        return False
    return True

def main():
  #nodes = int(sys.stdin.readline().strip())
  #tree = []
  #for i in range(nodes):
  #  tree.append(list(map(int, sys.stdin.readline().strip().split())))

  tree = Tree()
  tree.read()
  	
  if tree.IsBinarySearchTree():
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
