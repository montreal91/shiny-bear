# coding: utf-8

from __future__     import division

from human          import AHuman
from code_constants import PRECISION
from game_constants import DIVISION

class ADivision( object ):
    """docstring for ADivision"""
    __slots__ = (
        "__identifier",
        "__commander", "__soldiers",
        "__weapons", "__armours",
        "__discipline", "__attack", "__defence", "__logistics", "__max_soldiers",
        "__dis_penalty",
    )
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
        if self.__commander is None:
            self.__max_soldiers = 0
        else:
            self.__max_soldiers = self.__commander.leadership.actual * DIVISION[ "COMMANDER_LEADERSHIP_FACTOR" ]

    def __DefineDisPenalty( self ):
        if self.__max_soldiers == 0 or self.soldiers < self.__max_soldiers:
            self.__dis_penalty = 0
        else:
            self.__dis_penalty = len( self.__soldiers ) / self.__max_soldiers

    def __DefineAttack( self ):
        if self.__commander is None:
            self.__attack = 0
        else:
            self.__attack = self.__commander.attack.actual

    def __DefineDefence( self ):
        if self.__commander is None:
            self.__defence = 0
        else:
            self.__defence = self.__commander.defence.actual

    def __DefineLogistics( self ):
        if self.__commander is None:
            self.__logistics = 0
        else:
            self.__logistics = self.__commander.logistics.actual

    def __DefineDiscipline( self ):
        if self.__commander is None:
            self.__discipline = 0
            return
        dis = 0
        for soldier in self.__soldiers.itervalues():
            dis += soldier.discipline.actual
        if self.__commander is not None:
            dis = ( dis + self.__commander.discipline.actual ) / ( self.soldiers + 1 )
        else:
            dis = dis / self.soldiers
        self.__discipline = round( dis, PRECISION ) - self.dis_penalty

    def __DefineArmours( self ):
        if self.soldiers == 0 and self.__commander is None:
            self.__armours = 0
            return
        armours = 0
        for soldier in self.__soldiers.itervalues():
            armours += soldier.armour 
        if self.__commander is not None:
            armours = ( armours + self.__commander.armour ) / ( self.soldiers + 1 )
        else:
            armours = armours / self.soldiers
        self.__armours = round( armours, PRECISION )

    def __DefineWeapons( self ):
        if self.soldiers == 0 and self.__commander is None:
            self.__weapons = 0
            return
        weapons = 0
        for soldier in self.__soldiers.itervalues():
            weapons += soldier.weapon
        if self.__commander is not None:
            weapons = ( weapons + self.__commander.weapon ) / ( self.soldiers + 1 )
        else:
            weapons = weapons / self.soldiers
        self.__weapons = round( weapons, PRECISION )

    def __UpdateAllAttributes( self ):
        self.__DefineWeapons()
        self.__DefineArmours()

        self.__DefineMaxSoldiers()

        self.__DefineDisPenalty()
        self.__DefineDiscipline()
        self.__DefineAttack()
        self.__DefineDefence()
        self.__DefineLogistics()


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
        assert new_soldier.identifier not in self.__soldiers
        self.__soldiers[ new_soldier.identifier ] = new_soldier
        self.__UpdateAllAttributes()

    def AddManySoldiers( self, new_soldiers ):
        for soldier in new_soldiers:
            assert type( soldier ) == AHuman
            assert soldier.identifier not in self.__soldiers
            self.__soldiers[ soldier.identifier ] = soldier
        self.__UpdateAllAttributes()

    def RemoveOneSoldier( self, soldier_id ):
        ex_soldier = self.__soldiers.pop( soldier_id )
        self.__UpdateAllAttributes()
        return ex_soldier

    def RemoveAllSoldiers( self ):
        ex_soldiers = list( self.__soldiers.itervalues() )
        self.__soldiers = {}
        self.__UpdateAllAttributes()
        return ex_soldiers
