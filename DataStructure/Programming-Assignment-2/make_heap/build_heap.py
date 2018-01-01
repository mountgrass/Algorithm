# python3
import math

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def ReadTestData(self):
    f = open(r"tests\04.t","r")
    n = int(f.readline())
    line = f.readline()
    self._data = [int(x) for x in line.split()]

    print(n, len(self._data))
    f.close()
    
  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def SiftDown(self,i):
    maxIndex = i
    l = 2*i+1
    if l < len(self._data) and self._data[l] < self._data[maxIndex]:
      maxIndex = l
    r = 2*i+2
    if r < len(self._data) and self._data[r] < self._data[maxIndex]:
      maxIndex = r

    #print(i,l,r, maxIndex)
    if i!=maxIndex:
      self._data[i], self._data[maxIndex] = self._data[maxIndex], self._data[i]
      self._swaps.append( (i, maxIndex) )
      self.SiftDown(maxIndex)

  def CompareAnswer(self):
    f = open(r"tests\04.a","r")
    n = int(f.readline())
    i = 0
    #print(n, len(self._swaps))
    for line in f: # read rest of lines
      array=[]
      array.append([int(x) for x in line.split()])
      #print(array)
      j,k = array[0][0],array[0][1]
      (tJ,tK) = self._swaps[i]
      if j!=tJ or k!=tK:
        print('Error')
      i+=1
    f.close()
    
  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    #for i in range(len(self._data)):
    #  for j in range(i + 1, len(self._data)):
    #    if self._data[i] > self._data[j]:
    #      self._swaps.append((i, j))
    #      self._data[i], self._data[j] = self._data[j], self._data[i]
    n = len(self._data)
    if n < 2:
      return
    
    for i in range( int(n/2)-1, -1, -1 ):
      #print(i)
      self.SiftDown(i)
    

  def Solve(self):
    self.ReadData()
    #self.ReadTestData()
    self.GenerateSwaps()
    self.WriteResponse()
    #self.CompareAnswer()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
