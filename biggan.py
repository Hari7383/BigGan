# -*- coding: utf-8 -*-
"""BigGan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1265fvJ748wb7wNpWPyo8wF7SCUv5bLIo
"""

pip install pytorch-pretrained-biggan

"""Only for Animals"""

import nltk
nltk.download('wordnet')  # Download the WordNet corpus

import torch
from pytorch_pretrained_biggan import BigGAN, one_hot_from_names, truncated_noise_sample
from torchvision.utils import save_image
import matplotlib.pyplot as plt
from PIL import Image

# Load pre-trained BigGAN model
model = BigGAN.from_pretrained('biggan-deep-256')

# Switch model to evaluation mode
model.eval()

# Set up the input parameters
truncation = 0.4

# Create a one-hot vector for the class you want to generate
class_vector = one_hot_from_names(['dalmatian'], batch_size=1)

# Generate random noise vector
noise_vector = truncated_noise_sample(truncation=truncation, batch_size=1)

# Convert to torch tensors
noise_vector = torch.from_numpy(noise_vector)
class_vector = torch.from_numpy(class_vector)

# Generate image with the BigGAN model
with torch.no_grad():
    output = model(noise_vector, class_vector, truncation)

# Post-process the output to image
output = (output.clamp(-1, 1) + 1) / 2  # Normalize to [0, 1]
output = output.cpu()

# Save and display the generated image
save_image(output, 'generated_image.png')

# Load and show the image
image = Image.open('generated_image.png')
plt.imshow(image)
plt.axis('off')
plt.show()