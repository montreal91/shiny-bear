# coding: utf-8

from unittest               import TestCase

from core.warehouse         import AWarehouse
from core.game_constants    import WAREHOUSE, SPECIALIZATIONS

class AWarehouseTestCase( TestCase ):
    def setUp( self ):
        self.weapons                = SPECIALIZATIONS[ "WEAPONS" ]
        self.armours                = SPECIALIZATIONS[ "ARMOURS" ]

        self.capacity_factor        = WAREHOUSE[ "CAPACITY_FACTOR" ]
        self.increase_capacity_cost = WAREHOUSE[ "INCREASE_CAPACITY_COST" ]
        self.decrease_capacity_cost = WAREHOUSE[ "DECREASE_CAPACITY_COST" ]

    def test_constuctor( self ):
        w_house = AWarehouse()
        self.assertEqual( w_house.capacity, 100 )
        self.assertEqual( w_house.specialization, self.weapons )
        self.assertEqual( w_house.amount, 0 )

        w_house = AWarehouse( specialization=self.armours, capacity=200 )
        self.assertEqual( w_house.capacity, 200 )
        self.assertEqual( w_house.specialization, self.armours )
        self.assertEqual( w_house.amount, 0 )

        with self.assertRaises( AssertionError ):
            w_house = AWarehouse( specialization="fart" )

    def test_increase_decrease_capacity( self ):
        w_house = AWarehouse()
        self.assertEqual( w_house.capacity, 100 )
        self.assertEqual( w_house.specialization, self.weapons )
        self.assertEqual( w_house.amount, 0 )

        self.assertEqual( w_house.IncreaseCapacity(), self.increase_capacity_cost )
        self.assertEqual( w_house.capacity, self.capacity_factor + 100 )

        self.assertEqual( w_house.DecreaseCapacity(), self.decrease_capacity_cost )
        self.assertEqual( w_house.capacity, 100 )

        w_house.DecreaseCapacity()
        w_house.DecreaseCapacity()
        self.assertEqual( w_house.capacity, 0 )

        w_house.IncreaseCapacity()
        self.assertEqual( w_house.capacity, self.capacity_factor )

    def test_take_put_items( self ):
        w_house = AWarehouse()
        w_house.PutItems( items_level=1, number_of_items=10 )
        self.assertEqual( w_house.amount, 10 )

        w_house.PutItems( items_level=1, number_of_items=10 )
        self.assertEqual( w_house.amount, 20)
        self.assertEqual( w_house.TakeSomeItems( items_level=1, number_of_items=15 ), 15 )

        w_house.PutItems( items_level=2, number_of_items=200 )
        self.assertEqual( w_house.amount, 100 )
        self.assertEqual( w_house.TakeSomeItems( items_level=1, number_of_items=10 ), 5 )
        self.assertEqual( w_house.amount, 95 )
        self.assertEqual( w_house.TakeSomeItems( items_level=1, number_of_items=10 ), 0 )
        self.assertEqual( w_house.amount, 95 )
        self.assertEqual( w_house.TakeSomeItems( items_level=-1, number_of_items=10 ), 0 )
        self.assertEqual( w_house.amount, 95 )
        self.assertEqual( w_house.TakeSomeItems( items_level=10, number_of_items=10 ), 0 )
        self.assertEqual( w_house.amount, 95 )
        self.assertEqual( w_house.TakeAllItems( items_level=2 ), 95 )
        self.assertEqual( w_house.amount, 0 )
        