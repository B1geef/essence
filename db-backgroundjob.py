from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import sqlalchemy

import database as db

engine = sqlalchemy.create_engine("postgresql+psycopg2://neondb_4ohx_user:fLNyrRWjOKghek3FmMAa8CQ9peLF8o2S@dpg-ch2gbul269v61fd8fm20-a.frankfurt-postgres.render.com/neondb_4ohx")
session = sqlalchemy.orm.sessionmaker(bind=engine)()

# create a function to delete old data from the table
def delete_old_data():
    # create a SQL query to delete rows older than 1 day
    # old_product=session.query(db.Product).filter(db.Product.deleted == True).all()    
    transactions = session.query(db.BtcTransaction).all()
    print(transactions)
    for transaction in transactions:
        session.delete(transaction)

    session.commit()

delete_old_data()
# create a scheduler that runs the delete_old_data function every day
# scheduler = BackgroundScheduler()
# scheduler.add_job(delete_old_data, 'interval', days=1)
# scheduler.start()