# coding: utf-8

from unittest   import TestCase
from random     import seed, randint

from division   import ADivision
from human      import *

class ADivisionTestCase( TestCase ):
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
        with self.assertRaises( AssertionError ):
            div.AddOneSoldier(sol)
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
        with self.assertRaises( AssertionError ):
            div.AddManySoldiers(soldiers)
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
