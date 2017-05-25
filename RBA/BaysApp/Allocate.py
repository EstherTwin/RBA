import db, dbfunctions
from queue import Queue

c = db.Database().conn()
bid=2
aid=1
firstid=1

flightdata = list(dbfunctions.fetchSchedule(c))
baydata = list(dbfunctions.fetchAllBays(c))
Adata = list(dbfunctions.fetchAllAircraft(c))
B_type = list(dbfunctions.SelectWBayType(c, bid))
A_type = list(dbfunctions.SelectWAircraftType(c, aid))
FAid_type = list(dbfunctions.SelectWAircraftType(c, firstid))

#print(data)
print("The Scheduled flights are:")
print("fNo", "Aid", "AAT","ADT", "MPD", "Date")
for record in flightdata:
    fid = record[0]
    flight_No = record[6]
    aircraft_id = record[5]
    AAT = record[2]
    ADT = record[1]
    MPD = record[3]
    Date = record[4]

    print(flight_No, aircraft_id, AAT, ADT, MPD, Date)

print ("The Aircrafts/Tag are:")
for record in Adata:
    Aid = record[0]
    ATag = record[1]
    Atype_id = record[2]

    print(ATag, '/', Atype_id)


    
print ("print where bay id = 2:")

for record in B_type:
    Bay = record[0]
    Tag = record[1]

    print(Tag)

print ("print where aircraft id = 1:")

for record in A_type:
    ATag = record[0]

    print(ATag)

print ("print Tag where aircraft id = 1:")

for record in FAid_type:
    FATag = record[0]

    print(FATag)

#def dump_queue(Queue):
    #queue_list = []
#for record in flightdata(Queue.get,'STOP'):
    #queue_list.append(record)

#return queue_list
    #i=(queue_list.queue)
    #print (i)

#q = Queue()
#for record in flightdata(q.get,'STOP'):
    #q.put(record)

#print (q.queue)

#Bays=bayTag

def Allocate():
    model = cplex.Cplex()
    model.objective.set_sense(model.objective.sense.maximize)
    model.variables.add(names=Bays)
    




