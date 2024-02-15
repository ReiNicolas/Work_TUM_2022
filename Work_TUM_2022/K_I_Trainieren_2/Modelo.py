import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        Number_Of_Images=3*1
        Number_Of_Filters1=8
        Kernel_Size1=6
        Number_Of_Filters2=6
        Kernel_Size2=8

        Neurons_Layer1=50
        Neurons_Layer2=50
        Neurons_Layer3=20
        Neurons_Layer_Out=10

        self.Convolution1=nn.Conv2d(Number_Of_Images,Number_Of_Filters1,Kernel_Size1)
        self.Convolution2=nn.Conv2d(Number_Of_Filters1,Number_Of_Filters2,Kernel_Size2)

        Max_Pool_Kernel=2
        self.Pool=nn.MaxPool2d(Max_Pool_Kernel,Max_Pool_Kernel)
    
        Neurons_After_Convolutions=Number_Of_Filters2*Kernel_Size2**2

        self.Linear1=nn.Linear(54,Neurons_Layer1)
        self.Linear2=nn.Linear(Neurons_Layer1,Neurons_Layer2)
        self.Linear3=nn.Linear(Neurons_Layer2,Neurons_Layer3)
        self.Linear4=nn.Linear(Neurons_Layer3,Neurons_Layer_Out)

    def forward(self,Input):
        After_Convolution1=self.Convolution1(Input)
        #print(After_Convolution1.size())
        After_MaxPool1=self.Pool(After_Convolution1)
        #print(After_MaxPool1.size())
        After_Convolution2=self.Convolution2(After_MaxPool1)
        #print(After_Convolution2.size())
        After_MaxPool2=self.Pool(After_Convolution2)
        #print(After_MaxPool2.size())


        Neurons_Input=torch.flatten(After_MaxPool2,1)
        Neurons_1=F.relu(self.Linear1(Neurons_Input))
        ##print(Neurons_1.size())
        Neurons_2=F.relu(self.Linear2(Neurons_1))
        Neurons_3=F.relu(self.Linear3(Neurons_2))
        ##print(Neurons_3)
        Neurons_Out=self.Linear4(Neurons_3)
        #print(Neurons_Out)

        ##mode=True if training and mode=False if predicting
        mode=self.training
        if(mode):
            ##Going to use cross entropy and that aplies log_softmax by itself.
            Output=Neurons_Out
        else:
            Output=torch.argmax(Neurons_Out,dim=1)

        return Output