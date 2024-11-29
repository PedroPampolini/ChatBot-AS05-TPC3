import os
pip = 'pip' if os.name == 'nt' else 'pip3'
def installApp():
  try:
    import flask
  except:
    installLib('Flask')
  try:
    import flask_socketio
  except:
    installLib('Flask-SocketIO')
  try:
    import transformers
  except:
    installLib('transformers')
  try:
    import PyPDF2
  except:
    installLib('PyPDF2')
  try:
    import torch
  except:
    installLib('torch')

  

def installLib(lib:str):
  os.system(f'{pip} install {lib}')



from typing import *
import torch