import pybullet as p
import pybullet_data
import numpy as np
import time


def build_cubic_tower(x, y, half_extents=0.1, num_cubic=10, mass=1):
    colBoxId = p.createCollisionShape(p.GEOM_BOX, halfExtents=[half_extents, half_extents, half_extents])
    basePosition = [x, y, half_extents]
    baseOrientation = [0, 0, 0, 1]
    visualShapeId = -1

    for i in range(num_cubic):
        boxUid = p.createMultiBody(mass, colBoxId, visualShapeId, basePosition, baseOrientation)
        basePosition[2] += 2 * half_extents


def build_cylinder_tower(x, y, radius_range=(0.1, 1), height_range=(1, 0.1), num_cylinder=5, mass=1):
    radiuses = np.linspace(*radius_range, num_cylinder)
    heights = np.linspace(*height_range, num_cylinder)
    colCylinderIdList = [p.createCollisionShape(p.GEOM_CYLINDER, radius=radius, height=height)
                         for radius, height in zip(radiuses, heights)]
    basePosition = [x, y, heights[0]/2]
    baseOrientation = [0, 0, 0, 1]
    visualShapeId = -1

    for i in range(num_cylinder):
        boxUid = p.createMultiBody(mass, colCylinderIdList[i], visualShapeId, basePosition, baseOrientation)
        if i < num_cylinder - 1:
            basePosition[2] += (heights[i] + heights[i+1]) / 2


if __name__ == "__main__":
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.createCollisionShape(p.GEOM_PLANE)

    build_cubic_tower(0, 0)
    build_cylinder_tower(0, 1)
    planeId = p.loadURDF("plane.urdf")
    p.setGravity(0, 0, -10)
    p.setRealTimeSimulation(1)

    while (1):
        keys = p.getKeyboardEvents()
        print(keys)

        time.sleep(0.01)

