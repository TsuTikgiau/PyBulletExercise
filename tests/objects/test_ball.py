import unittest
import pybullet as p
import pybullet_data
from bulletplay.objects.ball import create_ball


class TestTower(unittest.TestCase):

    def setUp(self):
        p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        planeId = p.loadURDF("plane.urdf")

    def test_ball(self):
        print('\ntest creation of ball')
        create_ball(0, 0, 1, 1, 2, 3)
        for t in range(5):
            p.stepSimulation()


if __name__ == '__main__':
    unittest.main()
