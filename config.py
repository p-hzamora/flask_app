from pathlib import Path
import secrets

basedir = Path(__file__).parent

class Config:
    DEBUG = True
    SECRET_KEY =secrets.token_hex(16)
    EXPLAIN_TEMPLATE_LOADING = True