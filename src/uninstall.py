import os, shutil
for the_file in os.listdir():
    if (the_file in ('__pycache__', 'objects', 'sounds')):
        shutil.rmtree(the_file)
    else:
        os.unlink(the_file)
