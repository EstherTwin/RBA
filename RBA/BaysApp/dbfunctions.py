import db

def fetchSchedule(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM BaysApp_schedule ORDER BY ActualDtime")
    return cursor.fetchall()

def fetchAllocations(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM BaysApp_bayallocation ORDER BY StartTime")
    return cursor.fetchall()

def fetchAid(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT Aircraft_id_id FROM BaysApp_schedule")
    return cursor.fetchall()

def fetchFlightNo(conn, aaid):
    cursor = conn.cursor()
    sql = "SELECT flight_id_id FROM BaysApp_schedule WHERE Aircraft_id_id =%d"
    cursor.execute(sql %(aaid))
    return cursor.fetchall()

def fetchActuaArrival(conn, aaid):
    cursor = conn.cursor()
    sql = "SELECT ActualAtime FROM BaysApp_schedule WHERE Aircraft_id_id =%d"
    cursor.execute(sql %(aaid))
    return cursor.fetchall()

def fetchActuaDeparture(conn, aaid):
    cursor = conn.cursor()
    sql = "SELECT ActualDtime FROM BaysApp_schedule WHERE Aircraft_id_id =%d"
    cursor.execute(sql %(aaid))
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

def fetchAllTag(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT Tag FROM BaysApp_aircraft")
    return cursor.fetchall()

def SelectWBayType(conn, Btype_id):
    cursor = conn.cursor()
    
    sql = ("SELECT Bay_Tag FROM BaysApp_bay WHERE Bay_type_id_id = %d")
    cursor.execute(sql %(Btype_id))
    return cursor.fetchall()

def SelectWAircraftType(conn, ATag):
    cursor = conn.cursor()
    
    sql = ("SELECT Type_id_id FROM BaysApp_aircraft WHERE Tag = '%s'")
    cursor.execute(sql %(ATag))
    return cursor.fetchall()

def SelectWAircraftNo(conn, Aid):
    cursor = conn.cursor()
    
    sql = ("SELECT Tag FROM BaysApp_aircraft WHERE id = %d")
    cursor.execute(sql %(Aid))
    return cursor.fetchall()

def SelectWAircraftID(conn, ATag):
    cursor = conn.cursor()
    
    sql = ("SELECT id FROM BaysApp_aircraft WHERE Tag = '%s'")
    cursor.execute(sql %(ATag))
    return cursor.fetchall()

def SelectFlightTag(conn, Fid):
    cursor = conn.cursor()
    
    sql = ("SELECT flight_No FROM BaysApp_flight WHERE id = %d")
    cursor.execute(sql %(Fid))
    return cursor.fetchall()


def InsertBay(conn, bid,fNo,start,end, dat):
    cursor = conn.cursor()
    
    sql = ("INSERT INTO BaysApp_bayallocation"
              "(Bay_id, FlightNo, StartTime, EndTime, Date)" 
              "VALUES ('%s', '%s', '%s', '%s', now())")
    cursor.execute(sql %(bid,fNo,start,end))
    conn.commit()
    return cursor.fetchall()
