  
class Agent
    def __init__(self)
        def program(percept)abstracta
        self.program=program
        
class vaccumEnvironment

    def __init__(self)
        self.status={ loc_Arandom.choice(['Clean','Dirty']),
                      loc_Brandom.choice(['Clean','Dirty']),
                      loc_Crandom.choice(['Clean','Dirty']),
                      loc_Drandom.choice(['Clean','Dirty'])
                      }
    def add_object(self,object,location=None)
        object.location=location or self.default_location(object)

    def default_location(self,object)
        return random.choice([loc_A,loc_B,loc_C,loc_D])

    def percept(self,agent)
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action)
        if action=='Right'
            if agent.location==loc_A agent.location= loc_B
            elif agent.location==loc_C agent.location= loc_D
        elif action=='Left'
            if agent.location==loc_B agent.location= loc_A
            elif agent.location==loc_D agent.location= loc_C
        elif action=='Up'
            if agent.location==loc_C agent.location= loc_A
            elif agent.location==loc_D agent.location= loc_B
        elif action=='Down'
            if agent.location==loc_A agent.location= loc_C
            elif agent.location==loc_B agent.location= loc_D
        elif action=='Suck'
            #if self.status[agent.location]=='Dirty'
            self.status[agent.location]='Clean'


loc_A,loc_B='A','B'
loc_C,loc_D='C','D'

class reflexVaccumAgent(Agent)
    def __init__(self)
        Agent.__init__(self)

        action=' '

        def program(percept)

            location=percept[0]
            status=percept[1]
            
            if status=='Dirty' action= 'Suck'
            elif location==loc_A action= random.choice(['Right','Down'])
            elif location==loc_B action= random.choice(['Left','Down'])
            elif location==loc_C action= random.choice(['Right','Up'])
            elif location==loc_D action= random.choice(['Left','Down'])

            percept=(location,status)
            print('Agent perceives %s and does %s'%(percept,action))

            return action
        
            
            
        self.program=program

            
Ragent=reflexVaccumAgent()
env=vaccumEnvironment()
env.add_object(Ragent)
for steps in range(20)
    action=Ragent.program(env.percept(Ragent))
    env.execute_action(Ragent,action)


