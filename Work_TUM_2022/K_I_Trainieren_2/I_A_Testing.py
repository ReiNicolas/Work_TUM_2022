from Modelo import Model
import torchvision
from torchvision import datasets, transforms
import torch
from torch import utils

Path='Work_TUM_2022\K_I_Trainieren_2\Model_Trained.pth'

K_I=Model()
K_I.load_state_dict(torch.load(Path))
K_I.eval()

Transformation_Used=transforms.ToTensor()

Transformation_Used=transforms.ToTensor()

Data_Test_Set=datasets.CIFAR10(root='./data',train=False,download=True,transform=Transformation_Used)

Batch_size=100

Data_Test_Loader=utils.data.DataLoader(Data_Test_Set,batch_size=Batch_size,shuffle=False)

Corrects=0
Avaliated=0

with torch.no_grad():
    for Data in Data_Test_Loader:
        Images, Labels=Data
        Output=K_I(Images)
        Avaliated+=Labels.size(0)
        Corrects+=(Output==Labels).int().sum()
Acuracy_Rate=Corrects/Avaliated
print(Acuracy_Rate)