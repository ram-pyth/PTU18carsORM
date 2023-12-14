from sqlalchemy.orm import sessionmaker
from model_cars import Car, engine

Session = sessionmaker(bind=engine)
session = Session()


def select_all(ses):
    all_data = ses.query(Car).all()
    return all_data


def create_record(ses, make, model, price, year):
    row_o = Car(make, model, price, year)
    ses.add(row_o)
    ses.commit()



