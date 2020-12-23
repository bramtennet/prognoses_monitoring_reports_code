import setuptools
import os
from setuptools import setup


pkg_dir = os.path.dirname(os.path.realpath(__file__))
# package description
with open(os.path.join(pkg_dir, 'README.md')) as f:
    long_description = f.read()
with open(os.path.join(pkg_dir, 'requirements.txt')) as f:
    required = f.read().splitlines()
with open(os.path.join(pkg_dir, 'PACKAGENAME')) as f:
    pkg_name = f.read().strip().strip('\n')
with open(os.path.join(pkg_dir, 'VERSION')) as f:
    version = f.read().strip().strip('\n')
    if 'BETA' in os.environ:
        version += f"b-{version}"
        print(f'Make beta version number: {version}')

setup(
    name=pkg_name,
    version=version,
    author="Bram van Vugt",
    author_email="Bram.van.Vugt@tennet.eu",
    description="prognoses monitoring package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bramtennet/prognoses_monitoring_reports_code",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)