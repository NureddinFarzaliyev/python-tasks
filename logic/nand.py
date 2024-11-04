class MatrixCalculator:

  def __init__(self, arr):
    self.arr = arr

  def printAnd(self):
    print("And Table for Given Matrix:")
    for i in self.arr:
      res = i[0] and i[1]
      print(str(i[0]) + str(i[1]) + " -> " + str(res == True))

  def printNand(self):
    print("Nand Table for Given Matrix:")
    for i in self.arr:
      res = i[0] and i[1]
      print(str(i[0]) + str(i[1]) + " -> " + str(res != True))
    
  def printBoth(self):
    print("and              nand")
    print("-------------------------")
    for i in self.arr:
      res = i[0] and i[1]
      print(str(i[0]) + str(i[1]) + " -> " + str(res == True) + " " + str(i[0]) + str(i[1]) + " -> " + str(res != True))


arr1 = MatrixCalculator([[0, 0], [0, 1], [1, 0], [1, 1]])
arr2 = MatrixCalculator([[1, 1], [1, 1], [1, 1], [0, 0]])
