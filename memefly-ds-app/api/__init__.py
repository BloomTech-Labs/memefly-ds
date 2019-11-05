from api.config import PACKAGE_ROOT
from api.config import DevelopmentConfig

with open(PACKAGE_ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()
