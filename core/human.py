# coding: utf-8

from __future__     import division
from random         import gauss

from name           import AName
from skill          import ASkill
from game_constants import GENDERS, HUMAN
from code_constants import RECRUIT, SOLDIER, CAPTAIN, GENERAL # Ranks
from code_constants import DISCIPLINE, ATTACK, DEFENCE, LOGISTICS, LEADERSHIP # Skills

class AHuman( object ):
    """docstring for AHuman"""
    __slots__ = ( 
        "__identifier", "__name", "__gender", 
        "__age", "__max_age", "__health", "__alive", "__valid",
        "__armour", "__weapon",
        "__discipline", "__attack", "__defence", "__logistics", "__leadership", 
        "__rank"
    )
    def __init__( self, name=AName(), identifier=0, gender=GENDERS[ "MALE" ] ):
        super( AHuman, self ).__init__()
        self.__identifier   = identifier
        self.__name         = name
        self.__gender       = gender 

        self.__age          = 0
        self.__max_age      = round( gauss( HUMAN[ "GAUSS_MU" ], HUMAN[ "GAUSS_SIGMA" ] ) )
        self.__health       = HUMAN[ "MAX_HEALTH" ]
        self.__alive        = True
        self.__valid        = True

        # Equipment
        self.__armour       = 0
        self.__weapon       = 0

        # Skills
        self.__discipline   = ASkill()
        self.__attack       = ASkill()
        self.__defence      = ASkill()
        self.__logistics    = ASkill()
        self.__leadership   = ASkill()

        self.__rank         = None

    @property 
    def identifier( self ):
        return self.__identifier

    @property 
    def gender( self ):
        return self.__gender

    @property 
    def full_name( self ):
        return self.__name.last_name.upper() + " " + self.__name.first_name + " " + self.__name.second_name

    @property 
    def short_name( self ):
        return self.__name.initials[ 0 ] + ". " + self.__name.initials[ 1 ] + ". " + self.__name.last_name

    @property 
    def age( self ):
        return self.__age

    @property 
    def armour( self ):
        return self.__armour

    @property 
    def weapon( self ):
        return self.__weapon

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
    def leadership( self ):
        return self.__leadership

    @property 
    def rank( self ):
        return self.__rank

    @property 
    def alive( self ):
        return self.__alive

    @property 
    def valid( self ):
        return self.__valid

    @property 
    def wounded( self ):
        return self.__health != HUMAN[ "MAX_HEALTH" ]

    @property 
    def health( self ):
        return self.__health

    @property 
    def average_skill( self ):
        return ( self.discipline.actual + self.attack.actual + self.defence.actual + self.logistics.actual + self.leadership.actual ) / 5

    def __Die( self ):
        self.__alive = False
        self.__valid = False

    def __CheckValidity( self ):
        if self.__health < HUMAN[ "VALIDITY_FACTOR" ]:
            self.__valid = False
        else:
            self.__valid = True

    def AgeUp( self ):
        if self.__alive is True:
            self.__age += 1
        if self.__age >= self.__max_age:
            self.__Die()

    def GetDamage( self, dmg ):
        self.__health -= int( dmg )
        self.__CheckValidity()
        if self.__health <= 0:
            self.__Die()

    def Heal( self, hit_points ):
        self.__health += hit_points
        if self.__health > HUMAN[ "MAX_HEALTH" ]:
            self.__health = HUMAN[ "MAX_HEALTH" ]

    def SetArmour( self, armour ):
        armour = int(armour)
        if armour >= 0:
            self.__armour = armour
        else:
            pass

    def SetWeapon( self, weapon ):
        weapon = int( weapon )
        if weapon >= 0:
            self.__weapon = weapon
        else:
            pass

    def IncreaseSkill( self, skill=None, all_skills=False ):
        if all_skills is True:
            self.__discipline.Increase()
            self.__attack.Increase()
            self.__defence.Increase()
            self.__logistics.Increase()
            self.__leadership.Increase()
        elif skill == DISCIPLINE:
            self.__discipline.Increase()
        elif skill == ATTACK:
            self.__attack.Increase()
        elif skill == DEFENCE:
            self.__defence.Increase()
        elif skill == LOGISTICS:
            self.__logistics.Increase()
        elif skill == LEADERSHIP:
            self.__leadership.Increase()
        else:
            raise AttributeError( "AHuman hasn't such skill." )

    def DecreaseSkills( self ):
        self.__discipline.Decrease()
        self.__attack.Decrease()
        self.__defence.Decrease()
        self.__logistics.Decrease()
        self.__leadership.Decrease()
        
    def SetRank( self, rank ):
        rank = int( rank )
        if 0 <= rank <= 4:
            self.__rank = rank
        else:
            raise AttributeError( "There is no such rank." )
