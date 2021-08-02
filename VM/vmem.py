# Virtual Memory Module

class VirtualMemory:
  def __init__(self):
    self.memory = {}
    # Key: 32-bit address 
    # Value: Any C variable/Python object
    self.counter = 1 
    # NOTE: self.counter is an integer, is not possible to use as a key for self.memory
  
  def checkCounter(self):
    # Check if self.counter is correct and fix self.counter if it 
    if bin(self.counter) in self.memory.keys():
      self.counter = 0
      while True:
        self.counter += 1
        if bin(self.counter) not in self.memory.keys():
          break
  
  def set(self, address, value, binaryMode=False):
    if binaryMode:
      self.memory[value] = address
    else:
      self.memory[bin(value)] = address
    if self.counter == address:
      self.counter += 1
    elif self.counter > address:
      self.counter = address
    elif self.counter < address:
      self.counter = address - 1
    self.checkCounter()
  
  def get(self, address, binaryMode=False):
    if binaryMode:
      return self.memory[value]
    else:
      return self.memory[bin(value)]
    if self.counter == address:
      self.counter += 1
    elif self.counter > address:
      self.counter = address
    elif self.counter < address:
      self.counter = address - 1
    self.checkCounter()
    
  def setNew(self, value):
    checkCounter()
    a = self.counter
    self.set(self.counter, value, binaryMode=True)
    return {
      "binary": bin(a),
      "int" : a,
    }
