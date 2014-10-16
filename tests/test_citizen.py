# coding: utf-8

from unittest import TestCase
from random import seed

from core.citizen import ACitizen
from core.game_constants import GENDERS

class ACitizenTestCase( TestCase ):
    def setUp( self ):
        self.male   = GENDERS[ "MALE" ]
        self.female = GENDERS[ "FEMALE" ]
        seed( 42 )

    def test_constructor( self ):
        citizen = ACitizen()
        self.assertEqual( citizen.gender, self.male )
        self.assertEqual( citizen.age, 0 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, True )

        citizen = ACitizen( gender=self.female )
        self.assertEqual( citizen.gender, self.female )
        self.assertEqual( citizen.age, 0 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, True )

        citizen = ACitizen( gender=self.male )
        self.assertEqual( citizen.gender, self.male )
        self.assertEqual( citizen.age, 0 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, True )

        citizen = ACitizen( age=10, gender=self.male )
        self.assertEqual( citizen.gender, self.male )
        self.assertEqual( citizen.age, 10 )
        self.assertEqual( citizen.max_age, 68 )
        self.assertEqual( citizen.alive, True )

        citizen = ACitizen( age=20, gender=self.female )
        self.assertEqual( citizen.gender, self.female )
        self.assertEqual( citizen.age, 20 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, True )

    def test_age_up( self ):
        citizen = ACitizen()
        self.assertEqual( citizen.age, 0 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, True )

        citizen.AgeUp()
        self.assertEqual( citizen.age, 1 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, True )

        citizen.AgeUp()
        self.assertEqual( citizen.age, 2 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, True )

        citizen.AgeUp()
        self.assertEqual( citizen.age, 3 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, True )

        citizen = ACitizen( age=64 )
        self.assertEqual( citizen.age, 64 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, True )

        citizen.AgeUp()
        self.assertEqual( citizen.age, 65 )
        self.assertEqual( citizen.max_age, 64 )
        self.assertEqual( citizen.alive, False )

    def test_give_birth( self ):
        citizen = ACitizen()
        while citizen.alive:
            self.assertEqual( citizen.GiveBirth(), None )
            citizen.AgeUp()

        citizen = ACitizen( gender=self.female )
        while citizen.alive:
            if citizen.age == 22:
                child = citizen.GiveBirth()
                self.assertEqual( child.age, 0 )
                self.assertEqual( child.gender, self.male )
                self.assertEqual( child.max_age, 58 )
            elif citizen.age == 24:
                child = citizen.GiveBirth()
                self.assertEqual( child.age, 0 )
                self.assertEqual( child.gender, self.male )
                self.assertEqual( child.max_age, 58 )
            elif citizen.age == 29:
                child = citizen.GiveBirth()
                self.assertEqual( child.age, 0 )
                self.assertEqual( child.gender, self.female )
                self.assertEqual( child.max_age, 62 )
            else:
                self.assertEqual( citizen.GiveBirth(), None )
            citizen.AgeUp()
            