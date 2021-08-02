# Implemented a Struct system similar to the Struct system found in C

class Struct:
  def __init__(self, struct_structure):
    self.struct_structure = {}
    # Key: Variable name
    # Type: Type as definited in ctypes_types.py
