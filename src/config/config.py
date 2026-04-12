
import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()


class Config:

    HOST_LOG: Final[str] = os.environ["HOST_LOG"]
    DB_LOG: Final[str] = os.environ["DB_LOG"]
    PORT_LOG: Final[str] = os.environ["PORT_LOG"]
    USER_LOG: Final[str] = os.environ["USER_LOG"]
    PASSWORD_LOG: Final[str] = os.environ["PASSWORD_LOG"]

    HOST_S3: Final[str] = os.environ["HOST_S3"]
    PORT_S3: Final[str] = os.environ["PORT_S3"]
    USER_S3: Final[str] = os.environ["ACCESS_KEY_S3"]
    PASSWORD_S3: Final[str] = os.environ["SECRET_KEY_S3"]
    CHAVE_API_YOUTUBE: Final[str] = os.environ["CHAVE_API_YOUTUBE"]
