import checkDependencies
checkDependencies.installApp()

from flask import Flask, render_template, Response, request
from flask_socketio import SocketIO, emit
from Bot import Bot, ModelName
import asyncio
import os

import warnings
warnings.filterwarnings("ignore")

socketio = SocketIO()
app = Flask(__name__)
bot = Bot(ModelName.roberta2)

@socketio.on('connect', namespace='/chat')
def joined(message):
    message = asyncio.run(bot.Greetings())
    emit('message', {
        'msg': f"Bot: {message}",
    })
    print(f"joined")


@socketio.on('text', namespace='/chat')
def text(message):
    print(f"text: {message['msg']}")
    try:
      # use asyncio to get bot message
      response = asyncio.run(bot.GetAnwser(message['msg'], 'uploadedPdf'))
      print(response)
      emit('message', {
          'msg': f"Bot: {response}",
      })
    except Exception as e:
      print(f"Error: {e}")
      emit('message', {
          'msg': f"Bot: {e}",
      })

@socketio.on('left', namespace='/chat')
def left(message):
    emit('status', {
        'msg': f"Voce saiu has left the room.",
    })
    print(f"left")
    


# index.html
@app.route('/')
def index():
    # get list of files in /uploadedPdf
    files = os.listdir('uploadedPdf')
    print(files)

    return render_template('index.html', pdfFiles=files)

@app.route('/uploadPdf', methods=['POST'])
def uploadPdf():
  print("uploadPdf")
  # save the uploaded PDF file in the server
  try:
    print(request.files)
    file = request.files['file']
    path = os.path.join('uploadedPdf', file.filename)
    request.files['file'].save(path)
    print("File saved")
    return render_template('success.html')
  except Exception as e:
    print("Error")
    return render_template('error.html',exception=e)

@app.route('/deletePdfList', methods=['DELETE'])
def deletePdfList():
  # delete all files in /uploadedPdf
  bot.ClearContext()
  files = os.listdir('uploadedPdf')
  for file in files:
    os.remove(os.path.join('uploadedPdf', file))
  return Response(status=200)

@app.route('/debug')
def debug():
  return '<h1>I AM ALIVE</h1>'

if __name__ == '__main__':
    socketio.init_app(app)
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)