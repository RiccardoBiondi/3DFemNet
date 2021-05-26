| **Authors**  | **Project** |  **Build Status** | **License** | **Code Quality** | **Coverage** |
|:------------:|:-----------:|:-----------------:|:-----------:|:----------------:|:------------:|
| [**R.Biondi**](https://github.com/RiccardoBiondi) [**E.Giampieri**](https://github.com/EnricoGiampieri) **G.Castellani**| **3DFemNet** | **Windows**: [![Build status](https://ci.appveyor.com/api/projects/status/d57n1rv4yk29daok?svg=true)](https://ci.appveyor.com/project/RiccardoBiondi/3dfemnet)**Linux**: [![Build Status](https://travis-ci.com/RiccardoBiondi/3DFemNet.svg?branch=main)](https://travis-ci.com/RiccardoBiondi/3DFemNet)|[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()|**Codacy** [![Codacy Badge](https://app.codacy.com/project/badge/Grade/6f428fcfb13840d7b2f439f5e8c3d384)](https://www.codacy.com/gh/RiccardoBiondi/3DFemNet/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=RiccardoBiondi/3DFemNet&amp;utm_campaign=Badge_Grade) **Codebeat** [![codebeat badge](https://codebeat.co/badges/be5cd759-f5ed-4db2-82c0-c4549dcd4989)](https://codebeat.co/projects/github-com-riccardobiondi-3dfemnet-main)|[![codecov](https://codecov.io/gh/RiccardoBiondi/3DFemNet/branch/main/graph/badge.svg?token=VWHLJ9BEJD)](https://codecov.io/gh/RiccardoBiondi/3DFemNet)|


![Project CI](https://github.com/RiccardoBiondi/3DFemNet/workflows/3DFemNet%20CI/badge.svg)


[![GitHub pull-requests](https://img.shields.io/github/issues-pr/RiccardoBiondi/3DFemNet.svg?style=plastic)](https://github.com/RiccardoBiondi/3DFemNet/pulls)
[![GitHub issues](https://img.shields.io/github/issues/RiccardoBiondi/3DFemNet.svg?style=plastic)](https://github.com/RiccardoBiondi/3DFemNet/issues)

[![GitHub stars](https://img.shields.io/github/stars/RiccardoBiondi/3DFemNet.svg?label=Stars&style=social)](https://github.com/RiccardoBiondi/3DFemNet/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/RiccardoBiondi/3DFemNet.svg?label=Watch&style=social)](https://github.com/RiccardoBiondi/3DFemNet/watchers)

# 3DFemNet

This project aims to smooth and improve the femur segmentation results by using
a deep learning approach. The basic  idea is to start from a (possibly) incomplete
or not-accurated femur segmentation and recostructing the original shape by infer
the continuos Signed Distance Function. This will lead to a smoother and accurate
3D femur reconstruction.


## Table of Contents

1. [Introduction](#Introduction)  
2. [Usage](#Usage)
3. [Authors](#Authors)
4. [License](#License)
5. [Acknowledge](#Acknowledge)
6. [Contribute](#Contribute)
7. [Cite](#Cite)
8. [References](#References)

## Introduction

## Usage

### Prerequisites

Supported python version: ![Python version](https://img.shields.io/badge/python-3.6|3.7|3.8-blue.svg)

### Installation

Download the project or the latest release:

```console
git clone https://github.com/RiccardoBiondi/3DFemNet
cd 3DFemNet
```

Install the required packages:
```console
pip install -r requirements.txt
```

To install 3DFemNet execute in 3DFemNet directory:
```console
python setup.py develop --user
```
#### testing

Testing routines use ```PyTest``` and ```Hypothesis```. Please install these packages to perform the test

All the full set of test is provided in [test](./test) folder.
You can run the full list of test with:
```console
python -m pytest
```

### Segment Scan

### Train a Model


## Authors

* <img src="https://avatars3.githubusercontent.com/u/48323959?s=400&v=4" width="25px"> **Riccardo Biondi** [git](https://github.com/RiccardoBiondi)

* <img src="https://avatars2.githubusercontent.com/u/1419337?s=400&v=4" width="25px;"/> **Enrico Giampieri** [git](https://github.com/EnricoGiampieri), [unibo](https://www.unibo.it/sitoweb/enrico.giampieri)

See also the list of [contributors](https://github.com/RiccardoBiondi/segmentation/contributors) who participated to this project.  [![GitHub contributors](https://img.shields.io/github/contributors/RiccardoBiondi/3DFemNet.svg?style=plastic)](https://github.com/RiccardoBiondi/3DFemNet/graphs/contributors/)


## License

`3DFemNet` is licensed under the MIT "Expat" License. [![License](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE.md)

## Acknowledge

Thanks goes to all contributors of this project.
A special thanks goes to Istituto Ortopedico Rizzoli which has provided the scans and the
hardware to train and test the network

## Contribute

Any contribution is more than welcome. Just fill an [issue](./.github/ISSUE_TEMPLATE.md) or a [pull request](./.github/PULL_REQUEST_TEMPLATE.md) and we will check ASAP!

See [here](https://github.com/RiccardoBiondi/3DFemNet/blob/master/CONTRIBUTING.md) for further informations about how to contribute with this project.

## Cite

If you have found `3DFemNet` helpful in your research, please consider citing the project



```tex
@misc{3DFemNet,
  author = {Biondi, Riccardo Giampieri, Enrico Castellani, Gastone},
  title = {Deep Learning approach for the reconstruction of femur segmentation using the Signed Distance Function},
  year = {2021},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/RiccardoBiondi/3DFemNet}}
}
```

## References
