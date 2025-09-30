import numpy as np   

# TODO: Forces for 3+
def compute_forces(bodies, G=1.0):
    n = len(bodies)
    forces = [np.zeros(3) for _ in range(n)]
    eps = 0.1  # softening length

    for i in range(n):
        for j in range(i + 1, n):
            r_vec = bodies[j].position - bodies[i].position
            r2 = np.dot(r_vec, r_vec)  # squared distance
            if r2 == 0:
                continue
            denom = (r2 + eps**2)**1.5
            force = G * bodies[i].mass * bodies[j].mass * r_vec / denom

            forces[i] += force
            forces[j] -= force
    return forces

       