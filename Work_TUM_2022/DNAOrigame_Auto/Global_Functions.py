from distutils.log import error
from xml.etree.ElementTree import PI

from Work_TUM_2022.DNAOrigame_Auto.Global_Variables import C_Scafold, C_Staple, Number_Of_Colums, Number_Of_Grids, Number_Of_Rows

def Binary_TOF(bool):
    if(bool):
        return '1'
    else:
        return '0'


def Inv_Binary_TOF(char):
    if(char=='1'):
        return True
    elif(char=='0'):
        return False
    else:
        raise NameError('Function Inv_Binary_TOF requires a 0 or 1 char')

def Max(A,B):
    if(A>B):
        return A
    else:
        return B

def Min(A,B):
    if(A<B):
        return A
    else:
        return B

def Count_Staples(Pipeting_Field):
    N=0
    for i in range(0,Number_Of_Grids):
        for p in range(0,Number_Of_Colums):
            for u in range(0,Number_Of_Rows):
                if(Pipeting_Field[i][p][u]==True):
                    N=N+1
    
    return N

def Pipeting_Values(Pipeting_Field,Ratio,V_F):
    #Pipeting_Field, Ratio, V_F, Initial_Temperature, Final_Temperature=Reading_Configs(File_Name)
    N=Count_Staples(Pipeting_Field)
    Alpha=Max(1,V_F/10)
    V_Staples_D=8*Alpha
    V_Scafold=1*Alpha
    V_Buffer=1*Alpha

    V_Dilution=C_Staple*V_Staples_D/(C_Scafold*Ratio*N)-1
    V_Staples=Alpha

    return V_Dilution,V_Staples_D,V_Scafold,V_Buffer, V_Dilution, V_Staples