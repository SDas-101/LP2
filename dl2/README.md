# Devanagari Handwritten Digit Recognition using CNN

## Overview

This project implements a Convolutional Neural Network (CNN) for recognizing handwritten **Devanagari digits (0–9)**.

The system includes:

* Model training on digit dataset
* Evaluation during training
* GUI-based inference
* Sequence prediction with accuracy display

The project builds upon a basic MNIST pipeline and improves it with deeper architecture, normalization, and augmentation.

---

## Project Structure

```
dl2_dev/
 ├── model.py          # CNN architecture
 ├── train.py          # Training script
 ├── app.py            # GUI inference application
 ├── dev_cnn.pth       # Trained model weights
 ├── data/             # Dataset (NOT included in repo)
 │    ├── train/
 │    │    ├── digit_0 ... digit_9
 │    ├── test/
 │         ├── digit_0 ... digit_9
 ├── README.md
```

---

## Dataset

This project uses a **Devanagari handwritten digit dataset**.

The dataset is **not included** in this repository.

Download it from:
👉 **[PASTE YOUR GOOGLE DRIVE LINK HERE]**

---

### Dataset Structure (IMPORTANT)

After downloading, arrange it exactly like this:

```
data/
 ├── train/
 │    ├── digit_0/
 │    ├── digit_1/
 │    ├── digit_2/
 │    ├── ...
 │    ├── digit_9/
 │
 ├── test/
      ├── digit_0/
      ├── digit_1/
      ├── digit_2/
      ├── ...
      ├── digit_9/
```

Each folder must contain images of that digit class.

The project uses `ImageFolder`, so incorrect structure will cause errors.

---

## Requirements

Python 3.10+

Install dependencies:

```
pip install torch torchvision matplotlib pillow
```

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
pip install torch torchvision matplotlib pillow
```

---

### 3. Train the model

```
python train.py
```

* Trains CNN for 15 epochs
* Displays test accuracy each epoch
* Saves model as `dev_cnn.pth`

---

### 4. Run GUI application

```
python app.py
```

---

## GUI Usage

1. Enter a sequence of digits (e.g., `8762483275`)
2. Click **Predict**
3. System will:

   * Select random handwritten samples from dataset
   * Predict each digit
   * Display digit strip
   * Show predicted sequence
   * Show prediction accuracy

---

## Model Architecture

The CNN consists of:

* 3 convolutional layers (32 → 64 → 128 filters)
* Batch Normalization
* Max Pooling
* Fully connected layer
* Dropout (0.3)
* Output layer (10 classes)

---

## Training Details

* Loss Function: CrossEntropyLoss
* Optimizer: Adam
* Learning Rate Scheduler: StepLR
* Data Augmentation:

  * RandomRotation(10)
  * RandomAffine (translation)

---

## Output

* Trained model: `dev_cnn.pth`
* Console output shows accuracy per epoch
* GUI shows:

  * Predicted digit sequence
  * Accuracy (correct predictions / total digits)

---

## Example Result

* Training accuracy: ~98%
* GUI prediction accuracy: near 100% on test samples

---

## Important Notes

* Dataset must be placed correctly inside `data/`
* Model automatically uses GPU if available
* GUI predictions depend on dataset samples
* This is classification-based prediction, not full OCR

---

## Limitations

* Works only on dataset samples, not arbitrary handwriting
* Limited to digits (0–9), not full Devanagari characters
* GUI uses random sampling from test set

---

## Future Improvements

* Extend to full Devanagari characters
* Add real handwriting input support
* Improve UI design
* Use deeper architectures (ResNet, etc.)

---

## License

For academic and educational use.
