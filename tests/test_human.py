# coding: utf-8

from unittest   import TestCase
from random     import seed

from core.name  import AName
from core.human import *

class AHumanTestCase( TestCase ):
    def setUp( self ):
        seed( 42 )

    def test_constructor( self ):
        human1 = AHuman()
        self.assertTrue( human1.full_name       == "FAWKES Guy Ronald" )
        self.assertTrue( human1.short_name      == "G. R. Fawkes" )
        self.assertTrue( human1.identifier      == 0 )
        self.assertTrue( human1.age             == 0) 
        self.assertTrue( human1.gender          == MALE )
        self.assertTrue( human1.health          == 100 )
        self.assertTrue( human1.alive   is True )
        self.assertTrue( human1.valid   is True )
        self.assertTrue( human1.wounded is False )
        self.assertTrue( human1.armour          == 0 )
        self.assertTrue( human1.weapon          == 0 )
        self.assertTrue( human1.average_skill   == 0 )
        self.assertTrue( human1.rank            == None )

        name    = AName( first_name="Ada", second_name="King", last_name="Lovelace" )
        human2  = AHuman( name=name, identifier=1815, gender=FEMALE )
        self.assertTrue( human2.full_name       == "LOVELACE Ada King" )
        self.assertTrue( human2.short_name      == "A. K. Lovelace" )
        self.assertTrue( human2.identifier      == 1815 )
        self.assertTrue( human2.age             == 0 )
        self.assertTrue( human2.gender          == FEMALE )
        self.assertTrue( human2.health          == 100 )
        self.assertTrue( human2.alive   is True )
        self.assertTrue( human2.wounded is False )
        self.assertTrue( human2.valid   is True )
        self.assertTrue( human2.armour          == 0 )
        self.assertTrue( human2.weapon          == 0 )
        self.assertTrue( human2.average_skill   == 0 )
        self.assertTrue( human2.rank            == None )


    def test_age_up( self ):
        human = AHuman()
        for i in xrange( 40 ):
            human.AgeUp()
        self.assertTrue( human.age == 40 )
        self.assertTrue( human.alive is True )
        for i in xrange( 40 ):
            human.AgeUp()
        self.assertTrue( human.age == 64 )
        self.assertTrue( human.alive is False )

    def test_health_damage_heal( self ):
        human = AHuman()
        human.GetDamage( 30 )
        self.assertTrue( human.health == 70 )
        self.assertTrue( human.alive    is True )
        self.assertTrue( human.valid    is True )
        self.assertTrue( human.wounded  is True )
        human.Heal( 10 )
        self.assertTrue( human.health == 80 )
        human.Heal( 30 )
        self.assertTrue( human.health == 100 )
        self.assertTrue( human.wounded  is False )
        self.assertTrue( human.valid    is True )
        human.GetDamage( 60 )
        self.assertTrue( human.health == 40 )
        self.assertTrue( human.alive    is True )
        self.assertTrue( human.wounded  is True )
        self.assertTrue( human.valid    is False )
        human.Heal( 50 )
        self.assertTrue( human.health == 90 )
        self.assertTrue( human.wounded  is True )
        self.assertTrue( human.valid    is False )
        human.GetDamage( 100 )
        self.assertTrue( human.alive    is False )

    def test_armour_and_weapon(self):
        human = AHuman()
        self.assertTrue( human.armour == 0 )
        self.assertTrue( human.weapon == 0 )
        human.SetWeapon( 10 )
        human.SetArmour( 20 )
        self.assertTrue( human.armour == 20 )
        self.assertTrue( human.weapon == 10 )
        human.SetArmour( 20 )
        human.SetWeapon( 5 )
        self.assertTrue( human.armour == 20 )
        self.assertTrue( human.weapon == 5 )

    def test_skills( self ):
        human = AHuman()
        human.IncreaseSkill( all_skills=True )
        self.assertTrue( human.discipline.actual    == 2 )
        self.assertTrue( human.attack.actual        == 3 )
        self.assertTrue( human.defence.actual       == 1 )
        self.assertTrue( human.logistics.actual     == 2 )
        self.assertTrue( human.leadership.actual    == 2 )
        human.IncreaseSkill( DISCIPLINE )
        human.IncreaseSkill( ATTACK )
        human.IncreaseSkill( DEFENCE )
        human.IncreaseSkill( LOGISTICS )
        human.IncreaseSkill( LEADERSHIP )
        self.assertTrue( human.discipline.actual    == 4 )
        self.assertTrue( human.attack.actual        == 6 )
        self.assertTrue( human.defence.actual       == 2 )
        self.assertTrue( human.logistics.actual     == 4 )
        self.assertTrue( human.leadership.actual    == 4 )
        human.DecreaseSkills()
        self.assertTrue( human.discipline.actual    == 2 )
        self.assertTrue( human.attack.actual        == 5 )
        self.assertTrue( human.defence.actual       == 0 )
        self.assertTrue( human.logistics.actual     == 2 )
        self.assertTrue( human.leadership.actual    == 2 )
        self.assertTrue( human.average_skill        == 2.2 )

    def test_ranks( self ):
        human = AHuman()
        self.assertTrue( human.rank is None )
        human.SetRank( RECRUIT )
        self.assertTrue( human.rank == RECRUIT )
        human.SetRank( SOLDIER )
        self.assertTrue( human.rank == SOLDIER )
        human.SetRank( CAPTAIN )
        self.assertTrue( human.rank == CAPTAIN )
        human.SetRank( GENERAL )
        self.assertTrue( human.rank == GENERAL )
        with self.assertRaises( AttributeError ):
            human.SetRank( 8 )
        with self.assertRaises( ValueError ):
            human.SetRank( "r" )
