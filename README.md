# Clicker

The goal of this script is (for now) just a simple auto clicker written in python.

## How it works

Basically while you hold the right mouse button down, the script will click every `100` miliseconds until you release
the mouse button.

### How to use it

```bash
# For linux users
python3 -m venv venv
python3 venv/bin/activate
pip3 install -r requirements.txt
python3 src/main.py

# For windows users
python -m venv venv
venv\Scripts\activate.ps1
pip install -r requirements.txt
python src\main.py
```

## Future plans

Make a config file/UI to configure the script with more listener options.