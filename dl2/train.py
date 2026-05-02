import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

from model import CNN


device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

train_transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.RandomRotation(10),
    transforms.RandomAffine(0, translate=(0.1, 0.1)),
    transforms.ToTensor()
])

test_transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.ToTensor()
])

train_data = datasets.ImageFolder("data/train", transform=train_transform)
test_data = datasets.ImageFolder("data/test", transform=test_transform)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=64)

model = CNN().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.5)

epochs = 15

for epoch in range(epochs):
    model.train()

    for x, y in train_loader:
        x, y = x.to(device), y.to(device)

        preds = model(x)
        loss = criterion(preds, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    scheduler.step()

    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)

            preds = model(x)
            predicted = preds.argmax(dim=1)

            correct += (predicted == y).sum().item()
            total += y.size(0)

    accuracy = 100 * correct / total

    print(f"Epoch {epoch+1}: Test Accuracy = {accuracy:.2f}%")

torch.save(model.state_dict(), "dev_cnn.pth")
print("Training complete")