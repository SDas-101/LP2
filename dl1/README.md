# Deep Learning Assignment 1

## Deep GAN for Multimedia Image Generation (MNIST)

This project implements a Deep Generative Adversarial Network (GAN) using PyTorch to generate synthetic handwritten digit images from the MNIST dataset.

---

## Project Structure

dl1/

* model.py → Generator and Discriminator architectures
* dataset.py → MNIST dataset loader
* train.py → GAN training loop
* app.py → image generation script
* data/ → dataset storage
* outputs/ → generated samples
* generator.pth → saved generator model

---

## Requirements

Python 3.10+ and:

* torch
* torchvision
* matplotlib
* numpy

Install using:

pip install -r ../requirements.txt

---

## How to Run

### 1. Create and activate virtual environment

#### Linux / WSL:

```
python3 -m venv venv
source venv/bin/activate
```

#### Windows:

```
python -m venv venv
venv\Scripts\activate
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Train the GAN

```
python train.py
```

* MNIST dataset will be **automatically downloaded** to `data/` 
* Model will be saved as `generator.pth`

---

### 4. Generate images

```
python app.py
```

* Generates new handwritten digits
* Output saved in `outputs/generated.png` 


## Output

* Generated images saved in `outputs/`
* Intermediate samples saved each epoch
* Final model saved as `generator.pth`
* `generated.png` contains newly synthesized digits

---

## Concepts Used

* Generative Adversarial Networks (GANs)
* Generator & Discriminator training
* Binary Cross-Entropy Loss
* Latent noise vectors
* GPU acceleration with CUDA
* PyTorch DataLoader

---

## Notes

If CUDA is available, training automatically uses GPU.
Otherwise, it falls back to CPU.

Training may take a few minutes depending on hardware.
