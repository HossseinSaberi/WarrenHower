from database import create_session


def get_db():
    db = create_session()
    try:
        yield db
    finally:
        db.close()