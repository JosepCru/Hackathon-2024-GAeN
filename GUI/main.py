import customtkinter as ctk
import os

from settings import Frame_settings

class NPs_detection_gui(ctk.CTk):
    def __init__(self, project_path = os.path.abspath('GUI'), *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Parameters and variables
        self.project_path = project_path

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

if __name__ == '__main__':
    app = NPs_detection_gui()
    app.mainloop()