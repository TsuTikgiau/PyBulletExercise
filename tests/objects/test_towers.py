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
        build_cubic_tower(0, 0)
        for t in range(5):
            p.stepSimulation()

    def test_cylinder_tower(self):
        print('\ntest creation of cylinder tower')
        build_cylinder_tower(1, 1)
        for t in range(5):
            p.stepSimulation()


if __name__ == '__main__':
    unittest.main()
