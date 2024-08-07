# A2CPS Data Submissions to the NIMH Data Archive (NDA)

## Dependencies

This software depends on several Python packages, which may be installed with:

    pip install -r requirements.txt

To export data from REDCap using API:

    redcap_export -t [API token] -p A2CPSMainStudy https://redcap.uchicago.edu/api/

To generate file in HEAL CDE format:

    python extract_to_cde/koos-12.py
    frictionless validate --schema schemas/koos-12.yaml tmp/heal_cde/koos-12.csv

To translate to NDA submission format (as determined by structure):

    python generate_uploads/koos-12.py
    vtcmd tmp/uploads/*
