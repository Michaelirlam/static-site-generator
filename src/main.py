from copy_static import import_to_public
from gen_content import generate_pages_recursive
import os
import shutil

def main():
    public = "./public/"
    if os.path.exists(public):
        shutil.rmtree(public)
    os.mkdir(public)
    import_to_public()
    generate_pages_recursive("./content/", "./template.html", "./public/")
main()