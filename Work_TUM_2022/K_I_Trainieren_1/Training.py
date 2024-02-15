import torch
import torch.nn as nn
import torch.optim as optim
from torch import utils
from torchvision import datasets, transforms
from os.path import exists

from Modelo import Model

Transformation_Used=transforms.ToTensor()

Data_Train_Set=datasets.MNIST(root='data',train=True,download=True,transform=Transformation_Used)

Data_Train_Loader_Size=100

Data_Train_Loader=utils.data.DataLoader(Data_Train_Set,batch_size=Data_Train_Loader_Size,shuffle=True)

Loss_Function=nn.MSELoss()

Path='Work_TUM_2022\K_I_Trainieren_1\Model_Trained.pth'

Path_Exists=exists(Path)

K_I=Model()


if(Path_Exists):
    K_I.load_state_dict(torch.load(Path))




Optimizer=optim.SGD(K_I.parameters(),lr=0.1,momentum=0.9)

for epoch in range(5):

    running_loss=0.0
    for i,data in enumerate(Data_Train_Loader):
        Inputs_Sqr, Labels_Int=data

        Inputs_Vec=Inputs_Sqr.view(Data_Train_Loader_Size,1,784)

        Labels_Vec=torch.zeros([Data_Train_Loader_Size,1,10])
        
        for i in range(0,Data_Train_Loader_Size):
            Labels_Vec[i][0][Labels_Int[i]]=1

        Optimizer.zero_grad()
        Outputs=K_I(Inputs_Vec)
        
        
        loss=Loss_Function(Outputs,Labels_Vec)
        loss.backward()
        Optimizer.step()

        if(loss<=4*10**-2):
            break


torch.save(K_I.state_dict(),Path)