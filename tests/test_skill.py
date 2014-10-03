# coding: utf-8

from unittest   import TestCase
from random     import seed, random

from core.skill import ASkill

class ASkillTestCase( TestCase ):
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
