#Robust Gate Assignment

#the goal is to allocate bays to the selected schedule
#There are certain constraints to consider
#The objectives are:
#Minimize the number of ungated flghts
#Minimize the passenger connection time

import db, dbfunctions

import cplex
c = db.Database().conn()
cursor=c.cursor()


flightdata = list(dbfunctions.fetchSchedule(c))
fetchAid = list(dbfunctions.fetchAid(c))
baydata = list(dbfunctions.fetchAllBays(c))
Adata = list(dbfunctions.fetchAllAircraft(c))
fetchTag = list(dbfunctions.fetchAllTag(c))
fetchAll = list(dbfunctions.fetchAllocations(c))

ATagSql = ("SELECT Tag FROM BaysApp_aircraft WHERE id = %d")
TagA = ("SELECT Type_id_id FROM BaysApp_aircraft WHERE Tag = '%s'")

for record in Adata:
    #global Aid
    Aid = record[0]
    #global ATag
    ATag = record[1]
    Atype_id = record[2]

    print(Aid, ATag, Atype_id)
Ata =[]
Atyd=[]
FNo=[]
index=0
AAt=[]
ADt=[]
FTag=[]
preffered=None
for record in fetchTag:
    global ATag
    ATag =record[0]
    #print ("id",aircraft_id)
    #for item in range(len(aircraft_id))
    Ata=[ATag]
    #print(Aid)
    for items in range(len(Ata)):
        #print("This are the items",Ata[items])
        #i=0
        #while i < len(Aid): 
           #print("After while",index, Aid[i])
           #index+=1 
           #i+=1 
        if Ata[items] !="":
           #print("you are somewhere")
           #if Aid[items]==1:
           #newAid=[]
           #print(Ata[items])
           singleTag= Ata.pop()
           print("The Aircraft Tag is:",singleTag)
           #elif Aid[]
           ATag=singleTag
           #Db functions after getting the Tag
           A_type = list(dbfunctions.SelectWAircraftType(c, ATag))
           A_id = list(dbfunctions.SelectWAircraftID(c, ATag))
           for record in A_id:
              aid=record[0]
              print("The Aircraft id is:", aid)
              FNo=[aid]
              singleAid= FNo.pop()
              aaid=singleAid
           #get flight Number
              FlightNo = list(dbfunctions.fetchFlightNo(c, aaid))
              for record in FlightNo:
                  flightNo=record[0]
                  print ("the flightNo for this is:", flightNo)
                  #get the Flight Tag
                  Ftag=[flightNo]
                  singleFl=Ftag.pop()
                  Fid=singleFl
                  FlightTag = list(dbfunctions.SelectFlightTag(c, Fid))
                  for record in FlightTag:  
                      flight=record[0]
                  
           #get the Actual Arrival time to instert it s the start time
              Arrival = list(dbfunctions.fetchActuaArrival(c, aaid))
              for record in Arrival:
                  startT=record[0]
                  print("The start time is:", startT)
           #get the departure time to be the end time
              Departure = list(dbfunctions.fetchActuaDeparture(c, aaid))
              for record in Departure:
                  startD=record[0]
                  print("The end time is:", startD)
           #The second db funtions for getting the Aircraft type
           for record in A_type:
              AType_id = record[0]
              Atyd=[Atype_id]
              print("Atype is",AType_id)
              singleType= Atyd.pop()
           #Allocate bays according to the Aircraft type
              if AType_id==1:
                 Btype_id=AType_id
                 B_type = list(dbfunctions.SelectWBayType(c, Btype_id))
		#where Bay type is 1
                    #print("One")
                    #print(Tag)
                 if B_type >1:
                       preffered=B_type[0][0]
                       print(".......", preffered)
                 else:
                       preffered=B_type[0]
                       print("Check the tag", preffered)
                 #print("", B_type[0][0])
                 for record in B_type:
                    BTag=record[0]
                    print("There available bays for type 1",BTag)
                    #while i < len(BTag): 
                        #print("After while",index, Aid[i])
                        #index+=1 
                        #i+=1
                        #prefered=
                 bid=preffered
                 fNo=flight
                 start=startT
                 end=startD
                 dat="27/05/2017"
                 Allocate = list(dbfunctions.InsertBay(c, bid,fNo,start,end,dat))
              elif AType_id==2:
                 
		#where Bay type is 2 or 3
                    #print("two")
                 Btype_id=AType_id
                 B_type = list(dbfunctions.SelectWBayType(c, Btype_id))
		#where Bay type is 1
                    #print("One")
                    #print(Tag)
                 if B_type >1:
                       preffered=B_type[0][0]
                       print(".......", preffered)
                 else:
                       preffered=B_type[0]
                       print("Check the tag", preffered)
                 for record in B_type:
                    BTag=record[0]
                    print("There available bays for type 2",BTag)
                    #print(Tag)
                 bid=preffered
                 fNo=flight
                 start=startT
                 end=startD
                 dat="27/05/2017"
                 Allocate = list(dbfunctions.InsertBay(c, bid,fNo,start,end,dat))
              elif AType_id==3:

		#where Bay type is 2 or 3
                 Btype_id=AType_id
                 B_type = list(dbfunctions.SelectWBayType(c, Btype_id))
		#where Bay type is 1
                    #print("One")
                    #print(Tag)
                 if B_type >1:
                       preffered=B_type[0][0]
                       print(".......", preffered)
                 else:
                       preffered=B_type[0]
                       print("Check the tag", preffered)
                 for record in B_type:
                    BTag=record[0]
                    print("There available bays for type 3",BTag)
                    #print(Tag)
                 bid=preffered
                 fNo=flight
                 start=startT
                 end=startD
                 dat="27/05/2017"
                 Allocate = list(dbfunctions.InsertBay(c, bid,fNo,start,end,dat))
                    
              else:
                  print('That Bay does not exist')
              
        else:
           print("Check Again")
        
def All():
    model = cplex.Cplex()
    model.objective.set_sense(model.objective.sense.maximize)
    #model.variables.add(names=aircraft_id)

    for record in fetchAll:
       #global Aid
       alid = record[0]
       #global ATag
       StartT = record[1]
       EndT = record[2]
       Date = record[3]
       Bayid = record[4]
       FlNumber= record[5]

    #spilted=aircraft_id.split()
       #print("The Allocations are:")
       print(FlNumber, Bayid, StartT, EndT, Date)
    
       
    return
if __name__ == "__main__":
    All()
