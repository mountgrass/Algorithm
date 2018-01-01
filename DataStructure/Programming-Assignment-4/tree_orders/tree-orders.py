# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
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

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if self.n ==0:
      return self.result

    stack = []
    stack.append(0)
    while stack:
      currentElem = stack[-1]
      stack.pop(-1)
      #print('currentElem {0}'.format(currentElem))
      self.result.append(self.key[currentElem])
      if self.right[currentElem]!=-1:
        stack.append(self.right[currentElem])
      if self.left[currentElem]!=-1:
        stack.append(self.left[currentElem])
                
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if self.n ==0:
      return self.result

    stack = []
    stack.append(0)
    stack2 = []
      
    while stack:
        currentElem = stack[-1]
        stack.pop(-1)
        stack2.append(self.key[currentElem])

        if self.left[currentElem]!=-1:
          stack.append(self.left[currentElem])
          
        if self.right[currentElem]!=-1:
          stack.append(self.right[currentElem]) 

    self.result = list(reversed(stack2))
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
