from opentrons import protocol_api
import opentrons
import sys
import os
import json

sys.path.append(os.getcwd())

from Work_TUM_2022.DNAOrigame_Auto.Global_Variables import *
from Work_TUM_2022.DNAOrigame_Auto.Pipeting.Pipeting_Functions import *

metadata = {
    'protocolName': 'My Protocol',
    'author': 'Nicolas Reinaldet Eichenauer <email@address.com>',
    'description': 'Protocol to automate the process of doing DNA origami',
    'apiLevel': '2.0' ,
}

def run(protocol: protocol_api.ProtocolContext):
    ##Plataform
    Holder_Path='Work_TUM_2022\\DNAOrigame_Auto\\Pipeting\\biotech_tuberack.json'
    Tipracks='geb_96_tiprack_10ul'

    with open(Holder_Path) as Holder_File:
        from opentrons.simulate  import get_protocol_api
        Protocol_Simul=get_protocol_api('2.0')
        Holder_Definition=json.load(Holder_File)
        Holder=Protocol_Simul.load_labware_from_definition(Holder_Definition,8)
        Holder_File.close()
    Right=protocol.load_instrument('p10_single','right')
    Tiprack_1=protocol.load_labware(Tipracks,4)


    Right.pick_up_tip(Tiprack_1["A1"])

    for i in Holder.wells():
        Right.move_to(i.top())
        if(i==Holder["A1"] or i==Holder["L2"]):
            protocol.pause("If the position is accurate click 'resume")
            Right.move_to(i.bottom())
        protocol.pause("If the position is accurate click 'resume.'")