# A2CPS Data Submissions to the NIMH Data Archive (NDA)

## Dependencies

I suggest using a virtual environment, ex:
    vitrualenv venv
    source venv/bin/activate

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

### Configuration
To export data from REDCap using API:

    redcap_export -t "[API token]" -p A2CPS_Main_Study_MCC1 https://redcap.uchicago.edu/api/
    redcap_export -t "[API token]" -p A2CPS_Main_Study_MCC2 https://redcap.uchicago.edu/api/
    redcap_export -t "[API token]" -p A2CPS_TKA_MCC2 https://redcap.tacc.utexas.edu/api/
    redcap_export -t "[API token]" -p A2CPS_Thoracic_MCC1 https://redcap.tacc.utexas.edu/api/

Next well need to include the mapping of RedCap record_ids to NDA guids, these are stored in the 
`nda_guid` from the `consented_participant_information` form and can be pulled 
and pooled from each project, here's a copy I made:
- https://utexas.box.com/s/ajaajviaxg3393ykyftcm8u8anxlw7zu
- copy that file into `ids/guids.csv`

We'll need to set our date offset for participants, that's done locally with a .env file, ex:

    echo "DAY_OFFSET=1" >> .env

For testing, any date offset is fine but check with me to get the real one if you're uploading to NDA

And also include a copy of freeze ids to filter by subjects in the data freeze, ex:
- https://github.com/a2cps/snapshot/blob/7842917c0eba80b9a3b1acbd952d1f835c62b493/src/snapshot/data/DataFreeze_1_022823.csv
- add that file to `ids/DataFreeze_1_022823.csv`

### Export, Transform, Validate
The general process is: 
- export data from RedCap
- transform to match HEAL CDE format
- validate HEAL format
- transform to NDA format
- validate HEAL format

You can extract either a single form, multiple forms, or all if you use no arguments, see `python extract_to_cde/extract.py --help` for details:

    python extract_to_cde/extract.py koos

Validate HEAL formats individually:

    frictionless validate --schema schemas/koos-12.yaml tmp/heal_cde/koos-12.csv

To translate to NDA submission format (as determined by structure):

    export PYTHONPATH="./frictionless/plugins"
    frictionless transform --pipeline generate_uploads/koos-12.json tmp/heal_cde/koos-12.csv

To generate and validate file for upload to NDA (defaults to all if no argument passed):

    python generate_uploads/create_nda.py koos
    vtcmd tmp/uploads/*

To generate new NDA template and definitions files for submitting data without and existing NDA structure:

    python generate_nda_templates/create_nda_structuers.py --input-vlmd <CDE-VLMD.json> --output-file <NDA-shortname>

Note: Validation of NDA upload will show "Invalid GUID" errors unless you use
the [NDA GUID Tool](https://nda.nih.gov/nda/nda-tools) to generate valid
GUIDs.

## Development details
I develop locally on my Mac, to manage dependencies I use homebrew, pyenv, and virtualenv
- install Homebrew with the curl command at this site: https://brew.sh/
- should install in /opt/homebrew/ if you're using an ARM Mac chip
- add `export PATH="/opt/homebrew/bin:$PATH"` to your ~/.zprofile (or ~/.bash_profile or ~/.bashrc if you're running on a bash shell)
- `brew install pyenv`
- `pyenv install 3.11.8`
- `pyenv local 3.11.8`
- `pip install virtualenv`
- `python -m virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- and `pip install notebook` if you want to use a jupyter notebook 

Once your development environment is setup, you can open `build_example.ipynb` to 
see a demonstration of pulling the RedCap form and comparing it to the HEAL schema. 

When ready to add a new conversion for one of the forms you'll need to add a new parameter name
to "choices" in parser.add_arguments from `extract.py` [here](https://github.com/a2cps/a2cps-data-submission/blob/95c945ecad35977fb603672c250cf73ba5d940ca/extract_to_cde/extract.py#L605):

    choices=["all", "prsupport", "koos", "taps", "gad", "pcs", "phq", "prsleep"],

and create a new parameter name:function mapping [here](https://github.com/a2cps/a2cps-data-submission/blob/95c945ecad35977fb603672c250cf73ba5d940ca/extract_to_cde/extract.py#L587), ex:

    "prsleep": extract_prsleep,

Next you'll need to add the RedCap form name [here](https://github.com/a2cps/a2cps-data-submission/blob/95c945ecad35977fb603672c250cf73ba5d940ca/extract_to_cde/extract.py#L548).
For a full list of forms you can use `print_forms(project)` from the `build_example.ipynb`

Then I would copy one of the existing functions, and edit it for the new form. ex [here](https://github.com/a2cps/a2cps-data-submission/blob/95c945ecad35977fb603672c250cf73ba5d940ca/extract_to_cde/extract.py#L456)

To find out what files to put into `codes`, `drop_if_all_null`, `null_assignments`, `rename_columns`, `replace_values`, and `output_columns`. I use the helper functions in build_example.ipynb to compare the RedCap fields with the HEAL schema. Heal schemas are stored in the 'schemas' folder. 

Often during the validation step, I notice an issue with the schema, like a value missing in enumLabels, or complaints about using "pattern" with integers, see example from `schemas/phq-9.yaml` [here](https://github.com/a2cps/a2cps-data-submission/commit/95c945ecad35977fb603672c250cf73ba5d940ca#diff-2a67651760edcb9b9d6dda7fa2048b43b1c4608365b327ed320a37c3baf5929fL59), but for the most part the schemas are ready to use and authored by the HEAL team. 

Similarly sometimes the steps in the frictionless pipeline validation need to be edited as well, see `generate_uploads/promis-sleep-distrubance.json` [here](https://github.com/a2cps/a2cps-data-submission/commit/95c945ecad35977fb603672c250cf73ba5d940ca#diff-74c8c6db01581519b99b438ddf1a6bced19d5508b33b8f0edc5d681480229ebdL13) but this is relatively uncommon and for the most part these are good to go. 

Now to create the NDA outputs you'll need to add a parameter option to `generate_uploads/create_nda.py` [here](https://github.com/a2cps/a2cps-data-submission/blob/95c945ecad35977fb603672c250cf73ba5d940ca/generate_uploads/create_nda.py#L92)

and add the function mapping simliar to how we did before in the extract script, [here](https://github.com/a2cps/a2cps-data-submission/blob/95c945ecad35977fb603672c250cf73ba5d940ca/generate_uploads/create_nda.py#L75)

and add a simple output function to define the file names ex [here](https://github.com/a2cps/a2cps-data-submission/blob/95c945ecad35977fb603672c250cf73ba5d940ca/generate_uploads/create_nda.py#L59), 
define a output filepath in the tmp/uploads directory, 
the "header" line which you can find in the Submission template for a given Data Structure, ex:
https://nda.nih.gov/data-structure/prsld01
and pass the path to the HEAL CDE (also in the tmp folder)

After that you can test if the conversion was successful following the "Export, Transform, Validate" section above



## Helpful links:
- https://a2cps-pain.slack.com/files/U017H6H7XGW/F082HPR3UJD/heal_cdes.zip 
- https://heal.nih.gov/data/common-data-elements-repository 
- https://nda.nih.gov/general-query.html?q=query=data-structure%20~and~%20searchTerm=prsleep%20~and~%20orderBy=shortName%20~and~%20orderDirection=Ascending%20~and~%20resultsView=tiled-view
- https://a2cps.atlassian.net/wiki/spaces/DIRC/pages/442990601/NDA+Data+Structure+Status


