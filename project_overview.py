# Project Overview

# The goal of this project is to create an develop an effective system for detecting faulty tires using a pre-trained ResNet18 model.
# The system can identify images containing defects as opposed to a good one, which is useful for detection , replacement of faulty tyres for avoiding safety incidents.

import torch
import torch.nn as nn
from torchvision import models

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load pre-trained ResNet18
resnet18 = models.resnet18(pretrained=True)

# Replace the last layer (classifier) to match number of classes for fine-tuning
num_classes = len(train_data.classes)  # Assuming train_data contains your dataset
resnet18.fc = nn.Linear(resnet18.fc.in_features, num_classes)

# Freeze all layers except the last layer for fine-tuning
for param in resnet18.parameters():
    param.requires_grad = False

for param in resnet18.fc.parameters():
    param.requires_grad = True


resnet18.to(device)
