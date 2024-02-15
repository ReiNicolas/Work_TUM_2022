import torch
torch.cuda.device(0)
print(torch.cuda.is_available())