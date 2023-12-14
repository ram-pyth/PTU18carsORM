from sqlalchemy.orm import sessionmaker
from model_cars import Car, engine

Session = sessionmaker(bind=engine)
session = Session()


def select_all(ses):
    all_data = ses.query(Car).all()
    return all_data

# for eil_o in all_data:
#     print(eil_o)

# INSERT
# row_o = Car("BMW", "x3", 5000, 2003)
# session.add(row_o)
# session.commit()
