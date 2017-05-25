import db

def fetchSchedule(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM BaysApp_schedule ORDER BY ActualAtime")
    return cursor.fetchall()

def fetchFlight(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM BaysApp_flight")
    return cursor.fetchall()

def selectWhereExample(conn, fid):
    cursor = conn.cursor()
    sql = "SELECT * FROM BaysApp_flight WHERE id=%d, '%s'"
    cursor.execute(sql %(fid, strg))
    return cursor.fetchall()

def fetchAllBays(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM BaysApp_bay")
    return cursor.fetchall()

def fetchAllAircraft(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM BaysApp_aircraft")
    return cursor.fetchall()

def SelectWBayType(conn, bid):
    cursor = conn.cursor()
    
    sql = ("SELECT * FROM BaysApp_bay WHERE Bay_type_id_id = %d")
    cursor.execute(sql %(bid))
    return cursor.fetchall()

def SelectWAircraftType(conn, aid):
    cursor = conn.cursor()
    
    sql = ("SELECT Tag FROM BaysApp_aircraft WHERE Type_id_id = %d")
    cursor.execute(sql %(aid))
    return cursor.fetchall()

def SelectWAircraftNo(conn, firstid):
    cursor = conn.cursor()
    
    sql = ("SELECT Tag FROM BaysApp_aircraft WHERE id = %d")
    cursor.execute(sql %(firstid))
    return cursor.fetchall()
