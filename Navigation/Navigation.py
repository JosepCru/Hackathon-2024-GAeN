import numpy as np

class Autonomous_navigator():
    def __init__(self, image_sample, image_spiral):
        self.image_sample = image_sample
        self.image_spiral = image_spiral
        self.path_tracking = []

        self.step = 32
        self.fov = 256

    def calculate_np_probability(self, image):
        """
        This is the model which it will calculate the probability of finding nanoparticles
        """
        # do things
        return p

    # def standard_movement(image_sample, ):

    def border(self, i, j):
        """
        This function detects borders when scanning the image.
        border_x and border_y: coordinates along the x and y axis that we want to verify if they are exceeding the limits of the images.
        
        """
        
        border_left = j
        border_right = j + self.fov
        border_up = i - self.fov
        border_down = i 
        dimension_down, dimension_right = self.image_sample.shape
        
        if border_left >= 0 or border_right < dimension_right:
            return True
    
        if border_up >= 0 or border_down < dimension_down : 
            return True


    def find_np(self, p_np, coord_microscope):
        """
        This algorithm determines the navigation path for detecting nanoparticles. The direction of movement is guided by the probability of encountering nanoparticles at the next 
        step. This probability is provided by our model, which compares the likelihood of finding nanoparticles in different directions and selects the direction with the highest 
        probability.
        """
        n = self.step
        i, j = coord_microscope

        #Up
        if not self.border(i - n, j): 
            scanning_m_u = self.image_sample[i-self.fov-n:i-n, j:j+self.fov]
            prob_mov_u = self.calculate_np_probability(scanning_m_u)
        else:
            prob_mov_u = 0
        
        #Down
        if not self.border(i+n, j): 
            scanning_m_d = self.image_sample[i-self.fov+n:i+n, j:j+self.fov]
            prob_mov_d = self.calculate_np_probability(scanning_m_d)
        else: 
            prob_mov_d = 0

        #Left
        if not self.border(i, j-n): 
            scanning_m_r = self.image_sample[i-self.fov:i, j+n:j+self.fov+n]
            prob_mov_r = self.calculate_np_probability(scanning_m_r)
        else:
            prob_mov_l = 0
        
        #Right
        if not self.border(i, j+n):     
            scannig_m_l = self.image_sample[i-self.fov:i, j-n:j+self.fov-n]
            prob_mov_l = self.calculate_np_probability(scannig_m_l)
        else:
            prob_mov_r = 0
        
        probs = [prob_mov_r, prob_mov_l, prob_mov_u, prob_mov_d]
        max_prob = np.max(probs)

        #Acquiring the image of the nanoparticle when the surroundings haven't higher porbability of finding a nanoparticle than the current posistion
        if max_prob <= p_np: 
            i_new, j_new = i, j 
        
        #Displacement
        if max_prob == prob_mov_r: #go to the right
            i_new, j_new = i, j+n
            
        elif max_prob == prob_mov_l: #go to the left
            i_new, j_new = i, j-n
   
        elif max_prob == prob_mov_u: #go up
            i_new, j_new = i-n, j
                
        elif max_prob == prob_mov_d: #go down
            i_new, j_new = i+n, j

        return i_new, j_new



    def autonomous_navigation(self, image_sample, image_spiral, coord_microscope, step_movement = 32, fov = 256, threshold = 0.2):
        i, j = coord_microscope
        image_microscope = self.image_sample[i - fov: i, j : j + fov]

        # Calculate probability
        # p_np = self.calculate_np_probability(image_microscope)

        # if p_np < threshold:
        #     i_new, j_new = self.standard_movement(image_sample)

        # else:
        #     i_new, j_new = self.find_np()

        #     if i == i_new & j == j_new:
        #         self.acquire_images()
        #         i_new, j_new = self.find_new_grid()

        # self.path_tracking.append((i_new, j_new))
        # return i_new, j_new


    def autonomus_np_finder(self, coord_microscope, nps_wanted):
        i, j = coord_microscope
        nps_finded = 0
        while nps_finded < nps_wanted:
            i_new, j_new = self.autonomous_navigation(image_sample, image_spiral, coord_microscope, step_movement = 32, fov = 256, threshold = 0.2)
            coord_microscope = (i_new, j_new)