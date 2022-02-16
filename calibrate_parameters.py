def calibrate_depth(depth):
    slope = 2.8957595647292513
    bias = -49.338457552465684
    depth = slope * depth + bias
    return depth