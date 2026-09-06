from copy_static import import_to_public
from gen_content import generate_page
import os
import shutil

def main():
    public = "./public/"
    if os.path.exists(public):
        shutil.rmtree(public)
    os.mkdir(public)
    import_to_public()
    generate_page("./content/index.md", "./template.html", "./public/index.html")
main()