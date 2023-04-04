import sqlite3 as sq
from help_for_bot import bot

async def sql_start():
    try:
        db = sq.connect('opinion.db')
        curs = db.cursor()
        print('База данных подключена')
    
    except sq.Error as e:
        print('Error', e)
    
    finally:
        curs.close()
        db.close()


async def add_user(user_id):
    try:
        db = sq.connect('opinion.db')
        curs = db.cursor()

        curs.execute('INSERT INTO user(user_id) VALUES(?)',[user_id])
    
    except sq.Error as e:
        print('Error',e)

    finally:
        curs.close()
        db.close()

async def sql_earn(user_id , value):

    operation = '+'
    user_id = int(user_id)
    
    try:
        db = sq.connect('opinion.db')
        curs = db.cursor()

        curs.execute('INSERT INTO records(user_id, operation, value) VALUES(?, ?, ?)',[user_id, operation , value])
        db.commit()
    
    except sq.Error as e:
        print('Error',e)
    
    finally:
        curs.close()
        db.close()

async def sql_expens(user_id , value):
    operation = '-'
    user_id = int(user_id)
    
    try:
        db = sq.connect('opinion.db')
        curs = db.cursor()

        curs.execute('INSERT INTO records(user_id, operation, value) VALUES(?, ? , ?)',[user_id, operation , value])
        db.commit()
    
    except sq.Error as e:
        print('Error',e)
    
    finally:
        curs.close()
        db.close()

async def opinion_sql(user_id):
    try:
        db = sq.connect('opinion.db')
        curs = db.cursor()

        message = curs.execute('SELECT * FROM `records` WHERE user_id = ?', [user_id]).fetchall()
        
        return message

    except sq.Error as e:
        print('Error',e)
    
    finally:
        curs.close()
        db.close()

