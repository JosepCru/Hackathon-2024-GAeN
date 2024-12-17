from PIL import Image
import random
import os
import matplotlib.pyplot as plt
import numpy as np

def generate_sample(pathBackgrounds, pathNanoparticles, n_rows = 5, n_columns = 5, prob_nano = 0.5, size = 128):
    imagesBackground = os.listdir(pathBackgrounds)
    imagesNanoparticles = os.listdir(pathNanoparticles)
    sample_width = n_columns * size
    sample_height = n_rows * size
    sample_final =  np.zeros((sample_height, sample_width, 3), dtype=np.uint8)

    for row in range(n_rows):
        for col in range(n_columns):
            if random.random() > prob_nano:
                img = random.choice(imagesBackground)
                img_path = os.path.join(pathBackgrounds, img)
            else:
                img = random.choice(imagesNanoparticles)
                img_path = os.path.join(pathNanoparticles, img)

            img = Image.open(img_path).convert("RGB")
            img_np = np.array(img)

            y_start = row * size
            y_end = (row + 1) * size
            x_start = col * size
            x_end = (col + 1) * size


            sample_final[y_start:y_end, x_start:x_end, :] = img_np
    
    return np.array(sample_final)