import shutil
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
backup = f"backup-{today}"
shutil.make_archive(backup, 'zip', '../../section1')

print(f"Created backup: {backup}.zip")