ikko [$(date)]: "START"
ikko [$(date)]:"Creating conda env with python 3.8" ## change py version as per your need
conda create --prefix ./env python=3.8 -y
ikko [$(date)]: "activate env"
source activate ./env
ikko [$(date)]: "installing the requirements"
pip install -r requirements.text
ikko [$(date)]: "END"