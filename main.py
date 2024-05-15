import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Float, CHAR, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = sqlalchemy.orm.declarative_base()


class Company(Base):
    __tablename__ = "companies"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    age = Column("Age", Integer)
    ceo = Column("ceo", String)
    marketvalue = Column("marketvalue", Float)


    def __init__(self,name, age, ceo, marketvalue):
        # self.id = id
        self.name = name
        self.age = age
        self.ceo = ceo
        self.marketvalue = marketvalue

    def __repr__(self):
        return f"{self.name} {self.age} {self.ceo} {self.marketvalue}USD"
    

class Employee(Base):
    __tablename__ = "employees"

    empname = Column("empname", String)
    empid = Column("empid", Integer, primary_key=True, autoincrement=True)
    address = Column("address", String)
    boss = Column(String, ForeignKey("companies.id"))


    def __init__(self, empname, empid, address, boss):
        self.empid = empid
        self.empname = empname
        self.address = address
        self.boss = boss

    def __repr__(self):
        return f"{self.empname} {self.address} employed by {self.boss}"
    


    

engine = create_engine("sqlite:///mydb.db, echo=True")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

company1 = Company("Marginseye", 4, "Edwin", 150000)
session.add(company1)
session.commit()


company2 = Company("Geesol", 3, "Gift", 190000)
company3 = Company("Safaricom", 20, "Peter", 50000000)
company4 = Company("Amazon", 4, "Bezos", 890000000)
company5 = Company("Owtechsol", 4, "Francis", 1500)

session.add(company2)
session.add(company3)
session.add(company4)
session.add(company5)

session.commit()


#querying objects

results = session.query(Company).all()
print(results)

emp1 = Employee("Els", 1, "Ruaka", "Edwin")
session.add(emp1)
session.commit()



