# A2CPS Data Submissions to the NIMH Data Archive (NDA)

## Dependencies

This software depends on several Python packages, which may be installed with:

    pip install -r requirements.txt

Installation in a Python virtual environment is always recommended. REDCap
utilities require [xmarshal](https://github.com/pschumm/xmarshal), which must
be compiled using [Cython](https://cython.readthedocs.io/). Thus, prior to
installation, you will need a C compiler:

**Linux**

    sudo apt-get install build-essential

**macOS**

Install Apple’s XCode from the App Store

**Windows**

Install [Microsoft's C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)


## Usage

To export data from REDCap using API:

    redcap_export -t [API token] -p A2CPSMainStudy https://redcap.uchicago.edu/api/

To generate file in HEAL CDE format:

    python extract_to_cde/koos-12.py
    frictionless validate --schema schemas/koos-12.yaml tmp/heal_cde/koos-12.csv

To translate to NDA submission format (as determined by structure):

    python generate_uploads/koos-12.py
    vtcmd tmp/uploads/*
