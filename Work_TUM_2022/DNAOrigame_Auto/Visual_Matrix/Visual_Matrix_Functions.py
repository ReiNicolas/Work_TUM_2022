import os
import sys
#sys.path.append(os.getcwd())
from Global_Variables import *

def ID_Buttons(Grid,Row,Colum):
    ID=1000+Grid*Grid_Size+Row*Grid_Lenght+Colum
    return ID

def Grid_Of_ID(ID):
    Grid=(ID-1000)//Grid_Size
    return Grid

def Row_Of_ID(ID):
    Row=((ID-1000)-Grid_Size*Grid_Of_ID(ID))//Grid_Lenght
    return Row

def Colum_Of_ID(ID):
    Colum=(ID-1000-Grid_Size*Grid_Of_ID(ID)-Grid_Lenght*Row_Of_ID(ID))
    return Colum