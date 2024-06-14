import os
import re
import sys
sys.path.pop(0)
from setuptools import setup
sys.path.append("./sdist_upip")
import sdist_upip

version_reference = os.getenv('GITHUB_REF', default='1.0.0')
release_version_search = re.search(r'(\d+.\d+.\d+)', version_reference)
if release_version_search:
    release_version = release_version_search.group()
    print(f'Version: {release_version}')
else:
    raise ValueError("Version was not found")

setup(
    name='OTAUpdateManager',
    version=release_version,
    description='Implementation of OTA for remote monitoring and controlling of IoT devices',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    packages=[''],
    project_urls={
        'Source': 'https://github.com/raghulrajg/MicroPython-OTAUpdateManager'
    },
    author='Raghul Raj G',
    author_email='raghulrajatmega328@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU v3.0 License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "OTA",
        "OTAUpdateManager",
        "Update",
        "Microcontroller",
        "Micropython"
    ],
    cmdclass={'sdist': sdist_upip.sdist}
)