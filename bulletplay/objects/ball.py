import pybullet as p


def create_balls(x, y, vx, vy, radius=0.1, mass=20):
    colBallId = p.createCollisionShape(p.GEOM_SPHERE, radius=radius)
    basePosition = [x, y, radius/2]
    baseOrientation = [0, 0, 0, 1]
    visualShapeId = -1
    ballUid = p.createMultiBody(mass, colBallId, visualShapeId, basePosition, baseOrientation)
    p.resetBaseVelocity(ballUid, linearVelocity=[vx, vy, 0])
