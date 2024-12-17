import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

from widgets.titled_frame import Frame_titled

class Frame_settings(ctk.CTkFrame):
    def __init__(self, root, project_path, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        ctk.CTkLabel(self, text = 'Settings',anchor = 'center', font=('American typewriter', 32), fg_color='#1f6aa5').pack(fill = 'x', padx = 5, pady = 5)
 
        # Frame General
        self.frame_fft = Frame_titled(self, 'General settings')

        # Layout
        self.frame_fft.pack(padx = 5, pady = 10, fill = 'x')
