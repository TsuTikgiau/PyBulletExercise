from setuptools import setup, find_packages


setup(
    name='bulletplay',
    version='0.1.0',
    description='Toy project to learn PyBullet',
    author='Deyao Zhu',
    author_email='tsu.tikgiau@gmail.com',
    url='https://github.com/TsuTikgiau/PyBulletExercise',
    packages=find_packages(exclude=('tests',)),
    install_requires=['PyBullet==2.0.9', 'numpy']
)