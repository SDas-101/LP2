import os
import torch
import torchvision.utils as vutils

from model import Generator


device = "cuda" if torch.cuda.is_available() else "cpu"

G = Generator().to(device)
G.load_state_dict(torch.load("generator.pth", map_location=device))
G.eval()

os.makedirs("outputs", exist_ok=True)

torch.manual_seed(13)

z = torch.randn(16, 100).to(device)

with torch.no_grad():
    fake = G(z).view(-1, 1, 28, 28)

vutils.save_image(
    fake,
    "outputs/generated.png",
    normalize=True,
    nrow=4
)

print("Images saved to outputs/generated.png")