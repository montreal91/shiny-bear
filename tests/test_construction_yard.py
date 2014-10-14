# coding: utf-8

from unittest               import TestCase

from core                   import AnAbstractBuilding
from core.construction_yard import AConstructionYard

class AConstructionYardTestCase( TestCase ):
    def test_constructor( self ):
        yard = AConstructionYard()
        self.assertEqual( yard.busy_building_modules, 0 )
        self.assertEqual( yard.buildings_under_construction, 0 )

    def test_add_remove_building( self ):
        yard        = AConstructionYard()
        buildings   = [ AnAbstractBuilding( identifier=i, complexity=( i * 10 ) ) for i in xrange( 1, 4 ) ]
        yard.AddBuilding( buildings[ 0 ] )
        self.assertEqual( yard.busy_building_modules, 0 )
        self.assertEqual( yard.buildings_under_construction, 1 )

        yard.AddBuilding( buildings[ 0 ], b_modules=10 )
        self.assertEqual( yard.busy_building_modules, 0 )
        self.assertEqual( yard.buildings_under_construction, 1 )

        yard.AddBuilding( buildings[ 1 ] )
        self.assertEqual( yard.busy_building_modules, 0 )
        self.assertEqual( yard.buildings_under_construction, 2 )

        yard.AddBuilding( buildings[ 2 ], b_modules=5 )
        self.assertEqual( yard.busy_building_modules, 5 )
        self.assertEqual( yard.buildings_under_construction, 3 )

        self.assertEqual( yard.RemoveBuilding( 1 ), 0 )
        self.assertEqual( yard.busy_building_modules, 5 )
        self.assertEqual( yard.buildings_under_construction, 2 )

        self.assertEqual( yard.RemoveBuilding( 0 ), 0 )
        self.assertEqual( yard.busy_building_modules, 5 )
        self.assertEqual( yard.buildings_under_construction, 2 )

        self.assertEqual( yard.RemoveBuilding( 2 ), 0 )
        self.assertEqual( yard.busy_building_modules, 5 )
        self.assertEqual( yard.buildings_under_construction, 1 )

        self.assertEqual( yard.RemoveBuilding( 3 ), 5 )
        self.assertEqual( yard.busy_building_modules, 0 )
        self.assertEqual( yard.buildings_under_construction, 0 )

    def test_add_take_building_modules_to_building( self ):
        yard        = AConstructionYard()
        buildings   = [ AnAbstractBuilding( identifier=i, complexity=( i * 10 ) ) for i in xrange( 1, 4 ) ]
        for builbing in buildings:
            yard.AddBuilding( builbing, b_modules=5 )

        self.assertEqual( yard.buildings_under_construction, 3 )
        self.assertEqual( yard.busy_building_modules, 15 )
        yard.AddBuildingModulesToBuilding( building_id=1, b_modules=5 )
        self.assertEqual( yard.busy_building_modules, 20 )
        yard.AddBuildingModulesToBuilding( building_id=2, b_modules=10 )
        self.assertEqual( yard.busy_building_modules, 30 )
        yard.AddBuildingModulesToBuilding( building_id=3, b_modules=15 )
        self.assertEqual( yard.busy_building_modules, 45 )
        yard.AddBuildingModulesToBuilding( building_id=2, b_modules=0 )
        self.assertEqual( yard.busy_building_modules, 45 )
        yard.AddBuildingModulesToBuilding( building_id=2, b_modules=-30 )
        self.assertEqual( yard.busy_building_modules, 45 )

        self.assertEqual( yard.TakeBuildingModulesFromBuilding( building_id=1, b_modules=-30 ), 0 )
        self.assertEqual( yard.busy_building_modules, 45 )
        self.assertEqual( yard.TakeBuildingModulesFromBuilding( building_id=1, b_modules=3 ), 3 )
        self.assertEqual( yard.busy_building_modules, 42 )
        self.assertEqual( yard.TakeBuildingModulesFromBuilding( building_id=2, b_modules=3 ), 3 )
        self.assertEqual( yard.busy_building_modules, 39 )

        self.assertEqual( yard.TakeBuildingModulesFromBuilding( building_id=1, all_modules=True ), 7 )
        self.assertEqual( yard.busy_building_modules, 32 )
        self.assertEqual( yard.TakeBuildingModulesFromBuilding( building_id=2, all_modules=True ), 12 )
        self.assertEqual( yard.busy_building_modules, 20 )
        self.assertEqual( yard.TakeBuildingModulesFromBuilding( building_id=3, all_modules=True ), 20 )
        self.assertEqual( yard.busy_building_modules, 0 )

    def test_construct_pop_ready_buildings( self ):
        yard        = AConstructionYard()
        buildings   = [ AnAbstractBuilding( identifier=i, complexity=( i * 10 ) ) for i in xrange( 1, 4 ) ]
        for builbing in buildings:
            yard.AddBuilding( builbing, b_modules=10 )

        self.assertEqual( yard.buildings_under_construction, 3 )
        self.assertEqual( yard.busy_building_modules, 30 )

        yard.Construct()
        out = yard.PopReadyBuildings()
        self.assertEqual( out.b_modules, 10 )
        self.assertEqual( len( out.buildings ), 1 )
        self.assertEqual( out.buildings[ 0 ], buildings[ 0 ] )
        self.assertEqual( yard.buildings_under_construction, 2 )
        self.assertEqual( yard.busy_building_modules, 20 )

        yard.Construct()
        out = yard.PopReadyBuildings()
        self.assertEqual( out.b_modules, 10 )
        self.assertEqual( len( out.buildings ), 1 )
        self.assertEqual( out.buildings[ 0 ], buildings[ 1 ] )
        self.assertEqual( yard.buildings_under_construction, 1 )
        self.assertEqual( yard.busy_building_modules, 10 )

        yard.AddBuilding( AnAbstractBuilding( identifier=5, complexity=10 ), 10 )
        yard.Construct()
        out = yard.PopReadyBuildings()
        self.assertEqual( out.b_modules, 20 )
        self.assertEqual( len(out.buildings), 2 )
        self.assertEqual( yard.buildings_under_construction, 0 )
        self.assertEqual( yard.busy_building_modules, 0 )
        self.assertTrue( buildings[ 2 ] in out.buildings )
