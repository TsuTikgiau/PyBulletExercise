import unittest
import pybullet as p
import pybullet_data
from bulletplay.objects.towers import build_cubic_tower, build_cylinder_tower


class TestTower(unittest.TestCase):

    def setUp(self):
        p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        planeId = p.loadURDF("plane.urdf")

    def test_cubic_tower(self):
        print('\ntest creation of cubic tower')
        build_cubic_tower(x=0, y=0, half_extents=1, num_cubic=3, mass=2)
        for t in range(5):
            p.stepSimulation()

    def test_cylinder_tower(self):
        print('\ntest creation of cylinder tower')
        build_cylinder_tower(x=1, y=1, radius_range=(1, 0.1), height_range=(0.1, 1), num_cylinder=10, mass=2)
        for t in range(5):
            p.stepSimulation()


if __name__ == '__main__':
    unittest.main()
