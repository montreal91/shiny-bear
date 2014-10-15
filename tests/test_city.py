# coding: utf-8

from unittest                   import TestCase

from core.city                  import ACity
from core.military_university   import AMilitaryUniversity
from core.soldier_school        import ASoldierSchool

from core.code_constants        import STATUS_CODES
from core.game_constants        import BUILDING_MODULE_PRICE, BUILDINGS, SPECIALIZATIONS

class ACityTestCase( TestCase ):
    def setUp(self):
        self.weapons = SPECIALIZATIONS[ "WEAPONS" ]
    def test_constructor_and_properties( self ):
        city        = ACity()
        self.assertEqual( city.identifier, 0 )
        self.assertEqual( city.title, "Rome" )
        self.assertEqual( city.avaiable_building_modules, 0 )
        self.assertEqual( city.busy_building_modules, 0 )
        self.assertEqual( city.buildings, tuple() )
        self.assertEqual( city.number_of_buildings, 0 )

        city.title  = "New York"
        self.assertEqual( city.title, "New York" )

        city        = ACity( identifier=complex( 1, 2 ), title="Montreal" )
        self.assertEqual( city.identifier.real, 1 )
        self.assertEqual( city.identifier, complex( 1, 2 ) )
        self.assertNotEqual( city.identifier, ( 1, 2 ) )
        self.assertEqual( city.title, "Montreal" )
        self.assertEqual( city.avaiable_building_modules, 0 )
        self.assertEqual( city.busy_building_modules, 0 )
        self.assertEqual( city.buildings, tuple() )
        self.assertEqual( city.number_of_buildings, 0 )

    def test_buy_sell_building_modules( self ):
        city = ACity()
        self.assertEqual( city.avaiable_building_modules, 0 )

        self.assertEqual( city.BuyBuildingModules(), 0 )
        self.assertEqual( city.avaiable_building_modules, 0 )
        self.assertEqual( city.BuyBuildingModules( -5 ), 0 )
        self.assertEqual( city.avaiable_building_modules, 0 )
        self.assertEqual( city.BuyBuildingModules( 0.9 ), 0 )
        self.assertEqual( city.avaiable_building_modules, 0 )
        self.assertEqual( city.BuyBuildingModules( 12 ), BUILDING_MODULE_PRICE * 12 )
        self.assertEqual( city.avaiable_building_modules, 12 )
        self.assertEqual( city.BuyBuildingModules( 13 ), BUILDING_MODULE_PRICE * 13 )
        self.assertEqual( city.avaiable_building_modules, 25 )

        self.assertEqual( city.SellBuildingModules(), 0 )
        self.assertEqual( city.avaiable_building_modules, 25 )
        self.assertEqual( city.SellBuildingModules( - 5), 0 )
        self.assertEqual( city.avaiable_building_modules, 25 )
        self.assertEqual( city.SellBuildingModules( 0.8 ), 0 )
        self.assertEqual( city.avaiable_building_modules, 25 )
        self.assertEqual( city.SellBuildingModules( 5 ), BUILDING_MODULE_PRICE * 5 / 2 )
        self.assertEqual( city.avaiable_building_modules, 20 )
        self.assertEqual( city.SellBuildingModules( 30 ), BUILDING_MODULE_PRICE * 20 / 2 )
        self.assertEqual( city.avaiable_building_modules, 0 )
        self.assertEqual( city.SellBuildingModules( 30 ), 0 )
        self.assertEqual( city.avaiable_building_modules, 0 )

        city.BuyBuildingModules( 20 )
        self.assertEqual( city.avaiable_building_modules, 20 )
        self.assertEqual( city.SellBuildingModules( all_modules=True ), BUILDING_MODULE_PRICE * 20 / 2 )

    def test_start_abort_construction( self ):
        city = ACity( identifier=1 )

        self.assertEqual( city.StartConstruction( BUILDINGS.MILITARY_UNIVERSITY.SHORT_NAME ), BUILDINGS.MILITARY_UNIVERSITY.COST )
        self.assertEqual( city.StartConstruction( BUILDINGS.SOLDIER_SCHOOL.SHORT_NAME ), BUILDINGS.SOLDIER_SCHOOL.COST )
        self.assertEqual( city.StartConstruction( BUILDINGS.FACTORY.SHORT_NAME ), STATUS_CODES.FAILURE )
        self.assertEqual( city.StartConstruction( BUILDINGS.FACTORY.SHORT_NAME, specialization=self.weapons ), BUILDINGS.FACTORY.COST )
        self.assertEqual( city.StartConstruction( BUILDINGS.WAREHOUSE.SHORT_NAME, specialization=self.weapons ), BUILDINGS.WAREHOUSE.COST )

        self.assertEqual( city.AbortConstruction( complex( 1, 1 ) ), BUILDINGS.MILITARY_UNIVERSITY.COST )
        self.assertEqual( city.AbortConstruction( complex( 1, 2 ) ), BUILDINGS.SOLDIER_SCHOOL.COST )
        self.assertEqual( city.AbortConstruction( complex( 1, 3 ) ), BUILDINGS.FACTORY.COST )
        self.assertEqual( city.AbortConstruction( complex( 1, 4 ) ), BUILDINGS.WAREHOUSE.COST )

    def test_add_reduce_building_modules_to_at_building( self ):
        city    = ACity( identifier=2 )
        city.BuyBuildingModules( 50 )
        for i in xrange( 5 ):
            city.StartConstruction( BUILDINGS.SOLDIER_SCHOOL.SHORT_NAME )

        self.assertEqual( city.avaiable_building_modules, 50 )
        self.assertEqual( city.busy_building_modules, 0 )

        res     = city.AddBuildingModulesToBuilding( building_id=complex( 2, 1 ), b_modules=5 )
        self.assertEqual( res, STATUS_CODES.SUCCESS )
        self.assertEqual( city.avaiable_building_modules, 45 )
        self.assertEqual( city.busy_building_modules, 5 )

        res     = city.AddBuildingModulesToBuilding( building_id=complex( 2, 2 ), b_modules=10 )
        self.assertEqual( res, STATUS_CODES.SUCCESS )
        self.assertEqual( city.avaiable_building_modules, 35 )
        self.assertEqual( city.busy_building_modules, 15 )

        res     = city.AddBuildingModulesToBuilding( building_id=complex( 2, 3 ), b_modules=15 )
        self.assertEqual( res, STATUS_CODES.SUCCESS )
        self.assertEqual( city.avaiable_building_modules, 20 )
        self.assertEqual( city.busy_building_modules, 30 )

        res     = city.AddBuildingModulesToBuilding( building_id=complex( 2, 4 ), b_modules=20  )
        self.assertEqual( res, STATUS_CODES.SUCCESS )
        self.assertEqual( city.avaiable_building_modules, 0 )
        self.assertEqual( city.busy_building_modules, 50 )

        city.BuyBuildingModules( 10 )
        res     = city.AddBuildingModulesToBuilding( building_id=complex( 1, 2 ), all_modules=True )
        self.assertEqual( res, STATUS_CODES.FAILURE )
        self.assertEqual( city.avaiable_building_modules, 10 )
        self.assertEqual( city.busy_building_modules, 50 )

        res     = city.AddBuildingModulesToBuilding( building_id=complex( 2, 8 ), b_modules=5 )
        self.assertEqual( res, STATUS_CODES.FAILURE )
        self.assertEqual( city.avaiable_building_modules, 10 )
        self.assertEqual( city.busy_building_modules, 50 )

        res     = city.AddBuildingModulesToBuilding( building_id=complex( 2, 3 ), all_modules=True )
        self.assertEqual( res, STATUS_CODES.SUCCESS )
        self.assertEqual( city.avaiable_building_modules, 0 )
        self.assertEqual( city.busy_building_modules, 60 )

        city.ReduceBuildingModulesAtBuilding( building_id=complex( 2, 1 ), b_modules=5 )
        self.assertEqual( city.avaiable_building_modules, 5 )
        self.assertEqual( city.busy_building_modules, 55 )

        city.ReduceBuildingModulesAtBuilding( building_id=complex( 2, 1 ), b_modules=5 )
        self.assertEqual( city.avaiable_building_modules, 5 )
        self.assertEqual( city.busy_building_modules, 55 )

        city.ReduceBuildingModulesAtBuilding( building_id=complex( 2, 1 ), all_modules=True )
        self.assertEqual( city.avaiable_building_modules, 5 )
        self.assertEqual( city.busy_building_modules, 55 )

        city.ReduceBuildingModulesAtBuilding( building_id=complex( 2, 2 ), b_modules=5 )
        self.assertEqual( city.avaiable_building_modules, 10 )
        self.assertEqual( city.busy_building_modules, 50 )

        city.ReduceBuildingModulesAtBuilding( building_id=complex( 2, 3 ), all_modules=True )
        self.assertEqual( city.avaiable_building_modules, 35 )
        self.assertEqual( city.busy_building_modules, 25 )

        city.ReduceBuildingModulesAtBuilding( building_id=complex( 2, 4 ), b_modules=25 )
        self.assertEqual( city.avaiable_building_modules, 55 )
        self.assertEqual( city.busy_building_modules, 5 )

        self.assertEqual( city.AbortConstruction( complex( 2, 2 ) ), BUILDINGS.SOLDIER_SCHOOL.COST )
        self.assertEqual( city.avaiable_building_modules, 60 )
        self.assertEqual( city.busy_building_modules, 0 )

    def test_construct( self ):
        city = ACity( identifier=3 )
        city.StartConstruction( BUILDINGS.SOLDIER_SCHOOL.SHORT_NAME )
        city.StartConstruction( BUILDINGS.SOLDIER_SCHOOL.SHORT_NAME )
        city.StartConstruction( BUILDINGS.MILITARY_UNIVERSITY.SHORT_NAME )
        city.StartConstruction( BUILDINGS.MILITARY_UNIVERSITY.SHORT_NAME )
        city.BuyBuildingModules( 30 )
        city.AddBuildingModulesToBuilding( building_id=complex( 3, 1 ), b_modules=5 )
        city.AddBuildingModulesToBuilding( building_id=complex( 3, 2 ), b_modules=10 )
        city.AddBuildingModulesToBuilding( building_id=complex( 3, 3 ), b_modules=5 )
        city.AddBuildingModulesToBuilding( building_id=complex( 3, 4 ), b_modules=10 )
        self.assertEqual( city.avaiable_building_modules, 0 )
        self.assertEqual( city.busy_building_modules, 30 )

        city.ActivateConstructionYard()

        self.assertEqual( city.number_of_buildings, 1 )
        self.assertEqual( city.AbortConstruction( complex( 3, 3 ) ), BUILDINGS.MILITARY_UNIVERSITY.COST / 2 )
        self.assertEqual( city.AbortConstruction( complex( 3, 6 ) ), 0 )
        self.assertEqual( city.avaiable_building_modules, 15 )
        self.assertEqual( city.busy_building_modules, 15 )

        city.ActivateConstructionYard()
        self.assertEqual( city.number_of_buildings, 2 )
        self.assertEqual( city.avaiable_building_modules, 25 )
        self.assertEqual( city.busy_building_modules, 5 )

        city.ActivateConstructionYard()
        self.assertEqual( city.number_of_buildings, 3 )
        self.assertEqual( city.avaiable_building_modules, 30 )
        self.assertEqual( city.busy_building_modules, 0 )

        city.ActivateConstructionYard()
        self.assertEqual( city.number_of_buildings, 3 )
        self.assertEqual( city.avaiable_building_modules, 30 )
        self.assertEqual( city.busy_building_modules, 0 )

        buildings   = city.buildings
        self.assertTrue( type( buildings[ 0 ] ) == AMilitaryUniversity )
        self.assertTrue( type( buildings[ 1 ] ) == ASoldierSchool )
        self.assertTrue( type( buildings[ 2 ] ) == ASoldierSchool )
        buildings1  = city.buildings
        self.assertFalse( buildings is buildings1 )
