from opentrons import protocol_api
import opentrons
import sys
import os
import json

sys.path.append(os.getcwd())

from Work_TUM_2022.DNAOrigame_Auto.Global_Variables import *
from Work_TUM_2022.DNAOrigame_Auto.Pipeting.Pipeting_Functions import *
from Work_TUM_2022.DNAOrigame_Auto.Reading_Configs.Reading_Configs import *


# metadata
metadata = {
    'protocolName': 'My Protocol',
    'author': 'Nicolas Reinaldet Eichenauer <email@address.com>',
    'description': 'Protocol to automate the process of doing DNA origami',
    'apiLevel': '2.0' 
}

def run(protocol: protocol_api.ProtocolContext):
    ##Plataform
    Holder_Path='Work_TUM_2022\\DNAOrigame_Auto\\Pipeting\\biotech_tuberack.json'
    DNA_Bioracks_Name='biorad_96_wellplate_200ul_pcr'
    Tipracks='geb_96_tiprack_10ul'
    Thermocycler_String='thermocycler'
    Plataform_Thermocycler_String='opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap'
    with open(Holder_Path) as Holder_File:
        from opentrons.simulate  import get_protocol_api
        Protocol=get_protocol_api('2.0')
        Holder_Definition=json.load(Holder_File)
        Holder=Protocol.load_labware_from_definition(Holder_Definition,8)
        Holder_File.close()

    DNA_ST_well_1=protocol.load_labware(DNA_Bioracks_Name,1)
    DNA_ST_well_2=protocol.load_labware(DNA_Bioracks_Name,2)
    DNA_ST_well_3=protocol.load_labware(DNA_Bioracks_Name,3)
    DNA_ST_Wells=[DNA_ST_well_1,DNA_ST_well_2,DNA_ST_well_3]

    Tiprack_1=protocol.load_labware(Tipracks,4)
    Tiprack_2=protocol.load_labware(Tipracks,5)
    Tiprack_3=protocol.load_labware(Tipracks,6)
    Tiprack_4=protocol.load_labware(Tipracks,8)
    Tipracks_Vec=[Tiprack_1,Tiprack_2,Tiprack_3,Tiprack_4]

    Thermocycler=protocol.load_module(Thermocycler_String)
    Plataform_Thermocycler=Thermocycler.load_labware(Plataform_Thermocycler_String)
    
    Right=protocol.load_instrument('p10_single','right',tip_racks=Tipracks_Vec)
    Left=protocol.load_instrument('p10_multi','left',tip_racks=Tipracks_Vec)

    Heating=True

    Pipeting_Field, Scafold_Staple_Ratio, V_F, Initial_Temperature,Final_Temperature=Reading_Configs("Folder_Text.txt")

    N=0
  
    DNAStaple_Mixing("Folder_Text.txt",Right,Left,Holder,DNA_ST_Wells)

    if(Heating==True):
        V_Dilution,V_Staples_D,V_Scafold,V_Buffer,V_Dilution,V_Staples=Pipeting_Values(Pipeting_Field=Pipeting_Field,Ratio=Scafold_Staple_Ratio,V_F=V_F)
       
        #Below we dilute the staples in the D1 of holder and put the dilution on the E1 ( final mixture )
        Right.pick_up_tip()
        Right.transfer(V_Staples,Holder["F2"],Holder["D1"],new_tip="never")
        Right.transfer(V_Dilution,Holder["C1"],Holder["D1"],new_tip="never")
        #The numbers on mix are made so it will "rotate" at least 35*V_Staples uL of volume
        Right.mix(Max(7,int(35*V_Staples/Right.max_volume)+1),Min(5*V_Staples,Right.max_volume))
        Right.transfer(V_Staples_D,Holder["D1"],Holder["E1"],new_tip="never")
        Right.drop_tip()

        #Below we put the staple and the buffer into the E1 tube ( final mixture )
        Right.transfer(V_Scafold,Holder["A1"],Holder["E1"],new_tip="always")
        Right.pick_up_tip()
        Right.transfer(V_Buffer,Holder["B1"],Holder["E1"],new_tip="never")
        #Same as line 69, the numbers on mix are made so it will "rotate" at least 35*V_Staples ul of volume ( V_Staple is more or less the unity of our transferances ) 
        Right.mix(Max(7,int(35*V_Staples/Right.max_volume)+1),Min(5*V_Staples,Right.max_volume))

        #Below we put our final mixture on the opentrons thermocycler and turn the thermocycler

        Thermocycler.open_lid()
        Right.transfer(V_F,Holder["E1"],Plataform_Thermocycler["D6"],new_tip="never")
        protocol.home()
        Thermocycler.close_lid()
        
        Thermocycler.set_block_temperature(temperature=Min(99,Initial_Temperature+5),hold_time_seconds=0,hold_time_minutes=15,block_max_volume=V_F)
        Thermocycler.set_lid_temperature(105)
        i=Initial_Temperature
        while(i>=Final_Temperature):
            Thermocycler.set_block_temperature(i,hold_time_seconds=0,hold_time_minutes=60,block_max_volume=V_F)
            i=i-1
        Thermocycler.set_block_temperature(4)
        Thermocycler.set_lid_temperature(20)