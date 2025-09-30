import numpy as np   

# TODO: Forces for 3+
def compute_forces(bodies, G=1.0):
    n = len(bodies)
    forces = [np.zeros(3) for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            r_vec = bodies[j].position - bodies[i].position
            distance = np.linalg.norm(r_vec)
            if distance == 0:
                continue
            force_mag = G * bodies[i].mass * bodies[j].mass / (distance ** 2)
            force_dir = r_vec / distance
            force = force_mag * force_dir

            forces[i] += force
            forces[j] -= force
    return forces

       