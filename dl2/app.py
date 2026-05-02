import torch
import random
from PIL import Image, ImageTk
from torchvision import transforms
import matplotlib.pyplot as plt
import os
import tkinter as tk

from model import CNN


device = "cuda" if torch.cuda.is_available() else "cpu"

model = CNN().to(device)
model.load_state_dict(torch.load("dev_cnn.pth"))
model.eval()

transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.ToTensor()
])


def show_full_sequence(full_text):
    popup = tk.Toplevel(root)
    popup.title("Full Predicted Sequence")
    popup.geometry("900x250")

    text_box = tk.Text(popup, wrap="word", font=("Arial", 14))
    text_box.pack(fill="both", expand=True)

    text_box.insert("1.0", full_text)
    text_box.config(state="disabled")


def predict_number():
    number = entry.get()

    predicted_output = ""
    images = []
    predictions = []
    correct = 0

    for digit in number:
        folder = f"data/test/digit_{digit}"

        files = [f for f in os.listdir(folder) if f.endswith(".png")]
        img_path = os.path.join(folder, random.choice(files))

        img = Image.open(img_path)

        tensor = transform(img).unsqueeze(0).to(device)

        with torch.no_grad():
            pred = model(tensor)
            predicted = pred.argmax().item()

        predicted_output += str(predicted)
        predictions.append(predicted)
        images.append(img)

        if str(predicted) == digit:
            correct += 1

    accuracy = (correct / len(number)) * 100

    fig_width = max(15, len(images) * 0.4)
    fig, axes = plt.subplots(1, len(images), figsize=(fig_width, 3))

    if len(images) == 1:
        axes = [axes]

    for i, image in enumerate(images):
        axes[i].imshow(image, cmap="gray")
        axes[i].set_title(str(predictions[i]), fontsize=8)
        axes[i].axis("off")

    plt.savefig("output_digits.png", bbox_inches="tight")
    plt.close()

    output_img = Image.open("output_digits.png")
    output_img = output_img.resize((900, 180))

    tk_img = ImageTk.PhotoImage(output_img)

    image_label.config(image=tk_img)
    image_label.image = tk_img

    # show first 50 digits only
    short_output = predicted_output[:50]

    if len(predicted_output) > 50:
        result_label.config(
            text=f"Predicted sequence: {short_output}..."
        )

        full_button.config(
            text="View Full Sequence",
            command=lambda: show_full_sequence(predicted_output)
        )
        full_button.pack()
    else:
        result_label.config(
            text=f"Predicted sequence: {predicted_output}"
        )
        full_button.pack_forget()

    accuracy_label.config(
        text=f"Accuracy: {accuracy:.2f}%"
    )


root = tk.Tk()
root.title("Devanagari Digit Recognition")
root.geometry("1200x700")

tk.Label(root, text="Enter number:", font=("Arial", 14)).pack()

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack()

tk.Button(root, text="Predict", command=predict_number, font=("Arial", 14)).pack()

image_label = tk.Label(root)
image_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

accuracy_label = tk.Label(root, text="", font=("Arial", 14))
accuracy_label.pack()

full_button = tk.Button(root, font=("Arial", 12))

root.mainloop()