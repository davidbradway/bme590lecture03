

## Using Virtualenv
virtualenv test
source test/bin/activate
pip install -r requirements.txt
deactivate

## Using Conda
conda create -n test
source activate test
pip install -r requirements.txt
