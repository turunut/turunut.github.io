import numpy as np

import objCT
import objRotator

class Material:
  def __init__(self):
    self.rotator = objRotator.NOTRotator()
    self.CT      = None
      
  def read(self, lines):
    for iline, line in enumerate(lines):
        line = line.lower().split(); line.append("")
        #display(line)
    
        if line[0] == "ct:":
            self.CT = objCT.CTFactory(line[1])
            self.CT.read(lines[iline:], line)

        if line[0].lower() == "rotation:":
            vecRot = np.array([float(num) for num in line[1:-1]])
            self.rotator = objRotator.RotatorFactory(vecRot)
            
    return self.CT.check()

  def getCT_3D(self, C, i):      
    return [ self.CT.compute3D(C), self.rotator.Loc2Glo(self.CT.compute3D(C)) ][i]

  def getCT_PS(self, C, i):      
    return [ self.CT.computePS(C), self.rotator.Loc2Glo(self.CT.computePS(C)) ][i]



class Laminate(Material):
  def __init__(self):
    self.layers = []
      
  def read(self, lines):
    for iline, line in enumerate(lines):
        line = line.lower().split(); line.append("")
    
        if (line[0] == "begin") and (line[1] == "layer"):
          mat = objMaterial.Material()
          flag = mat.read(lines)

          self.layers.append(mat)
            
    return self.CT.check()

  def getCT_3D(self, C, i):      
    return [ self.CT.compute3D(C), self.rotator.Loc2Glo(self.CT.compute3D(C)) ][i]

  def getCT_PS(self, C, i):      
    return [ self.CT.computePS(C), self.rotator.Loc2Glo(self.CT.computePS(C)) ][i]