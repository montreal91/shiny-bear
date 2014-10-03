# coding: utf-8

from unittest   import TestCase

from core       import AnAbstractBuilding

class AnAbstractBuildingTestCase( TestCase ):
    def test_constructor( self ):
        building1 = AnAbstractBuilding()
        self.assertEqual(   building1.cost, 1 )
        self.assertEqual(   building1.complexity, 1 )
        self.assertEqual(   building1.progress, 0 )

        building2 = AnAbstractBuilding( complexity=10, cost=9000 )
        self.assertEqual( building2.cost, 9000 )
        self.assertEqual( building2.complexity, 10 )
        self.assertEqual( building2.progress, 0 )

    def test_build( self ):
        building = AnAbstractBuilding( complexity=10 )
        building.Build( 5 )
        self.assertEqual( building.progress, 50 )
        building.Build( 1 )
        self.assertEqual( building.progress, 60 )
        building.Build( 3 )
        self.assertEqual( building.progress, 90 )
        building.Build( 5 )
        self.assertEqual( building.progress, 100 )

        building = AnAbstractBuilding( complexity=17 )
        building.Build( 3 )
        self.assertEqual( building.progress, 17.65 )
        building.Build( 7 )
        self.assertEqual( building.progress, 58.82 )
        building.Build( 10 )
        self.assertEqual( building.progress, 100 )

    def test_calculate_construction_period( self ):
        building = AnAbstractBuilding( complexity=10 )
        self.assertEqual( building.CalculateConstructionPeriod( 1 ), 10 )
        self.assertEqual( building.CalculateConstructionPeriod( 3 ), 4 )
        self.assertEqual( building.CalculateConstructionPeriod( 5 ), 2 )
        self.assertEqual( building.CalculateConstructionPeriod( 7 ), 2 )
        self.assertEqual( building.CalculateConstructionPeriod( 10 ), 1 )
        self.assertEqual( building.CalculateConstructionPeriod( 20 ), 1 )
        building.Build( 6 )
        self.assertEqual(building.CalculateConstructionPeriod( 1 ), 4 )
        self.assertEqual(building.CalculateConstructionPeriod( 2 ), 2 )
        self.assertEqual(building.CalculateConstructionPeriod( 3 ), 2 )
        self.assertEqual(building.CalculateConstructionPeriod( 4 ), 1 )
        