def calibrate_depth(depth):
    slope = 2.8957595647292513
    bias = -49.338457552465684
    depth = slope * depth + bias
    return depth

def caculate_height(scale_y_left):
    slope = -80.0513698630137
    bias = 210.5593607305936
    bias = bias + 2
    height = slope * scale_y_left + bias
    return height