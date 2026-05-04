class CRUDBase:
    def __init__(self, model):
        self.model = model

    def get_all(self, db):
        return db.query(self.model).all()

    def get_one(self, db, id):
        return db.query(self.model).get(id)