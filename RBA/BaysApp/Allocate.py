import db, dbfunctions
#from queue import Queue
import cplex


c = db.Database().conn()
global Btype, ATag, Aid, AType
Btype_id=3
ATag='KQ125'
Aid=4
AType_id=2

flightdata = list(dbfunctions.fetchSchedule(c))
baydata = list(dbfunctions.fetchAllBays(c))
Adata = list(dbfunctions.fetchAllAircraft(c))
A_type = list(dbfunctions.SelectWAircraftType(c, ATag))
FAid_type = list(dbfunctions.SelectWAircraftNo(c, Aid))



#print(data)
#print("The Scheduled flights are:")
#print("fNo", "Aid", "AAT","ADT", "MPD", "Date")


    #print(flight_No, aircraft_id, AAT, ADT, MPD, Date)

print ("The Aircrafts/Tag are:")
for record in Adata:
    #global Aid
    Aid = record[0]
    #global ATag
    ATag = record[1]
    Atype_id = record[2]

    print(ATag, Aid)

for record in baydata:
    bay_id = record[0]
    bay_Tag = record[1]
    #global Btype_id
    Btype_id = record[2]
    print("This is the Bid", Btype_id)

ATag=[]
for record in FAid_type:
    FATag = record[0]
    ATag.append(FATag)

    print("Recently Added", ATag)

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
B_type = list(dbfunctions.SelectWBayType(c, Btype_id))
#print (q.queue)
for record in B_type:
    Tag = record[0]
#where Bay type is 2 or 3
    print(Tag)

Bays=Tag



def Allocate():
    model = cplex.Cplex()
    model.objective.set_sense(model.objective.sense.maximize)
    model.variables.add(names=Bays)
    model.variables.get_names()
    #for record in FAid_type:
        #FATag = record[0]
    global Btype, ATag, Aid, AType

    print("Scheuled flights......")
    Aid= []
    for record in flightdata:
        fid = record[0]
        flight_No = record[6]
        aircraft_id = record[5]
        AAT = record[2]
        ADT = record[1]
        MPD = record[3]
        Date = record[4]
        Aid.append(aircraft_id)
        print (Aid)
        #print(flight_No, aircraft_id, AAT, ADT, MPD, Date)
        #get aircraft tag using the aircraft id
    
         #get the aircraft type using the tag
    for record in A_type:
        global AType_id 
        AType_id = record[0]

        print("Used Atype",AType_id)
        #AType_id=3
	#check if the aircraft type id is null
        if AType_id>0:
            print("Loading....." )
            #print(ATag, Aid, Btype_id)
		#where Bay type is 1=2
            print("The AType is ..", AType_id)
	#if the aircraft id =1 then that means its a wide body and can only be parked in an 
	#enclosed bay, so we print Bays Availabe where bay type is 1
            if AType_id==1:
                for record in B_type:
                    Tag = record[0]
		#where Bay type is 1
                    #print("One")
                    print(Tag)
                    #print(ATag, Aid, Btype_id)
            elif AType_id==2:
                for record in B_type:
                    Tag = record[0]
		#where Bay type is 2 or 3
                    print("two")
                    #print(Tag)
            elif AType_id==3:
                for record in B_type:
                    Tag = record[0]
		#where Bay type is 2 or 3
                    print("Three")
                    print(Tag)
            else:
                print('That Bay does not exist')
        else:
            print("Check the AType")
               
                

    return
if __name__ == "__main__":
    Allocate()

def Assign():
 
    print("You have made it")
    return
if __name__ == "__main__":
    Assign()



