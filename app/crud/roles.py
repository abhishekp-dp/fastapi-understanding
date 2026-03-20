from sqlalchemy.orm import Session

from app.models.roles import Roles


def create_role(db: Session, id: int, name: str):
    # Step 1: Create object
    new_role = Roles(id=id, name=name)

    # Step 2: Add to session
    db.add(new_role)

    # Step 3: Commit to database
    db.commit()

    # Step 4: Refresh (to get auto-generated ID)
    db.refresh(new_role)

    # Step 5: Return inserted user
    return new_role