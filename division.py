from human import AHuman

class ADivision( object ):
    """docstring for ADivision"""
    def __init__(  self, identifier=0  ):
        super( ADivision, self ).__init__()
        self.__identifier   = identifier
        self.__commander    = None
        self.__soldiers     = {}

        # Equipment
        self.__armours      = 0
        self.__weapons      = 0

        # Tactic skills
        self.__discipline   = 0
        self.__attack       = 0
        self.__defence      = 0
        self.__logistics    = 0
        self.__max_soldiers = 0

        # Additional atributes
        self.__dis_penalty  = 0

    @property 
    def identifier( self ):
        return self.__identifier

    @property 
    def commander( self ):
        return self.__commander

    @property 
    def max_soldiers( self ):
        return self.__max_soldiers

    @property 
    def soldiers( self ):
        return len( self.__soldiers )

    @property
    def dis_penalty( self ):
        return self.__dis_penalty

    @property 
    def armours( self ):
        return self.__armours

    @property 
    def weapons( self ):
        return self.__weapons

    @property 
    def discipline( self ):
        return self.__discipline

    @property 
    def attack( self ):
        return self.__attack

    @property 
    def defence( self ):
        return self.__defence

    @property 
    def logistics( self ):
        return self.__logistics

    def __DefineMaxSoldiers( self ):
        self.__max_soldiers = self.__commander.leadership * 5

    def __DefineDisPenalty( self ):
        if self.__max_soldiers == 0 or self.soldiers < self.__max_soldiers:
            return 0
        else:
            res = len( self.__soldiers ) / float( max_soldiers )

    def __DefineAttack( self ):
        self.__attack = self.__commander.attack.actual

    def __DefineDefence( self ):
        self.__defence = self.__commander.defence.actual

    def __DefineLogistics( self ):
        self.__logistics = self.__commander.logistics.actual

    def __DefineDiscipline( self ):
        dis = 0
        for soldier in self.__soldiers.itervalues():
            dis += soldier.discipline.actual
        if self.__commander is not None:
            dis = float( dis + self.__commander.discipline.actual ) / ( self.soldiers + 1 )
        else:
            dis = float( dis ) / self.soldiers
        return round( dis, 2 ) - self.dis_penalty

    def __DefineArmours( self ):
        armours = 0
        for soldier in self.__soldiers.itervalues():
            armours += soldier.armour 
        if self.__commander is not None:
            armours = float( armours + self.__commander.armour ) / ( self.soldiers +1 )
        else:
            armours = float( armours ) / self.soldiers
        return round( armours, 2 )

    def __DefineWeapons( self ):
        weapons = 0
        for soldier in self.__soldiers.itervalues():
            weapons += soldier.weapon
        if self.__commander is not None:
            weapons = float( weapons + self.__commander.weapon ) / ( self.soldiers + 1 )
        return round( weapons, 2 )

    def __UpdateAllAttributes( self ):
        self.__DefineWeapons()
        self.__DefineArmours()

        self.__DefineMaxSoldiers()

        self.__DefineDiscipline()
        self.__DefineAttack()
        self.__DefineDefence()
        self.__DefineLogistics()

        self.__DefineDisPenalty()

    def SetCommander( self, new_commander ):
        assert type( new_commander ) == AHuman
        self.__commander = new_commander
        self.__UpdateAllAttributes()        

    def RemoveCommander( self ):
        ex_commander = self.__commander
        self.__commander = None
        self.__UpdateAllAttributes()
        return ex_commander

    def AddOneSoldier( self, new_soldier ):
        assert type( new_soldier ) == AHuman
        self.__soldiers[ new_soldier.identifier ] = new_soldier
        self.__UpdateAllAttributes()

    def AddManySoldiers( self, new_soldiers ):
        for soldier in new_soldiers:
            assert type( soldier ) == AHuman
            self.__soldiers[ soldier.identifier ] = soldier
        self.__UpdateAllAttributes()

    def RemoveOneSoldier( self, soldier_id ):
        return self.__soldiers.pop( soldier_id )

    def RemoveAllSoldiers( self ):
        soldiers = list( self.__soldiers.itervalues() )
        self.__soldiers = {}
        self.__UpdateAllAttributes()
        return soldiers
