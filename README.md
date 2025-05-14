# mh-operator

<div align="center">

[![Build status](https://github.com/chaoqing/mh-operator/workflows/build/badge.svg?branch=master&event=push)](https://github.com/chaoqing/mh-operator/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/mh-operator.svg)](https://pypi.org/project/mh-operator/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/chaoqing/mh-operator/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/chaoqing/mh-operator/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/chaoqing/mh-operator/releases)
[![License](https://img.shields.io/github/license/chaoqing/mh-operator)](https://github.com/chaoqing/mh-operator/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Awesome `mh-operator` provide interfaces and common routines for the Agilent MassHunter official SDK.

</div>


## Usage:

```powershell
# install mh_operator_legacy into Python2.7 and MassHunter search path
mh-operator.exe install

# analysis and report test data
mh-operator.exe analysis yellow.D -m methods\Analysis.m --report-method methods\Report.m
```

## Notice:

- MassHunter use [IronPython2.7.5](https://github.com/IronLanguages/main/releases/download/ipy-2.7.5/IronPython-2.7.5.msi) for its SDK engine, normally it does not have the python StdLib under its `PYTHONPATH`. For this package to work, you may need copy/paste the StdLib from `C:\Program Files\IronPython 2.7\Lib` to like `C:\MassHunter\Scripts\Unknowns\Lib` .
