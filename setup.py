from os.path import join, dirname, abspath
from setuptools import setup, find_packages


prj_dir = dirname(abspath(__file__))
setup(
    name='ir-provisioner',
    version='0.0.1',
    packages=find_packages(),
    long_description=open(join(prj_dir, 'README.rst')).read(),
    entry_points={
        'console_scripts': ['ir-provisioner=main:main']
    },
    author='rhos-qe',
    author_email='rhos-qe-dept@redhat.com'
)
