import numpy as np
from OpenGL.GLU import gluLookAt

import simWindow as sw

def _normalize(v):
    # Normalizing Vectors
    v = np.array(v, dtype=np.float32)
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

class Camera:
    def __init__(self, simWin, position):
        self.position = np.array(position, dtype=np.float32)
        self.theta = 0.0   # yaw (degrees)
        self.phi = 0.0     # pitch (degrees)
        self.update_vectors()
        self.move_speed_base = 60
        self.simWin = simWin

    def update_vectors(self):
        # Updating Camera's Vector values
        yaw = np.deg2rad(self.theta)
        pitch = np.deg2rad(self.phi)
        global_up = np.array([0.0, 1.0, 0.0], dtype=np.float32) # Universal Up (Y-Axis)

        self.forwards = np.array([
            np.cos(pitch) * np.sin(yaw),
            np.sin(pitch),
            -np.cos(pitch) * np.cos(yaw)
        ], dtype=np.float32)
        self.forwards = _normalize(self.forwards)

        self.right = np.cross(self.forwards, global_up)
        self.right = _normalize(self.right)

        self.up = np.cross(self.right, self.forwards)
        self.up = _normalize(self.up)

    def apply_view(self):
        # Build center point camera is looking at
        center = self.position + self.forwards
        gluLookAt(
            float(self.position[0]), float(self.position[1]), float(self.position[2]),
            float(center[0]), float(center[1]), float(center[2]),
            float(self.up[0]), float(self.up[1]), float(self.up[2])
        )

    def move_local(self, dx=0.0, dy=0.0, dz=0.0):
        # Moves camera along the axes via dx, dy and dz
        self.position += self.right * dx
        self.position += self.up * dy
        self.position += self.forwards * dz

    def rotate(self, dtheta=0.0, dphi=0.0):
        # Rotates camera along the axes via theta and phi (on Y and Z Axes)
        self.theta = (self.theta + dtheta) % 360.0
        self.phi = max(-89.9, min(89.9, self.phi + dphi))
        self.update_vectors()