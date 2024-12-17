
class Autonomous_navigator():
    def __init__(self, image_sample, image_spiral):
        self.image_sample = image_sample
        self.image_spiral = image_spiral
        self.path_tracking = []

    # def calculate_np_probability(image):
    #     # do things
    #     return p

    # def standard_movement(image_sample, ):

    def autonomous_navigation(image_sample, image_spiral, coord_microscope, step_movement = 32, fov = 256, threshold = 0.2):
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

        # self.path_tracking.append(i_new, j_new)
        # return i_new, j_new


    def autonomus_np_finder(self, coord_microscope, nps_wanted):
        i, j = coord_microscope
        nps_finded = 0
        while nps_finded < nps_wanted:
            i_new, j_new = self.autonomous_navigation(image_sample, image_spiral, coord_microscope, step_movement = 32, fov = 256, threshold = 0.2)
            coord_microscope = (i_new, j_new)