from  .base import os, BASE_DIR

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child(str(os.getenv("DB_LOCAL"))),
    }
}