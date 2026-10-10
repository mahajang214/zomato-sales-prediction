import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from sql.connect_postgreSQL import connect_db


import dotenv
dotenv.load_dotenv()

from sql.connect_postgreSQL import connect_db


connect_db()