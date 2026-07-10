# N-BodySim

## General Purpose

N-BodySim is an interactive 3D gravitational simulation project. Its goal is to model how multiple massive bodies influence each other over time using pairwise gravity, and to visualize that motion in real time.

The project is useful for:

- understanding n-body dynamics conceptually,
- experimenting with initial positions, velocities, mass, and radius,
- observing orbital-like or chaotic motion in a rendered 3D scene.

## How the Project Functions

The application runs as two cooperating processes:

- a **simulation process** that computes physics and renders the 3D scene,
- a **GUI process** that handles controls, object creation, and status display.

These processes communicate through multiprocessing queues:

- `body_to_sim_queue`: sends newly created bodies from GUI to simulation,
- `sim_to_body_queue`: sends current sphere state from simulation back to GUI.

### Runtime Flow

1. `Programs/main.py` starts both processes.
2. The simulation window initializes OpenGL, scene objects, camera, and physics engine.
3. Each simulation frame:

- computes gravitational forces between all bodies,
- updates velocity and position for each sphere,
- receives any newly added body from GUI,
- sends current body data back to GUI,
- renders spheres, grids, and axis indicator.

4. The GUI window:

- renders a control/info panel,
- lets the user open an Add Object form,
- pushes new body parameters into the simulation queue,
- displays current simulated body values received from simulation.

## Physics Model

The simulation uses Newton-style pairwise attraction with a small softening factor to avoid singularities at extremely small distances.

Per body update:

- net force is accumulated from all other bodies,
- acceleration is computed as `force / mass`,
- velocity and position are advanced using a time step `dt`.

## Main Components

- `Programs/main.py`: process orchestration and queue wiring.
- `Programs/simulation/physicsCalc.py`: force computation and integration.
- `Programs/simulation/simWindow.py`: simulation loop and queue I/O.
- `Programs/simulation/scene.py`: initial body setup and camera placement.
- `Programs/simulation/renderer.py`: OpenGL rendering (spheres, grids, axes).
- `Programs/simulation/events.py`: simulation-side camera and render toggles.
- `Programs/gui/guiWindow.py`: GUI loop and panel composition.
- `Programs/gui/body.py`: body add/update data bridge.
- `Programs/gui/methods.py`: Add Object form and input validation.

## Controls

### GUI Controls

- **Add**: opens form to create a new body.
- **Play/Pause, Reset, Fast**: present in UI (some are currently placeholders).

### Simulation Window Controls

- `W/A/S/D`: move camera forward/left/back/right.
- `Space` / `Left Shift`: move camera up/down.
- Mouse movement: look around (yaw/pitch).
- Arrow keys: rotate camera.
- `Q` / `E`: increase/decrease camera movement speed.
- `1`, `2`, `3`: toggle grid planes.
- `4`: toggle axis crosshair.
- `Esc`: quit.

## Input Parameters for New Bodies

When adding a body, you can provide:

- position `(x, y, z)`,
- velocity `(vx, vy, vz)`,
- mass,
- radius,
- color `(R, G, B, alpha)`.

Validation rules enforce:

- mass > 0,
- radius > 0,
- `R/G/B` in `[0, 255]`,
- `alpha` in `[0.0, 1.0]`.

## Installation and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
python Programs/main.py
```

This launches both the GUI and simulation windows.

## Collaborators

- RJ-2911
- money1501
- Prem791
