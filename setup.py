from setuptools import setup, find_packages


setup(
    name='bulletplay',
    python_requires='==3.5.5',
    version='0.1.1',
    description='Toy project to learn PyBullet',
    author='Deyao Zhu',
    author_email='tsu.tikgiau@gmail.com',
    url='https://github.com/TsuTikgiau/PyBulletExercise',
    packages=find_packages(exclude=('tests',)),
    install_requires=['PyBullet==2.0.9', 'numpy']
)