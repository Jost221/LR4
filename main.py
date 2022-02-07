import os

def input_patch():#Хренычев Максим
  pass#need to take patch from user, check directory for exist and return patch

def scan_file(path, level = 1, dictionary = {}):#Скитихин Георгий
  for i in os.listdir(path):
    print(os.path.join(path, i))
    try:
      if os.path.isdir(os.path.join(path, i)):
        scan_file(os.path.join(path, i), level + 1 ,dictionary)
      else:
        dictionary[os.path.join(path, i)] = os.stat(os.path.join(path, i)).st_size
    except Exception as error:
      print(error)
  return dictionary

def sort():#Шешин Александр
  pass#sort all dictionary and return dirctionary with file dublikate

def printed():#тимлид
  pass

