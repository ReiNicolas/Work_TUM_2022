import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        Size_Layer_In=784
        Size_Layer_H1=77
        Size_Layer_H2=20
        Size_Layer_H3=11
        Size_Layer_Out=10

        self.conv1=nn.Linear(Size_Layer_In,Size_Layer_H1)
        self.conv2=nn.Linear(Size_Layer_H1,Size_Layer_H2)
        self.conv3=nn.Linear(Size_Layer_H2,Size_Layer_H3)
        self.conv4=nn.Linear(Size_Layer_H3,Size_Layer_Out)
    
    def forward(self,Data_In,Training=False):
        Neurons_H1=F.relu(self.conv1(Data_In))
        Neurons_H2=F.relu(self.conv2(Neurons_H1))
        Neurons_H3=F.relu(self.conv3(Neurons_H2))
        Neurons_Out=F.relu(self.conv4(Neurons_H3))
        
        SoftMax=nn.Softmax()

        Data_Out=SoftMax(Neurons_Out)

        return Data_Out

