import os
import sys

path = '/home/apex890520/hj-quotation'  # 替換成你的專案路徑
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings.prod' # 替換成你的settings檔名

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())