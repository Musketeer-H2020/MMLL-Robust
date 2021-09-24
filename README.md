# MMLL-Robust
MMLL extensions for Robustness

# Installation using Anaconda (Windows and Linux)

0. Requisites:
  - Conda: https://www.anaconda.com
  - Git client: https://git-scm.com/
  
1. Create conda environment:
```
conda create -n mmll python=3.7 pip
```
2. Activate environment:
```
conda activate mmll
```
3. Install dependencies:
```
conda install gmpy2
pip install git+https://github.com/Musketeer-H2020/MMLL-Robust.git
```
4. Navigate to a folder of your choice  (as for instance your home folder '~') and clone project:
```
git clone https://github.com/Musketeer-H2020/MMLL-Robust
```

## Installation using venv in Linux

Alternatively, you can use Python venv built-in module to create a working environment.

1. Install Python 3.7:
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
sudo apt-get install python3.x-dev
```
2. Update pip:
```
python3 -m pip install --upgrade pip
```
3. Create virtual environment in your home folder:
```
cd ~
python3 -m venv mmll
```
Please note: "mmll" is the environment name. You can use whatever name you prefer.

4. Install library:
```
pip install git+https://github.com/Musketeer-H2020/MMLL-Robust.git
```

