from pyscript import document
import numpy as np
import objMaterial
import objCT
import objRotator

def translate_english(event):
    E11text = document.querySelector("#E11")
    G12text = document.querySelector("#G12")
    n12text = document.querySelector("#n12")
    E11 = float(E11text.value)
    G12 = float(G12text.value)
    n12 = float(n12text.value)

    output_div = document.querySelector("#output")
    output_div.innerText = "Hello world2!" + str(E11)
    #display("Hello world2!")

    display(get_type("typeCTselector"))

def get_type(id):
    typetext = document.querySelector("#"+str(id))
    type = str(typetext.value)
    return type

def typeCTevent(event):
    display("holahola")

def CTcompute(event):
    textfield = document.querySelector("#CTfield")
    lines = textfield.value.split("\n")

    mat = objMaterial.Material()
    flag = mat.read(lines)
    
    #display(CT.C)
    if flag:
      CT3D = np.zeros((6,6));      CTPS = np.zeros((3,3))
        
      output_div = document.querySelector("#CT_3D")
      printArray(output_div, mat.getCT_3D(CT3D, 0) )
      output_div = document.querySelector("#CT_3D_rot")
      printArray(output_div, mat.getCT_3D(CT3D, 1) )
        
      output_div = document.querySelector("#CT_PS")
      printArray(output_div, mat.getCT_PS(CTPS, 0) )
      output_div = document.querySelector("#CT_PS_rot")
      printArray(output_div, mat.getCT_PS(CTPS, 1) )

def printArray(place, array):
    for irow in range(0, array.shape[0]):
      if irow == 0:        
        place.innerText  = np.array_str(array[irow,:], precision=2, suppress_small=True)[1:-1] + '\n'
      else:
        place.innerText += np.array_str(array[irow,:], precision=2, suppress_small=True)[1:-1] + '\n'







    