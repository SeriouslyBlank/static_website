import os
import shutil
from pathlib import Path

from textnode import TextNode
from htmlnode import markdown_to_html_node
from split_nodes import extract_title


# --- Path anchors ---
# This file lives at static/src/main.py -> so STATIC_DIR is its parent directory's parent
STATIC_DIR = Path(__file__).resolve().parent.parent
PUBLIC_DIR = STATIC_DIR / "public"


def main():
    dummy = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(dummy)

    # 1) Copy all static assets to public (exclude code + content)
    source_dir_to_dest_dir(
        src_dir=STATIC_DIR,
        dst_dir=PUBLIC_DIR,
        exclude_dirs={"src", "content", ".git", "__pycache__"},
        exclude_files={"template.html"},
        exclude_globs=("*.md",),
    )

    # 2) Render the home page from Markdown + template
    generate_page(
        from_path=STATIC_DIR / "content" / "index.md",
        template_path=STATIC_DIR / "template.html",
        dest_path=PUBLIC_DIR / "index.html",
    )


def generate_page(from_path: Path, template_path: Path, dest_path: Path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        contents_file = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        contents_temp = f.read()

    html_node = markdown_to_html_node(contents_file)
    content_html = html_node.to_html()

    title = extract_title(contents_file)

    full_html = contents_temp.replace("{{ Title }}", title).replace("{{ Content }}", content_html)

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with dest_path.open("w", encoding="utf-8") as f:
        f.write(full_html)


def source_dir_to_dest_dir(
    src_dir,
    dst_dir,
    *,
    exclude_dirs=None,
    exclude_files=None,
    exclude_globs=(),
):
    """
    Copy the contents of `src_dir` into a freshly recreated `dst_dir`,
    excluding selected directories/files/globs. Preserves metadata.
    """
    exclude_dirs = set(exclude_dirs or set())
    exclude_files = set(exclude_files or set())
    exclude_globs = tuple(exclude_globs or tuple())

    src = Path(src_dir).resolve()
    dst = Path(dst_dir).resolve()

    if not src.exists() or not src.is_dir():
        raise ValueError(f"Source directory does not exist or is not a directory: {src}")

    # Safety checks against nested/same paths
    src_str, dst_str = str(src), str(dst)
    if src == dst or dst_str.startswith(src_str + os.sep) or src_str.startswith(dst_str + os.sep):
        raise ValueError("Destination must not be the same as or nested within the source (and vice versa).")

    # Recreate destination directory
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True, exist_ok=True)

    # Use copytree with ignore callable so it's fast and metadata-preserving
    def _ignore(dirpath, names):
        # names are immediate children of dirpath
        ignored = set()

        # exclude specific directories by name
        for n in names:
            if n in exclude_dirs and (Path(dirpath) / n).is_dir():
                ignored.add(n)

        # exclude specific files by exact name
        for n in names:
            if n in exclude_files and (Path(dirpath) / n).is_file():
                ignored.add(n)

        # exclude by glob patterns
        if exclude_globs:
            for n in names:
                p = Path(dirpath) / n
                for pat in exclude_globs:
                    if p.match(pat) or Path(n).match(pat):
                        ignored.add(n)

        return ignored

    shutil.copytree(
        src,
        dst,
        dirs_exist_ok=True,      # safe re-run
        copy_function=shutil.copy2,
        ignore=_ignore,
    )


if __name__ == "__main__":
    main()
