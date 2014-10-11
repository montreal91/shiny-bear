# coding: utf-8

from __future__     import division

from human          import AHuman
from division       import ADivision
from code_constants import PRECISION

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
        return self.__commander

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
        if self.divisions != 0:
            weapons = 0
            for division in self.__divisions.itervalues():
                weapons += division.weapons
            if self.__commander is not None:
                weapons += self.__commander.weapon
                weapons /= ( self.divisions + 1 )
            else:
                weapons /= self.divisions
            self.__weapons = round( weapons, PRECISION )
        elif self.__commander is not None:
            self.__weapons = self.__commander.weapon
        else:
            self.__weapons = 0

    def __DefineArmours( self ):
        if self.divisions != 0:
            armours = 0
            for division in self.__divisions.itervalues():
                armours += division.armours
            if self.__commander is not None:
                armours += self.__commander.armour
                armours /= ( self.divisions + 1 )
            else:
                armours /= self.divisions
            self.__armours = round( armours, PRECISION )
        elif self.__commander is not None:
            self.__armours = self.__commander.armour
        else:
            self.__armours = 0

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
        if self.__commander is None:
            self.__discipline = 0 #???
        elif self.divisions == 0:
            self.__discipline = self.__commander.discipline.actual # ???
        else:
            discipline = 0
            for division in self.__divisions.itervalues():
                discipline += division.discipline
            discipline /= self.divisions
            discipline = discipline * self.__commander.discipline.actual - self.__dis_penalty #???
            self.__discipline = round( discipline, PRECISION )

    def __DefineAttack( self ):
        if self.__commander is None:
            self.__attack = 0
        elif self.divisions == 0:
            self.__attack = self.__commander.attack.actual
        else:
            attack = 0
            for division in self.__divisions.itervalues():
                attack += division.attack
            attack /= self.divisions
            attack = attack * self.__commander.attack.actual #???
            self.__attack = round( attack, PRECISION )

    def __DefineDefence( self ):
        if self.__commander is None:
            self.__defence = 0
        elif self.divisions == 0:
            self.__defence = self.__commander.defence.actual
        else:
            defence = 0
            for division in self.__divisions.itervalues():
                defence += division.defence
            defence /= self.divisions
            defence = defence * self.__commander.defence.actual #???
            self.__defence = round( defence, PRECISION )

    def __DefineLogistics( self ):
        if self.__commander is None:
            self.__logistics = 0
        elif self.divisions == 0:
            self.__logistics = self.__commander.logistics.actual
        else:
            logistics = 0
            for division in self.__divisions.itervalues():
                logistics += division.logistics
            logistics /= self.divisions
            logistics = logistics * self.__commander.logistics.actual #???
            self.__logistics = round( logistics, PRECISION )

    def __UpdateAllAttributes( self ):
        self.__DefineStrength()

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
        assert new_division.identifier not in self.__divisions
        self.__divisions[ new_division.identifier ] = new_division
        self.__UpdateAllAttributes()

    def RemoveDivision( self, ex_div_id ):
        ex_division = self.__divisions.pop( ex_div_id )
        self.__UpdateAllAttributes()
        return ex_division

    def MoveToPosition( self, position ):
        pass
