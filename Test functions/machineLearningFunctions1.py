import numpy as np
"""
Problem:
You have a container and inside it are possibly balls of red and blue colors Compute for the total entropy of the 
container. You will be given 3 space separated integers. First integer will be the total number of balls in the jar.
The other 2 will be the number of balls for each color.
"""


def calculate_entropy(n, x_count, y_count):
    x_percentage = round(x_count / n, 2)
    y_percentage = round(y_count / n, 2)

    entropy_of_x = -x_percentage * np.log2(x_percentage) if x_count > 0 else 0
    entropy_of_y = -y_percentage * np.log2(y_percentage) if y_count > 0 else 0

    entropy = round(entropy_of_x + entropy_of_y, 2)

    return entropy


print(calculate_entropy(6, 2, 4))




