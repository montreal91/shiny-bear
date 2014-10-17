# coding: utf-8

from unittest import TestCase
from random import seed

from core.population import APopulation
from core.game_constants import POPULATION

class APopulationTestCase( TestCase ):
    def setUp( self ):
        seed( 42 )

    def test_constructor( self ):
        popln = APopulation()
        self.assertEqual( popln.total_population, 0 )
        self.assertEqual( popln.ever_lived, 0 )
        self.assertEqual( popln.military_aged, 0 )

        popln = APopulation( starting_population=200 )
        self.assertEqual( popln.total_population, 200 )
        self.assertEqual( popln.ever_lived, 200 )
        self.assertEqual( popln.military_aged, 2 )

    def test_live_one_year( self ):
        popln = APopulation()
        popln.LiveOneYear()
        self.assertEqual( popln.total_population, 0 )
        self.assertEqual( popln.ever_lived, 0 )
        self.assertEqual( popln.military_aged, 0 )

        popln = APopulation( starting_population=200 )
        self.assertEqual( popln.total_population, 200 )
        self.assertEqual( popln.ever_lived, 200 )
        self.assertEqual( popln.military_aged, 2 )

        for i in xrange( 20 ):
            popln.LiveOneYear()

        self.assertEqual( popln.total_population, 301 )
        self.assertEqual( popln.ever_lived, 325 )
        self.assertEqual( popln.military_aged, 7 )

    def test_take_military_aged( self ):
        popln = APopulation( starting_population=200 )
        self.assertEqual( popln.total_population, 200 )
        self.assertEqual( popln.ever_lived, 200 )
        self.assertEqual( popln.military_aged, 2 )
        recruits = popln.TakeMilitaryAged()

        self.assertEqual( len ( recruits ), 2 )
        self.assertEqual( popln.military_aged, 0 )
        self.assertEqual( popln.total_population, 198 )

        for recruit in recruits:
            self.assertEqual( recruit.age, 16 )

        for i in xrange( 20 ):
            popln.LiveOneYear()

        self.assertEqual( popln.total_population, 293 )
        self.assertEqual( popln.ever_lived, 319 )
        self.assertEqual( popln.military_aged, 5 )

        recruits = popln.TakeMilitaryAged()
        self.assertEqual( len( recruits ), 5 )
        self.assertEqual( popln.military_aged, 0 )
        self.assertEqual( popln.total_population, 288 )

        for recruit in recruits:
            self.assertEqual( recruit.age, 16 )
