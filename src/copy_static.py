import os
import shutil

def import_to_docs(src="./static/", dest="./docs"):
    static = os.listdir(src)

    for item in static:
        src_item = os.path.join(src, item)
        dest_item = os.path.join(dest, item)
        if not os.path.isfile(src_item):
            os.makedirs(dest_item, exist_ok=True)
            import_to_docs(src_item, dest_item)
        else:
            shutil.copy(src_item, dest_item)
    return