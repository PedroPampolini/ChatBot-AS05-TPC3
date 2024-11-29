import os
pip = 'pip' if os.name == 'nt' else 'pip3'
def installApp():
  try:
    import flask
  except:
    installLib('flask')
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

  try:
    import flask
    import flask_socketio
    import transformers
    import PyPDF2
    import torch
  except Exception as e:
    print(f"[ERROR] {e}")
    print("[ERROR] Could not install all dependencies")
    print("[ERROR] Please install the missing dependencies manually")
    exit(1)

  

def installLib(lib:str):
  print(f"[DEBUG] Installing {lib}")
  os.system(f'{pip} install {lib}')