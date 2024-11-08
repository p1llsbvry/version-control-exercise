Create virtual environment:
```sh
conda create -n ump-env python=3.11
```
Activate the environment:
```sh
conda activate ump-env
```
Install packages:
```sh
#pip install requests
#pip install plotly
#pip install python-dotenv
# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
```

## Usage

Run the script:
```sh
python app/unemployment.py

# equivalent:
# equivalent (we'll need this once we start importing code from one file to another):
python -m app.unemployment
```