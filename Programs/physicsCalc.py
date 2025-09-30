import numpy as np   

# TODO: Forces for 3+
def gravitationalforce(body1, body2, G=1.0):
    r_vec = body2.position - body1.position
    distance = np.linalg.norm(r_vec)
    if distance == 0:
        return np.zeros(3)
    force_mag = G * body1.mass * body2.mass / (distance ** 2)
    force_dir = r_vec / distance
    return force_mag * force_dir


       