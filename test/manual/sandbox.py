from pathlib import Path
from sys import path

ROOT_DIR = Path(path[0]).parent.parent
path.insert(0, str(ROOT_DIR / 'src'))

import app