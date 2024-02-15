from Work_TUM_2022.DNAOrigame_Auto.Global_Variables import *
from Work_TUM_2022.DNAOrigame_Auto.Reading_Configs.Reading_Configs import *

##Take as input a string that has the local Path to the json fie with the labware definition and a int that represents the position. Returns the Labware to be used on the code ( should more or less replace the load() function for custon labware.
def Load_Custon_Labware(Path,Place):
    #Import localy the libraries needed for this and name the Protocol librarie for better use latter.
    from opentrons.execute import get_protocol_api
    import json
    Protocol=get_protocol_api('2.0')
    
    #In order open the file, load it on the code and make a Labware object out of it.
    Labware_File=open(Path)
    Labware_Def=json.load(Labware_File)
    Return_Labware=Protocol.load_labware_from_definition(Labware_Def,Place)
    return Return_Labware

def Create_Well(Racks,i,u,p):
    Dictionary_Alphabet={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J'}
    Row=Dictionary_Alphabet[p]
    Well_Position=Row+str(u+1)
    Well=Racks[i].wells(Well_Position)
    return Well

def DNAStaple_Mixing(File_Name,Right,Left,Holder,Wells):
    Pipeting_Field, Scafold_Staple_Ratio, V_Final, Initial_Temperature,Final_Temperature=Reading_Configs(File_Name)
  
    for i in range(0,Number_Of_Grids):
        for u in range(0,Number_Of_Colums):
            All_Rows_Used=True
            for p in range(0,Number_Of_Rows):
                if(False==Pipeting_Field[i][u][p]):
                    All_Rows_Used=False
            if(All_Rows_Used==True):
                Left.transfer(1,Wells[i].columns(str(u+1)),Holder.columns('2'),new_tip='always')
            else:
                for p in range(0,Number_Of_Rows):
                    if(Pipeting_Field[i][u][p]==True):
                        Right.transfer(1,Create_Well(Wells,i,u,p),Holder.well('B1'),new_tip='always')
    Right.pick_up_tip()
    Positions_Holder=['A2',"L2","B2","K2","C2","J2","D2","I2","E2","H2","F2","G2","A2"]
    for i in range(0,3):
        for u in range(0,12):
            Right.transfer(10,Holder.well(Positions_Holder[u]),Holder.well(Positions_Holder[u+1]),new_tip='never',mix_before=(3,5))
    Right.drop_tip()