from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///cars.db")
Base = declarative_base()


class Car(Base):
    __tablename__ = "cars"
    rowid = Column(Integer, primary_key=True)
    car_make = Column(String)
    car_model = Column(String)
    car_price = Column(Integer)
    year = Column(Integer)

    def __init__(self, car_make, car_model, car_price, year):
        self.car_make = car_make
        self.car_model = car_model
        self.car_price = car_price
        self.year = year

    def __str__(self):
        return f"{self.rowid} {self.car_make} {self.car_model} {self.car_price} {self.year}"


Base.metadata.create_all(engine)

###################################
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # SELECT *
# all_data = session.query(Car).all()
# print(all_data)
#
# for eil_o in all_data:
#     print(eil_o)
#
# # INSERT
# # row_o = Car("BMW", "x3", 5000, 2003)
# # session.add(row_o)
# # session.commit()
# session.close()