import torch
import torch.nn as nn
import torch.nn.functional as F

from Work_TUM_2022.K_I_Trainieren_2.Modelo import Model

class Modelo(nn.Module):
    def __init__(self):
        super(Modelo,self).__init__()
        