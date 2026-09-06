from copy_static import import_to_public
import os
import shutil

def main():
    public = "./public/"
    if os.path.exists(public):
        shutil.rmtree(public)
    os.mkdir(public)
    import_to_public()

main()