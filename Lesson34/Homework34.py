import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ------------------------------------------------------------------------------TASK DESCRIPTIONS-----------------------
# ------Task1: Working with SQl: Creating Tables and etc - ORM
# ------Task2:
# ------Task3:
# ------Task4:


# ------------------------------------------------------------------------------GLOBAL Variables------------------------
global Task_list
Task_list = []


# ------------------------------------------------------------------------------MAIN GLOBAL CLASSES---------------------
class Task():
    def __init__(self, name):
        assert isinstance(name, str), "'name' must be a string!!!"
        self.Function = object
        Task_list.append(self)
        self.name = f"Task{Task_list.index(self) + 1}: {name}"

    def __str__(self):
        return self.name

    def write_function(self, object101):
        self.Function = object101

    def __call__(self):
        Looper = "y"
        while Looper == "y":
            self.Function()
            Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
            if Replay == "y":
                continue
            else:
                Looper = Replay


# ------------------------------------------------------------------------------CUSTOM GLOBAL FUNCTIONS-----------------

# ------------------------------------------------------------------------------TASK OBJECTS----------------------------
# --------------------------------------------------------------------------------------------------START TASK 1--------
Task01 = Task("Working with SQl: Creating Tables and etc - ORM")


def task1_body():
    pass
    # ----------------Task Variables----------------------------------
    HOST = 'localhost'
    PORT = 5432
    DATABASE = 'Lesson34'
    USER = 'postgres'
    PASSWORD = 'XX132Files'

    database_string = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    engine = create_engine(database_string)
    Base = declarative_base()

    # ----------------Task Classes------------------------------------
    class Products(Base):
        __tablename__ = 'products'
        product_id = Column('product_id', Integer, primary_key=True, autoincrement=True, unique=True)
        product_name = Column('product_name', String(30))
        product_price = Column('product_price', Double)
        stock_quantity = Column('stock_quantity', Integer)
        category_id = Column('category_id', Integer, ForeignKey('categories.category_id'))

        def __init__(self, product_name, price, stock_quantity, category_id):
            self.product_name = product_name
            self.product_price = price
            self.stock_quantity = stock_quantity
            self.category_id = category_id

    class Categories(Base):
        __tablename__ = 'categories'
        category_id = Column('category_id', Integer, primary_key=True, autoincrement=True, unique=True)
        category_name = Column('category_name', String(30))

        def __init__(self, category_name):
            self.category_name = category_name

    class Orders(Base):
        __tablename__ = 'orders'
        order_id = Column('category_id', Integer, primary_key=True, autoincrement=True, unique=True)
        product_id = Column('product_id', Integer, ForeignKey('products.product_id'))
        quantity = Column('quantity', Integer)
        order_date = Column('order_date', Date)
        status = Column('status', String(30))

        def __init__(self, product_id, quantity, order_date, status):
            self.product_id = product_id
            self.quantity = quantity
            self.order_date = order_date
            self.status = status

    # ----------------Task Functions------------------------------------------------------------------------------------
    # 1) For inserting in product table:
    def add_product(product_name, price, stock_quantity, category_id):
        product = Products(product_name, price, stock_quantity, category_id)
        session.add(product)
        session.commit()

    # 2) For inserting in categories table:
    def add_category(category_name):
        category = Categories(category_name)
        session.add(category)
        session.commit()

    # 3) For Deleting elements from product table
    def delete_product(product_name):
        product_data = session.query(Products).all()
        for product in product_data:
            if product.product_name == product_name:
                session.delete(product)
                session.commit()

    # 4) For Updating elements from product table
    def update_product(product_name):
        pass

    # For cleaning all tables
    def clear_all_tables():
        data = session.query(Products).all()
        for i in data:
            session.delete(i)
            session.commit()
        data = session.query(Categories).all()
        for i in data:
            session.delete(i)
            session.commit()
        data = session.query(Orders).all()
        for i in data:
            session.delete(i)
            session.commit()

    # ----------------Task BODY-----------------------------------------------------------------------------------------
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # adding new elements into categories table:
    add_category("Food")
    add_category("Clothes")
    add_category("Essentials")
    add_category("Electronics")

    # adding new elements into product table:
    add_product("LG 2000: vacuum TV", 4999.90, 2, 4)
    add_product("ASSus Nutbook 1.2", 456.56, 200, 4)
    add_product("Onion Ragu", 1.99, 1, 1)
    add_product("Grandma Socks", 3.50, 50, 2)
    add_product("Key to WC", 99999.99, 1, 3)

    delete_product('ASSus Nutbook 1.2')

    clear_all_tables()


Task01.write_function(task1_body)
# ----------------------------------------------------------------------------------------------------END TASK 1--------

# -----------------------------------------------------------------------------------------------------END TASK 3--------
# ------------------------------------------------------------------------------MAIN CODE-------------------------------
for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
