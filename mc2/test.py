import torch

from model import TrafficCNN
from dataset import get_test_loader


device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

test_loader = get_test_loader()

model = TrafficCNN()
model.load_state_dict(torch.load("traffic_cnn.pth"))
model.to(device)
model.eval()

correct = 0
total = 0

with torch.no_grad():
    for x, y in test_loader:
        x, y = x.to(device), y.to(device)

        preds = model(x)
        _, predicted = preds.max(1)

        total += y.size(0)
        correct += (predicted == y).sum().item()

accuracy = 100 * correct / total
print(f"Test Accuracy: {accuracy:.2f}%")
