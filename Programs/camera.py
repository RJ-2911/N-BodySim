import numpy as np
from OpenGL.GLU import gluLookAt

import simWindow as sw

def _normalize(v):
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
        # convert angles to radians
        yaw = np.deg2rad(self.theta)
        pitch = np.deg2rad(self.phi)

        # forward vector using spherical coordinates (right-handed, forward pointing into -Z at theta=0)
        self.forwards = np.array([
            np.cos(pitch) * np.sin(yaw),
            np.sin(pitch),
            -np.cos(pitch) * np.cos(yaw)
        ], dtype=np.float32)

        # normalize to be safe
        self.forwards = _normalize(self.forwards)

        global_up = np.array([0.0, 1.0, 0.0], dtype=np.float32)
        # right is cross(forward, up) to get screen-right
        self.right = np.cross(self.forwards, global_up)
        self.right = _normalize(self.right)

        # up is cross(right, forward)
        self.up = np.cross(self.right, self.forwards)
        self.up = _normalize(self.up)

    def apply_view(self):
        # Build center point camera is looking at
        center = self.position + self.forwards
        # Apply camera using gluLookAt
        gluLookAt(
            float(self.position[0]), float(self.position[1]), float(self.position[2]),
            float(center[0]), float(center[1]), float(center[2]),
            float(self.up[0]), float(self.up[1]), float(self.up[2])
        )

    # small helpers for moving the camera in local camera space
    def move_local(self, dx=0.0, dy=0.0, dz=0.0):
        # dx along right, dy along up, dz along forwards
        self.position += self.right * dx
        self.position += self.up * dy
        self.position += self.forwards * dz

    def rotate(self, dtheta=0.0, dphi=0.0):
        self.theta = (self.theta + dtheta) % 360.0
        self.phi = max(-89.9, min(89.9, self.phi + dphi))
        self.update_vectors()
