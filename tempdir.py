import tempfile
import os
with tempfile.TemporaryDirectory() as tmp_dirname:
    print('\n')
    print(tmp_dirname)
    print(os.path.join(tmp_dirname) ==tmp_dirname)
    print('\n')
