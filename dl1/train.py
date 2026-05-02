import os
import time
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.utils as vutils

from model import Generator, Discriminator
from dataset import get_mnist_loader


device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

loader = get_mnist_loader()

G = Generator().to(device)
D = Discriminator().to(device)

criterion = nn.BCELoss()

g_opt = optim.Adam(G.parameters(), lr=0.00015, betas=(0.5, 0.999))
d_opt = optim.Adam(D.parameters(), lr=0.0002, betas=(0.5, 0.999))

epochs = 50
z_dim = 100

os.makedirs("outputs", exist_ok=True)

training_start = time.time()

for epoch in range(epochs):

    epoch_start = time.time()

    for real, _ in loader:

        real = real.view(-1, 784).to(device)
        b = real.size(0)

        ones = torch.ones(b, 1).to(device)
        zeros = torch.zeros(b, 1).to(device)

        # -------------------------
        # Train Discriminator
        # -------------------------
        z = torch.randn(b, z_dim).to(device)
        fake = G(z)

        d_real = D(real)
        d_fake = D(fake.detach())

        d_loss = criterion(d_real, ones) + criterion(d_fake, zeros)

        d_opt.zero_grad()
        d_loss.backward()
        d_opt.step()

        # -------------------------
        # Train Generator twice
        # -------------------------
        z = torch.randn(b, z_dim).to(device)
        fake = G(z)

        g_loss = criterion(D(fake), ones)

        g_opt.zero_grad()
        g_loss.backward()
        g_opt.step()

    epoch_end = time.time()
    epoch_time = epoch_end - epoch_start

    print(
        f"Epoch {epoch+1}/{epochs} | "
        f"D Loss: {d_loss.item():.4f} | "
        f"G Loss: {g_loss.item():.4f} | "
        f"Time: {epoch_time:.2f} sec"
    )

    with torch.no_grad():
        z = torch.randn(16, z_dim).to(device)
        samples = G(z).view(-1, 1, 28, 28)

        vutils.save_image(
            samples,
            f"outputs/epoch_{epoch+1}.png",
            normalize=True,
            nrow=4
        )

training_end = time.time()
total_time = training_end - training_start

torch.save(G.state_dict(), "generator.pth")

print(f"Training complete in {total_time:.2f} seconds")