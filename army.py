from human      import AHuman
from division   import ADivision

class AnArmy( object ):
    """docstring for AnArmy"""
    __slots__ = (
        "__identifier",
        "__commander", "__divisions",
        "__strength",
        "__weapons", "__armours",
        "__max_divisions", "__discipline", "__attack", "__defence", "__logistics",
        "__dis_penalty", "__geo_position",
    )
    def __init__( self, identifier=0 ):
        super( AnArmy, self ).__init__()
        self.__identifier       = identifier

        self.__commander        = None
        self.__divisions        = {}

        self.__strength         = 0 # of troops

        # Equipment
        self.__weapons          = 0
        self.__armours          = 0

        # Tactical characteristics
        self.__max_divisions    = 0
        self.__discipline       = 0
        self.__attack           = 0
        self.__defence          = 0
        self.__logistics        = 0
        
        # Additional field
        self.__dis_penalty      = 0

        self.__geo_position     = ( 0, 0, 0 ) # Placeholder class

    @property 
    def identifier( self ):
        return self.__identifier

    @property 
    def commander( self ):
        return None

    @property 
    def strength( self ):
        return self.__strength

    @property 
    def divisions( self ):
        return len( self.__divisions )

    @property 
    def weapons( self ):
        return self.__weapons

    @property 
    def armours( self ):
        return self.__armours

    @property 
    def max_divisions( self ):
        return self.__max_divisions

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

    @property 
    def geo_position( self ):
        return self.__geo_position

    def __DefineStrength( self ):
        strength            = 0
        for division in self.__divisions.itervalues():
            strength += division.soldiers
            if division.commander is not None:
                strength += 1
        self.__strength     = strength

    def __DefineWeapons( self ):
        weapons         = 0
        for division in self.__divisions.itervalues():
            weapons += division.weapons
        if self.__commander is not None:
            weapons += self.__commander.weapon
            self.__weapons = float( weapons ) / ( self.divisions + 1 )
        else:
            self.__weapons = float( weapons ) / self.divisions
        self.__weapons  = round( self.__weapons, 2 )

    def __DefineArmours( self ):
        armours         = 0
        for division in self.__divisions.itervalues():
            armours += division.armours
        if self.__commander is not None:
            armours += self.__commander.armour
            self.__armours = float( weapons ) / ( self.divisions + 1 )
        else:
            self.__armours = float( armours ) / self.divisions
        self.__armours  = round( self.__armours, 2 )

    def __DefineMaxDivisions( self ):
        if self.__commander is not None:
            self.__max_divisions = self.__commander.leadership.actual
        else:
            self.__max_divisions = 0

    def __DefineDisPenalty( self ):
        if self.divisions <= self.__max_divisions:
            self.__dis_penalty = 0
        else:
            self.__dis_penalty = self.divisions - self.__max_divisions

    def __DefineDiscipline( self ):
        discipline = 0
        for division in self.__divisions.itervalues():
            discipline += division.discipline
        discipline = float( discipline ) / self.divisions
        if self.__commander is not None:
            discipline          = discipline * self.__commander.discipline.actual - self.__dis_penalty # add or multiply that's the question
            self.__discipline   = round( discipline, 2 )
        else:
            self.__discipline = 0 # ???

    def __DefineAttack( self ):
        attack = 0
        for division in self.__divisions.itervalues():
            attack += division.attack
        attack = float( attack ) / self.divisions
        if self.__commander is not None:
            attack          = attack * self.__commander.attack.actual #???
            self.__attack   = round( attack, 2 )
        else:
            self.__attack = 0

    def __DefineDefence( self ):
        defence = 0
        for division in self.__divisions.itervalues():
            defence += division.defence
        defence = float( defence ) / self.divisions
        if self.__commander is not None:
            defence         = defence * self.__commander.defence.actual #???
            self.__defence  = round( defence, 2 )
        else:
            self.__defence = 0

    def __DefineLogistics( self ):
        logistics = 0
        for division in self.__divisions.itervalues():
            logistics += division.logistics
        logistics = float( logistics ) / self.divisions
        if self.__commander is not None:
            logistics           = logistics * self.__commander.logistics.actual #???
            self.__logistics    = round( logistics, 2 )
        else:
            self.__logistics = 0

    def __UpdateAllAttributes( self ):
        # Equipment
        self.__DefineWeapons()
        self.__DefineArmours()

        # Additional attributes
        self.__DefineMaxDivisions()
        self.__DefineDisPenalty()

        # Tactics
        self.__DefineDiscipline()
        self.__DefineAttack()
        self.__DefineDefence()
        self.__DefineLogistics()

    def SetCommander( self, new_commander ):
        assert type( new_commander ) == AHuman
        self.__commander = new_commander
        self.__UpdateAllAttributes()

    def RemoveCommander( self ):
        ex_commander        = self.__commander
        self.__commander    = None
        self.__UpdateAllAttributes()
        return ex_commander

    def AddDivision( self, new_division ):
        assert type( new_division ) == ADivision
        self.__divisions[new_division.identifier] = new_division
        sefl.__UpdateAllAttributes()

    def RemoveDivision( self, ex_div_id ):
        ex_division = self.__divisions.pop( ex_div_id )
        sefl.__UpdateAllAttributes()
        return ex_division

    def MoveToPosition( self, position ):
        pass
