# Traffic Sign Classification using CNN (GTSRB)

## Overview

This project implements a Convolutional Neural Network (CNN) for traffic sign classification using the German Traffic Sign Recognition Benchmark (GTSRB).

The model is trained to classify traffic signs into 43 categories and supports:

* Training on the dataset
* Evaluation on test data
* Predicting a single image via GUI file picker

---

## Features

* Custom CNN architecture (4 convolutional blocks)
* Data augmentation during training
* Test accuracy evaluation
* Single image prediction with class label output
* GPU support (if available)

---

## Project Structure

```
mc2/
├── train.py              # Train the CNN model
├── test.py               # Evaluate model on test set
├── predict.py            # Predict class for a single image
├── model.py              # CNN architecture
├── dataset.py            # Data loading and preprocessing
├── traffic_cnn.pth       # Saved trained model
├── stop_sign.jpg         # Sample image
├── README.md
```

---

## Dataset

This project uses the GTSRB dataset.

Download it from:
https://drive.google.com/drive/folders/1eJnrhnkw2m4OWXssHA8kwbsEBrYIc0wh?usp=sharing

### After downloading:

Extract and place it like this:

```
mc2/
 ├── GTSRB/
     ├── Final_Training/
     │    └── Images/
     ├── Final_Test/
     │    ├── Images/
     │    └── GT-final_test.csv
```

The loaders expect this exact structure. If you change it, things will break and you’ll blame everything except yourself.

---

## Requirements

Install dependencies:

```
pip install torch torchvision pandas pillow tqdm
```

---

## How to Run

### 1. Train the model

```
python train.py
```

* Trains for 25 epochs
* Saves model as `traffic_cnn.pth` 

---

### 2. Evaluate on test set

```
python test.py
```

* Loads trained model
* Computes accuracy on GTSRB test set 

---

### 3. Predict a single image

```
python predict.py
```

* Opens file picker
* Select an image
* Outputs predicted class and label 

---

## Model Architecture

Defined in `model.py` 

* 4 convolutional layers with BatchNorm
* Max pooling after each block
* Dropout for regularization
* Fully connected classifier

---

## Data Pipeline

Defined in `dataset.py` 

* Resize to 32×32
* Random rotation + horizontal flip
* Normalization
* Custom test dataset using CSV labels

---

## Example Prediction

Input:

* `stop_sign.jpg`

Output:

```
Predicted Class ID: 14
Traffic Sign: Stop
```

---

## Notes

* Uses GPU if available (`cuda`), otherwise CPU
* Model expects 32×32 RGB images
* Dataset structure must match expected paths

---

## Future Improvements

* Use deeper architectures (ResNet, EfficientNet)
* Add validation split and early stopping
* Improve augmentation strategy
* Deploy as web app

---

## License

For academic and educational use.
