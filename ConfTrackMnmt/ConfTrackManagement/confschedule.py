from datetime import timedelta,datetime
import datetime as d
import operator
from confevent import ConfEvent
from confslot import ConfSlot

class ConfTrackManagement():
    """
    This class contains scheduling logic. Following is the logic:
      * Read data from file, 
      * create a list of Event objects,
      * sort the list of Events,
      * find out the combination for morning session and evening sessions
    """

    morning=[]#list containing morning talks
    evening=[]#list containing evening talks
    perday=7*60 #max session in a day
    
    def __init__(self,file):
        """
        list of talk events as read from the input saved as Event objects
        This method takes file as a input
        """
        self.talk_list=self.readInput(file)
        self.total_time=self.totaltime(self.talk_list)
        self.schedule(self.talk_list)

    
        #print('start-1ConfTrackManagement:def __init__(self,file): self.talk_list:,self.total_time',self.talk_list,self.total_time)
        #print('end-1')

    def readInput(self,file):
        """
        Read the input file and storing as event object
        This method takes file as a input
        """
        talks = []
        with open(file) as f:
            for line1 in f:
                line=line1.strip()
                title, minutes = line.rsplit(maxsplit=1)
                try:
                    minutes = int(minutes[:-3])
                # negative indexing raises error, so it means it's lightning
                except ValueError:
                    minutes = 5
                event=ConfEvent(line,minutes)
                ##print('event: output :::',event)
                talks.append(event)
        #print('start-2-ConfTrackManagement:readInput(self,file):talks[] :',talks)
        #print('end-2')
        return talks

    def schedule(self,talk_list):
        """
        Schedule events for a list of events
        This method takes list of talks as input
        
        """
        #print('start 4 :ConfTrackManagement:schedule(self,talk_list):totaltime,possibledays,talk_list, self.morning,self.evening',talk_list)
     
        totaltime=self.totaltime(talk_list)
        possibledays=int(totaltime/self.perday)+1
        talk_list.sort(key=operator.attrgetter('duration'))
        #print('totaltime,possibledays,sorted list',totaltime,possibledays,talk_list)

        m=self.combinations(talk_list,possibledays,ConfSlot(3*60))#morning slot
        self.clear(m)#clearing scheduled talk
        #print('clear()')
        evening_slot=ConfSlot(4*60,3*60)
        e=self.combinations(talk_list,possibledays,evening_slot)#evening slot
        self.clear(e) #clearing scheduled talks
        if(self.talk_list):
            raise Exception("Unable to schedule all task for conferencing")
        self.morning=m
        self.evening=e
        #print('end 4 :ConfTrackManagement:schedule(self,talk_list):totaltime,possibledays,talk_list, self.morning,self.evening',totaltime,possibledays,talk_list, self.morning,self.evening)


    def combinations(self,event_list,possibledays,slot):
        """
        This method gives a list of list of events that can be scheduled 
        for given slot
        It takes list of events to be scheduled, possible days and the slot 
        -morning or evening
        """
        #print('Start 6 :ConfTrackManagement : combinations(self,event_list,possibledays,slot:)')

        list_size=len(event_list)
        #print('event_lenght',list_size)
        e=[]
        count=0
        for i in range(list_size):
            start=i
            totaltime=0
            comb=[]
            while(start is not list_size):
                #print('start_value',start)
                curr=start
                start=start+1
                event=event_list[curr]
                #print('event_value',event,event.scheduled,totaltime)
                if event.scheduled or not slot.isValidEvent(event,totaltime):
                    #print('check weather event is true')
                    continue

                comb.append(event)
                #print('comb',comb)
                totaltime=totaltime+event.duration
                #print('totaltime',totaltime)
                if totaltime>=slot.max:
                    #print('breakbyy')
                    break
          
            if slot.isValidSession(totaltime):
                e.append(comb)
                #print('e',e)
                for talk in comb:
                    #marking events selected as scheduled
                    talk.scheduled=True
                count=count+1
                #print('count==possibledays',count,possibledays)
                if count==possibledays:
                    break
        #print('end 6 :ConfTrackManagement : combinations(self,event_list,possibledays,slot:)',list_size,count,e)

        return e

    def totaltime(self,talk_list):
        """
        Total minutes in a list of talks
        This method takes a list as a input
        """
        #print('start-3:ConfTrackManagement:totaltime:' ,sum([event.duration for event in talk_list]))
        #print('end-3')
        #for event in talk_list:
        #    print('loop',event)
        return sum([event.duration for event in talk_list])

    def clear(self,slot_list):
        """
        Clear already scheduled events from list of events
        This method takes list as a input
        """
        for event_list in slot_list:
            for event in event_list:
                #print('start 7:ConfTrackManagement:clear(self,slot_list):event_list,event:::',event_list,event)

                self.talk_list.remove(event)

    def print_output(self):
        """
        This returns a string of output in a required format
        """
        #print("start 8:ConfTrackManagement print_output()::::",len(self.morning))
        format="%I:%M%p"
        out=''
        for day in range(len(self.morning)):
            #print('self.morning)',self.morning)
            date = datetime(1,1,1,hour=9)
            #print('date',date)
            out+="Track " + str(day+1) + ":"+"\n"
            for event in self.morning[day]:
                out+=date.strftime(format)+" "+event.name+"\n"
                date=date+d.timedelta(minutes=event.duration)
            out+=date.strftime(format)+ " Lunch"+"\n"
            date=date+d.timedelta(minutes=60)

            try:#to handle cases where morning session has extra session and no evening session
                for event in self.evening[day]:
                    out+=date.strftime(format)+" "+event.name+"\n"
                    date=date+d.timedelta(minutes=event.duration)
            except:
                pass

            #if evening event finishes before 4PM Network event at 4PM
            #else it is occured at 5PM if it evening slot finished between 4 and 5 PM
            if(date<=datetime(1,1,1,hour=16)):
                date=datetime.min+d.timedelta(hours=16)
            else:
                date=datetime.min+d.timedelta(hours=17)
            out+=date.strftime(format)+ " Network Event"+"\n"+"\n"
            #print('ConfTrackManagement:print_output(self) date=datetime.min+d.timedelta(hours=17)',date,datetime.min+d.timedelta(hours=17))
        
        return out


