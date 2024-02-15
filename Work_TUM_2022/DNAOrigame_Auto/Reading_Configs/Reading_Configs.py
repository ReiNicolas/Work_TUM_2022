import sys
import os

sys.path.append(os.getcwd())


from Work_TUM_2022.DNAOrigame_Auto.Global_Variables import *
from Work_TUM_2022.DNAOrigame_Auto.Global_Functions import *


def Reading_Configs(File_Name):

    with open(File_Name) as F:
        String_From_File=F.readline()
        Ratio=float(F.readline())
        V_F=float(F.readline())
        Initial_Temperature=int(F.readline())
        Final_Temperature=int(F.readline())
        F.close()

    #This one is diferent from the one on Visual_Matrix becase it is grid-colum-row and that one is grid-row-colum
    Pipeting_Field=[[[Inv_Binary_TOF(String_From_File[Grid_Size*i+Number_Of_Colums*p+u]) for p in range(0,Number_Of_Rows)] for u in range(0,Number_Of_Colums)] for i in range(0,Number_Of_Grids)]

    return Pipeting_Field, Ratio, V_F, Initial_Temperature, Final_Temperature

    #List_Of_Tuples=[]
    

    #Here we iterate true the grid's to find sequences of points were
#    for i in range(0,Number_Of_Grids):
 #       for u in range(0,Number_Of_Colums):
  #          Start_Of_Sequence=NULL
   #         End_Of_Sequece=NULL
    #        In_A_Sequence=False
     #       for p in range(0,Number_Of_Rows):
      #          if(In_A_Sequence==False and Pipeting_Field[i][u][p]==True):
       #             Start_Of_Sequence=p
        #            In_A_Sequence=True
         #       if(In_A_Sequence==True and p==Number_Of_Rows):
          #          End_Of_Sequece=p
           #         List_Of_Tuples.append((i,u,Start_Of_Sequence,End_Of_Sequece))
            #        In_A_Sequence=False
             #   elif(In_A_Sequence==True and Pipeting_Field[i][u][p]==False):
              #      End_Of_Sequece=p-1
               #     List_Of_Tuples.append((i,u,Start_Of_Sequence,End_Of_Sequece))
                #    In_A_Sequence=False
    
    #return List_Of_Tuples