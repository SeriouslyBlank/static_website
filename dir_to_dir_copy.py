import os 
import shutil
from pathlib import Path


def source_dir_to_desig_dir():
    root = Path(".").resolve()
    public = root / "public"

    # Recreate public/
    if public.exists():
        shutil.rmtree(public)
    public.mkdir(parents=True, exist_ok=True)

    # Ignore function used for all subdirectories
    def ignore_hidden_and_dunder(dirpath, names):
        ignored = []
        for name in names:
            if name.startswith(".") or name.startswith("__"):
                ignored.append(name)
        return set(ignored)

    for entry in root.iterdir():
        # Skip the destination itself and hidden/dunder entries at top-level
        if entry.name == "public" or entry.name.startswith(".") or entry.name.startswith("__"):
            continue

        dest = public / entry.name
        if entry.is_dir():
            # Recursively copy directory, honoring ignore patterns and preserving metadata
            shutil.copytree(
                entry,
                dest,
                ignore=ignore_hidden_and_dunder,
                dirs_exist_ok=True  # requires Python 3.8+
            )
        elif entry.is_file():
            # Copy single file with metadata
            shutil.copy2(entry, dest)
        # (Optional) handle symlinks explicitly if you use them:
        # elif entry.is_symlink(): shutil.copy(entry, dest, follow_symlinks=False)


	


source_dir_to_desig_dir()