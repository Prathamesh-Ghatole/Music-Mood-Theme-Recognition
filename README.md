# Music-Mood-Theme-Recognition

## Setup:
### Download Dataset
```
wget -r -np -nH --cut-dirs=2 http://calab1.ucsd.edu/~datasets/cal500/
rm -r index.html* && rm cal500data/index.html*
```

### Run the Project
1. Setup a Python Virtual Environment
```
python3 -m venv env/
pip install -r requirements.txt
source env/bin/activate
```

2. Run the Project
```
python main.py
```