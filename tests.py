import unittest

from random     import seed, random, randint
from skill      import ASkill
from name       import AName
from human      import *
from division   import ADivision

class ASkillTestCase( unittest.TestCase ):
    def setUp( self ):
        seed( 42 )

    def test_creation( self ):
        skill = ASkill()
        self.assertTrue( skill.talent    == 2 )
        self.assertTrue( skill.maximum   == 14 )
        self.assertTrue( skill.actual    == 0 )
        with self.assertRaises( AttributeError ):
            skill.actual = 3
        with self.assertRaises( AttributeError ):
            skill.maximum = 4
        with self.assertRaises( AttributeError ):
            skill.talent = 8

    def test_increase( self ):
        skill   = ASkill()
        for i in xrange( 3 ):
            random()
        skill1  = ASkill()
        skill2  = ASkill()
        for i in xrange( 5 ):
            skill.Increase()
            skill1.Increase()
            skill2.Increase()
        self.assertTrue( skill.actual    == 10 )
        self.assertTrue( skill1.actual   == 5 )
        self.assertTrue( skill2.actual   == 15 )
        for i in xrange( 5 ):
            skill.Increase()
            skill1.Increase()
            skill2.Increase()
        self.assertTrue( skill.actual    == 14 )
        self.assertTrue( skill.actual    == skill.maximum )
        self.assertTrue( skill1.actual   == 6 )
        self.assertTrue( skill1.actual   == skill1.maximum )
        self.assertTrue( skill2.actual   == 18 )
        self.assertTrue( skill2.actual   == skill2.maximum )

    def test_decrease( self ):
        for i in xrange( 3 ):
            random()
        skill1 = ASkill()
        skill2 = ASkill()
        skill3 = ASkill()
        skill1.Decrease()
        skill2.Decrease()
        skill3.Decrease()
        self.assertTrue( skill1.actual == 0 )
        self.assertTrue( skill2.actual == 0 )
        self.assertTrue( skill3.actual == 0 )
        for i in xrange( 5 ):
            skill1.Increase()
            skill2.Increase()
            skill3.Increase()
        skill1.Decrease()
        skill2.Decrease()
        skill3.Decrease()
        self.assertTrue( skill1.actual == 8 )
        self.assertTrue( skill2.actual == 2 )
        self.assertTrue( skill3.actual == 14 )

class AHumanTestCase( unittest.TestCase ):
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

class ADivisionTestCase( unittest.TestCase ):
    def setUp( self ):
        seed( 42 )

    def test_constructor( self ):
        div1 = ADivision()
        self.assertTrue( div1.identifier    == 0 )
        self.assertTrue( div1.soldiers      == 0 )
        self.assertTrue( div1.max_soldiers  == 0 )
        self.assertTrue( div1.discipline    == 0 )
        self.assertTrue( div1.attack        == 0 )
        self.assertTrue( div1.defence       == 0 )
        self.assertTrue( div1.logistics     == 0 )
        self.assertTrue( div1.weapons        == 0 )
        self.assertTrue( div1.armours        == 0 )
        self.assertTrue( div1.dis_penalty   == 0 )
        self.assertTrue( div1.commander is None )
        div2 = ADivision( identifier=69 )
        self.assertTrue( div2.identifier    == 69 )

    def test_set_remove_commander( self ):
        div         = ADivision( identifier=69 )
        commander   = AHuman()
        commander.SetRank( CAPTAIN )
        commander.SetWeapon( 10 )
        commander.SetArmour( 9 )
        for i in range( 20 ):
            commander.IncreaseSkill( all_skills=True )
        div.SetCommander( commander )
        self.assertTrue( div.commander      == commander )
        self.assertTrue( div.max_soldiers   == 80 )
        self.assertTrue( div.soldiers       == 0 )
        self.assertTrue( div.discipline     == 14 )
        self.assertTrue( div.attack         == 14 )
        self.assertTrue( div.defence        == 17 )
        self.assertTrue( div.logistics      == 14 )
        self.assertTrue( div.weapons        == 10 )
        self.assertTrue( div.armours        == 9 )
        self.assertTrue( div.dis_penalty    == 0 )

        ex_captain  = div.RemoveCommander()
        self.assertTrue( ex_captain          == commander )
        self.assertTrue( div.commander is None )
        self.assertTrue( div.max_soldiers    == 0 )
        self.assertTrue( div.soldiers        == 0 )
        self.assertTrue( div.discipline      == 0 )
        self.assertTrue( div.attack          == 0 )
        self.assertTrue( div.defence         == 0 )
        self.assertTrue( div.logistics       == 0 )
        self.assertTrue( div.weapons         == 0 )
        self.assertTrue( div.armours         == 0 )
        self.assertTrue( div.dis_penalty     == 0 )

    def test_add_remove_one_soldier( self ):
        sol = AHuman( identifier=9 )
        div = ADivision( identifier=69 )
        sol.SetWeapon( 5 )
        sol.SetArmour( 4 )
        div.AddOneSoldier( sol )
        with self.assertRaises( AssertionError ):
            div.AddOneSoldier( 9000 )
        self.assertTrue( div.soldiers        == 1 )
        self.assertTrue( div.weapons         == 5 )
        self.assertTrue( div.armours         == 4 )
        div.RemoveOneSoldier( 9 )
        self.assertTrue( div.soldiers        == 0 )
        self.assertTrue( div.weapons         == 0 )
        self.assertTrue( div.armours         == 0 )
        with self.assertRaises( KeyError ):
            div.RemoveOneSoldier( 9 )

    def test_add_remove_many_soldiers( self ):
        div = ADivision( identifier=69 )
        cap = AHuman()
        cap.SetWeapon(10)
        cap.SetArmour(12)
        soldiers = [AHuman(identifier=i) for i in range(100)]
        for soldier in soldiers:
            for i in range(5):
                soldier.IncreaseSkill(skill=DISCIPLINE)
            soldier.SetWeapon(randint(5,6))
            soldier.SetArmour(randint(3,4))
            cap.IncreaseSkill(all_skills=True)
        div.AddManySoldiers(soldiers)
        self.assertTrue( div.soldiers      == 100 )
        self.assertTrue( div.max_soldiers  == 0 )
        self.assertTrue( div.discipline    == 0 )
        self.assertTrue( div.attack        == 0 )
        self.assertTrue( div.defence       == 0 )
        self.assertTrue( div.logistics     == 0 )
        self.assertTrue( div.dis_penalty   == 0 )
        self.assertTrue( div.weapons       == 5.44 )
        self.assertTrue( div.armours       == 3.51 )
        div.SetCommander(cap)
        self.assertTrue( div.discipline     == 8.22 )
        self.assertTrue( div.attack         == 14 )
        self.assertTrue( div.defence        == 17 )
        self.assertTrue( div.logistics      == 14 )
        self.assertTrue( div.weapons        == 5.49 )
        self.assertTrue( div.armours        == 3.59 )
        self.assertTrue( div.max_soldiers   == 80 )
        self.assertTrue( div.dis_penalty    == 1.25 )
        div.RemoveAllSoldiers()
        self.assertTrue( div.soldiers       == 0 )
        self.assertTrue( div.discipline     == 14 )
        self.assertTrue( div.weapons        == 10 )
        self.assertTrue( div.armours        == 12 )
        self.assertTrue( div.dis_penalty    == 0 )

if __name__ == '__main__':
    unittest.main()
