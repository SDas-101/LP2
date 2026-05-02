import os
import pandas as pd
from PIL import Image
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Dataset


# Common transform
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.RandomRotation(10),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),
])


# -----------------------------
# TRAIN LOADER (unchanged logic)
# -----------------------------
def get_train_loader(batch_size=64):
    train_data = datasets.ImageFolder(
        "GTSRB/Final_Training/Images",
        transform=transform
    )
    return DataLoader(train_data, batch_size=batch_size, shuffle=True)


# -----------------------------
# CUSTOM TEST DATASET
# -----------------------------
class GTSRBTestDataset(Dataset):
    def __init__(self,
                 root="GTSRB/Final_Test/Images",
                 csv_file="GTSRB/Final_Test/GT-final_test.csv",
                 transform=None):

        self.root = root
        self.transform = transform

        df = pd.read_csv(csv_file, sep=';')

        self.images = df['Filename'].values
        self.labels = df['ClassId'].values

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = os.path.join(self.root, self.images[idx])

        image = Image.open(img_path).convert("RGB")
        label = int(self.labels[idx])

        if self.transform:
            image = self.transform(image)

        return image, label


# -----------------------------
# TEST LOADER
# -----------------------------
def get_test_loader(batch_size=64):
    test_data = GTSRBTestDataset(transform=transform)
    return DataLoader(test_data, batch_size=batch_size, shuffle=False)
