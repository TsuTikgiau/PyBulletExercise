import pybullet as p
import pybullet_data
import time

from bulletplay.objects.towers import build_cubic_tower, build_cylinder_tower
from bulletplay.objects.ball import create_balls


def main():
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    # scenario building
    planeId = p.loadURDF("plane.urdf")
    build_cubic_tower(0, 0)
    build_cylinder_tower(0, 1)
    create_balls(0, -1, 0, 3)

    p.setGravity(0, 0, -10)
    p.setRealTimeSimulation(1)

    while True:
        time.sleep(0.01)


if __name__ == "__main__":
    main()
