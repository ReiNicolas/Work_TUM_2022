import torch
import torchvision
import torch.nn as nn
import torch.optim as optim
from torch import utils
from torchvision import datasets, transforms
from os.path import exists

from Modelo import Model

Path='Work_TUM_2022\K_I_Trainieren_2\Model_Trained.pth'

Path_Exists=exists(Path)

K_I=Model()

K_I.train()

if(Path_Exists):
    K_I.load_state_dict(torch.load(Path))


Transformation_Used=transforms.ToTensor()

Data_Train_Set=torchvision.datasets.CIFAR10(root='./data',train=True,download=True,transform=Transformation_Used)

Batch_size=100

Data_Train_Loader=utils.data.DataLoader(Data_Train_Set,batch_size=Batch_size,shuffle=True)


Criterion=nn.CrossEntropyLoss()
Optimizer=optim.SGD(K_I.parameters(),lr=0.01,momentum=0.9)

for epoch in range(200 ):


    for i,data in enumerate(Data_Train_Loader,0):
        Images,Labels =data

        Optimizer.zero_grad()
        Output=K_I(Images)
        #for i in range(0,Batch_size):
        #    Labels[i]=1
        Loss=Criterion(Output,Labels)
        Loss.backward()
        Optimizer.step()
        ##print(K_I.Convolution1.weight.grad)
        ##print(K_I.Linear4.weight.grad)
        ##break
            

torch.save(K_I.state_dict(),Path)