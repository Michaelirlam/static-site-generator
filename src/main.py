from copy_static import import_to_docs
from gen_content import generate_pages_recursive
import os
import shutil
import sys

if len(sys.argv) < 2:
    basepath = "/"
else:
    basepath = sys.argv[1]
    

def main():
    docs = "./docs/"
    if os.path.exists(docs):
        shutil.rmtree(docs)
    os.mkdir(docs)
    import_to_docs()
    generate_pages_recursive("./content/", "./template.html", docs, basepath)
main()