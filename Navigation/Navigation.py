# def calculate_np_probability(image):
#     # do things
#     return p

# def standard_movement(image_sample, ):

def autonomous_navigation(image_sample, image_spiral, coord_microscope, step_movement = 32, fov = 256, threshold = 0.2):
    i, j = coord_microscope
    image_microscope = image_sample[i - fov: i, j : j + fov]

    # Calculate probability
    # p_np = calculate_np_probability(image_microscope)

    # if p_np < threshold:
    #     i_new, j_new = standard_movement(image_sample)

    # else:
    #     i_new, j_new = find_np()

    #     if i == i_new & j == j_new:
    #         acquire_images()
    #         i_new, j_new = find_new_grid()

    # return i_new, j_new

def autonomus_np_finder(image_sample, image_spiral, coord_microscope):
    i, j = coord_microscope
    image_microscope = image_sample[i - fov: i, j : j + fov]
    nps_finded = 0
    while nps_finded < nps_wanted:
        i_new, j_new = autonomous_navigation(image_sample, image_spiral, coord_microscope, step_movement = 32, fov = 256, threshold = 0.2)
        coord_microscope = (i_new, j_new)