# -*- coding: utf-8 -*-
#!/usr/bin/env python

# python3 setup.py develop --user

import os

try:
    from setuptools import setup
    from setuptools import find_packages

except ImportError:
  from distutils.core import setup
  from distutils.core import find_packages

__author__  = ['Riccardo Biondi', 'Nico Curti']
__email__   = ['riccardo.biondi4@studio.unibo.it', 'nico.curti2@unibo.it']



def get_requires(requirements_filename):
    '''
    What packages are required for this module to be executed?
    Parameters
    ----------
        requirements_filename : str
          filename of requirements (e.g requirements.txt)
    Returns
    -------
        requirements : list
            list of required packages
    '''
    with open(requirements_filename, 'r') as fp:
        requirements = fp.read()

    return list(filter(lambda x: x != '', requirements.split()))



def read_description(readme_filename):
    '''
    Description package from filename
    Parameters
    ----------
        readme_filename : str
            filename with readme information (e.g README.md)
    Returns
    -------
        description : str
            str with description
    '''
    try:
        with open(readme_filename, 'r') as fp:
            description = '\n'
            description += fp.read()
        return description

    except IOError:
        return ''


here = os.path.abspath(os.path.dirname(__file__))


#Package-Metadata
NAME = "3DFemNet"
DESCRIPTION = '3D network for computing continuos SDF for femur segmentation'
URL = ''
EMAIL = ['riccardo.biondi4@studio.unibo.it']
AUTHOR = ['Riccardo Biondi']
VERSION = None
KEYWORDS = []
REQUIREMENTS_FILENAME = os.path.join(here, 'requirements.txt')
VERSION_FILENAME = os.path.join(here, 'Model', '__version__.py')
README_FILENAME = os.path.join(here, 'README.md')


# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    LONG_DESCRIPTION = read_description(README_FILENAME)

except IOError:
    LONG_DESCRIPTION = DESCRIPTION


# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(VERSION_FILENAME) as fp:
        exec(fp.read(), about)

else:
    about['__version__'] = VERSION

# parse version variables and add them to command line as definitions
#Version = about['__version__'].split('.')

setup(
    name=NAME,
    #version=about['__version__'],
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    download_url=URL,
    keywords=KEYWORDS,
    packages=find_packages(include=['Model','Model.*', 'utils', 'utils.*',
                                    'Network', 'Network.*'], exclude=('test', 'testing')),
    include_package_data=True, # no absolute paths are allowed
    platforms='any',
    install_requires=get_requires(REQUIREMENTS_FILENAME),

    entry_points={
        'console_scripts': [
        'lung_extraction = CTLungSeg.lung_extraction:main',
        'labeling = CTLungSeg.labeling:main',
        'train = CTLungSeg.train:main'
        'CTLungSeg = CTLungSeg.__main__:main'
    ]},

    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    license = 'MIT'
)
