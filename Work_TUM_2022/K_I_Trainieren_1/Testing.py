from tkinter import Label
import torch
import torch.nn as nn
import torch.optim as optim
from torch import utils
from torchvision import datasets, transforms

from Modelo import Model

Path='Work_TUM_2022\K_I_Trainieren_1\Model_Trained.pth'

K_I=Model()
K_I.load_state_dict(torch.load(Path))

Transformation_Used=transforms.ToTensor()

Data_Test_Set=datasets.MNIST(root='data',train=False,download=True,transform=Transformation_Used)

batch_size=100

Data_Test_Loader=torch.utils.data.DataLoader(Data_Test_Set,batch_size=batch_size,shuffle=False)
Number_Of_Correct_Data_Values=0
Number_Of_Data_Avaliated=0


K_I.eval()

with torch.no_grad():
    for data in Data_Test_Loader:
        Inputs_Sqr,Labels =data

        Inputs_Vec=Inputs_Sqr.view(batch_size,1,784)

        Outputs_RAW=K_I.forward(Inputs_Vec)
        
        Outputs_COOK=torch.argmax(Outputs_RAW,dim=2)

        ##Number_Of_Data_Avaliated+=Labels.size(0)
        ##Number_Of_Correct_Data_Values+=(Outputs_COOK==Labels).sum().item()
        for i in range(0,batch_size):
            Predicate_Value=Outputs_COOK[i]
            Correct_Value=Labels[i].item()
            if(Predicate_Value==Correct_Value):
                Number_Of_Correct_Data_Values+=1
            Number_Of_Data_Avaliated+=1
        
Acuracy_Rate=torch.div(Number_Of_Correct_Data_Values,Number_Of_Data_Avaliated).item()
print(Acuracy_Rate)