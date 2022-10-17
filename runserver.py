from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """run dash using flask"""
    Popen(["python", "./app.py"])