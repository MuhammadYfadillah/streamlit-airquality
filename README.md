## Setup Environment - Anaconda
```
conda create --name main-ds python=3.12.6
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir lastproject
cd lastproject
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard1.py
```