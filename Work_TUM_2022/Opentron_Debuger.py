import opentrons.simulate
import os
import sys
sys.path.append(os.getcwd())

file_path='C:\\Users\\nicol\\OneDrive\\Documents\\CC++\\workspaceCC++\\Work_TUM_2022\\DNAOrigame_Auto\\Pipeting\\Pipeting.py'
file_name='Pipeting.py'
file=open(file_path)

runlog=opentrons.simulate.simulate(file,file_name)
for text in runlog[0]:
    print(text['payload']['text'])