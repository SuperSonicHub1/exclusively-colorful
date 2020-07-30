import imghdr
import json

def validate_image(stream):
  header = stream.read(512)
  stream.seek(0) 
  format = imghdr.what(None, header)
  if not format:
      return None
  return '.' + (format if format != 'jpeg' else 'jpg')

def schools():
  with open("names.json")as f:
    return json.load(f)