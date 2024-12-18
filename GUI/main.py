import customtkinter as ctk
import os
import numpy as np
from PIL import Image
import torch
print(np.__version__)

from settings import Frame_settings
from widgets.interactive_image import Interactive_image
from widgets.interactive_grid import Interactive_grid
from fastbook import *
from fastai.vision.widgets import *
from fastai.vision.all import *
from auxiliar_functions import normalize_image

class NPs_detection_gui(ctk.CTk):
    def __init__(self, project_path = os.path.abspath('GUI'), *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Parameters and variables
        self.project_path = project_path
        self.grid_path = 'Data/image2.png'
        self.size_image = 600
        self.grid_width = 800
        self.grid_heigth = 600
        self.grid_matrix = np.array(Image.open(self.grid_path))
        self.zeros = np.zeros((256,256))
        self.model = torch.load('ML/models/model_tecnai_300.pt')

        self.learn_inf = load_learner('ML/models/nanos_detector.pkl')

        # Window theme
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        # Inizialicing window
        self.geometry('1300x800+50+50')
        self.title('Labeling app')

        # Window icon
        self.iconbitmap(self.project_path + '/assets/Group_icon.ico')

        # Frames set up
        self.frame_images = ctk.CTkFrame(self)
        self.frame_settings = Frame_settings(self, self.project_path)

        self.frame_settings.pack(side = 'right', fill = 'both', padx = 5, pady = 5)
        self.frame_images.pack(expand = True, fill = 'both', padx = 5, pady = 5)

        # Images
        self.image_microscope = Interactive_image(self.frame_images, self.zeros, title = 'Microscope view', font=('American typewriter', 24), width=self.size_image, height=self.size_image)
        self.image_grid = Interactive_grid(self.frame_images, self.show_region, self.grid_matrix, title = 'Grid', font=('American typewriter', 24), width=self.grid_width, height=self.grid_heigth)
        
        self.image_microscope.pack(side = 'right',  padx = 5, pady = 15, expand = True)
        self.image_grid.pack(side = 'right',  padx = 5, pady = 15)

        

    def show_region(self, matrix):
        
        prediction = self.model.predict(matrix)
        img_format = np.uint8(matrix*255) #We need change the format
        pred = self.learn_inf.predict(img_format)
        print(float(pred[2][1]), np.max(prediction[0][0]))
        self.image_microscope.change_image(prediction[0][0, :, : , 0])

        if float(pred[2][1]) > 0.5:
            color = 'green'
        else:
            color = 'red'
        self.frame_settings.label_model1.configure(text = f'Model 1: {float(pred[2][1]):.2f}',  text_color = color)
        

def get_x(r):
    im = Image.open('imagenes_M/' + r['labels'] +'/'+ r['file name'])
    return np.array(np.uint8(normalize_image(im)*255))
def get_y(r): return r['labels']

if __name__ == '__main__':
    app = NPs_detection_gui()
    app.mainloop()