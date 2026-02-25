from sqlalchemy.orm import Session
from app.models.users import User  # ✅ correct model import


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session):
    print("Abhishek")
    return db.query(User).all()


def create_user(db: Session, name: str, email: str):
    # Step 1: Create object
    new_user = User(name=name, email=email)

    # Step 2: Add to session
    db.add(new_user)

    # Step 3: Commit to database
    db.commit()

    # Step 4: Refresh (to get auto-generated ID)
    db.refresh(new_user)

    # Step 5: Return inserted user
    return new_user
