import os
import shutil
import sys
from generate import generate_pages_recursive

PATH = "docs"

def delete_public():
    if os.path.exists(PATH):
        print(f"deleting {PATH}")
        shutil.rmtree(PATH)

def copy_directory_contents(src_path: str, dst_path: str):
    src = os.listdir(src_path)
    for item in src:
        joined_src = os.path.join(src_path, item)
        if os.path.isfile(joined_src):
            shutil.copy(joined_src, dst_path)
            print(f"copied {item} to {dst_path}")
        else:
            new_dst = os.path.join(dst_path, item)
            if not os.path.exists(new_dst):
                os.mkdir(new_dst)
                print(f"created directory: '{new_dst}'")
            copy_directory_contents(joined_src, new_dst)

if len(sys.argv) >= 2:
    basepath = f"/{sys.argv[1]}/"
else:
    basepath = "/"

def main():
    delete_public()
    os.mkdir("docs")
    copy_directory_contents("static", "docs")
    generate_pages_recursive("content/", "template.html", "docs/", basepath)

if __name__ == "__main__":
    main()
