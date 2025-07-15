import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR

train_dataset = datasets.MNIST('../data', train=True, download=True,
                       transform=transform)
test_dataset = datasets.MNIST('../data', train=False,
                       transform=transform)

train_loader = torch.utils.data.DataLoader(dataset1,**train_kwargs)
test_loader = torch.utils.data.DataLoader(dataset2, **test_kwargs)