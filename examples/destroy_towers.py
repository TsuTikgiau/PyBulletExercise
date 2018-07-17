import pybullet as p
import pybullet_data
import time

from bulletplay.objects import build_cubic_tower, build_cylinder_tower


def main():
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    # scenario building
    planeId = p.loadURDF("plane.urdf")
    build_cubic_tower(0, 0)
    build_cylinder_tower(0, 1)

    p.setGravity(0, 0, -10)
    p.setRealTimeSimulation(1)

    while True:
        time.sleep(0.01)


if __name__ == "__main__":
    main()
