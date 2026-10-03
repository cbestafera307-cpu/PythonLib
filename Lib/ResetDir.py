import os

def ResetDir(dir):
    os.system(f"rm -r {dir}")
    os.system(f"mkdir -p {dir}")
