import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm

from model import TrafficCNN
from dataset import get_train_loader


device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

train_loader = get_train_loader()

model = TrafficCNN().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 25
lr = 0.0005


for epoch in range(epochs):
    model.train()
    total_loss = 0

    for x, y in tqdm(train_loader):
        x, y = x.to(device), y.to(device)

        preds = model(x)
        loss = criterion(preds, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss:.3f}")


torch.save(model.state_dict(), "traffic_cnn.pth")
print("Model saved as traffic_cnn.pth")
