import json
import django.db.models.base as Base
import inspect

def load_json(path):
  """
  Loads the json file in the given path.  

  Precondition:
  path: is a string of a valid json path.
  """
  with open (path) as file:
    return json.load(file)
  return {}
