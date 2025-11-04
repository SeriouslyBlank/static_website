import os
from textnode import TextNode
import shutil

from pathlib import Path

def main():
	dummy = TextNode("This is some anchor text", "link", "https://www.boot.dev")

	print(dummy)

	source_dir_to_dest_dir("test", "actually")




def source_dir_to_dest_dir(src_dir, dst_dir):
    """
    Copy the entire contents of `src_dir` into a freshly recreated `dst_dir`.

    - Preserves file metadata (uses shutil.copy2).
    - Does NOT ignore any files or directories.
    - Safety checks prevent copying into itself or into a nested path.
    """
    src = Path(src_dir).resolve()
    dst = Path(dst_dir).resolve()

    if not src.exists() or not src.is_dir():
        raise ValueError(f"Source directory does not exist or is not a directory: {src}")

    # Disallow same or nested paths that could cause data loss or recursion issues
    src_str, dst_str = str(src), str(dst)
    if src == dst or dst_str.startswith(src_str + os.sep) or src_str.startswith(dst_str + os.sep):
        raise ValueError("Destination must not be the same as or nested within the source (and vice versa).")

    # Recreate destination directory
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True, exist_ok=True)

    # Copy entire tree (metadata-preserving)
    shutil.copytree(
        src,
        dst,
        dirs_exist_ok=True,     # redundant since we just recreated, but safe if races happen
        copy_function=shutil.copy2
    )




if __name__ == "__main__":
    main()

	