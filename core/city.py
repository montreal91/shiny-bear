# coding: utf-8

from collections            import OrderedDict

from helpers                import ACounter
from construction_yard      import AConstructionYard
from population             import APopulation

from factory                import AFactory
from military_university    import AMilitaryUniversity
from soldier_school         import ASoldierSchool
from warehouse              import AWarehouse

from game_constants         import BUILDINGS, BUILDING_MODULE_PRICE, STARTING_CITY_POPULATION
from code_constants         import STATUS_CODES

class ACity( object ):
    """docstring for ACity"""
    def __init__( self, identifier=0, title="Rome" ):
        super( ACity, self ).__init__()
        self.__identifier           = identifier
        self.__title                = title
        self.__buildings_counter    = ACounter()
        
        self.__building_modules     = 0
        self.__buildings            = OrderedDict()
        self.__construction_yard    = AConstructionYard()

        self.__population           = APopulation( starting_population=STARTING_CITY_POPULATION )

    @property
    def identifier( self ):
        return self.__identifier

    @property
    def title( self ):
        return self.__title

    @title.setter
    def title(self, new_title):
        if type(new_title) == str:
            self.__title = new_title

    @property
    def avaiable_building_modules( self ):
        return self.__building_modules

    @property
    def busy_building_modules(  self  ):
        return self.__construction_yard.busy_building_modules

    @property
    def buildings( self ):
        copy = self.__buildings.copy()
        return tuple( copy.itervalues() )

    @property
    def number_of_buildings( self ):
        return len( self.__buildings )

    @property 
    def population(self):
        return self.__population.total_population

    def __CreateFactory( self, specialization ):
        return AFactory(
            identifier=complex( self.__identifier, self.__buildings_counter.Next() ),
            cost=BUILDINGS.FACTORY.COST,
            complexity=BUILDINGS.FACTORY.COMPLEXITY,
            specialization=specialization
        )

    def __CreateMilitaryUniversity( self ):
        return AMilitaryUniversity(
            identifier=complex( self.__identifier, self.__buildings_counter.Next() ),
            cost=BUILDINGS.MILITARY_UNIVERSITY.COST,
            complexity=BUILDINGS.MILITARY_UNIVERSITY.COMPLEXITY
        )

    def __CreateSoldierSchool( self ):
        return ASoldierSchool(
            identifier=complex(self.__identifier, self.__buildings_counter.Next() ),
            cost=BUILDINGS.SOLDIER_SCHOOL.COST,
            complexity=BUILDINGS.SOLDIER_SCHOOL.COMPLEXITY
        )

    def __CreateWarehouse( self, specialization ):
        return AWarehouse(
            identifier=complex( self.__identifier, self.__buildings_counter.Next() ),
            cost=BUILDINGS.WAREHOUSE.COST,
            complexity=BUILDINGS.WAREHOUSE.COMPLEXITY,
            specialization=specialization
        )

    def __SetInOperation( self ):
        out                     = self.__construction_yard.PopReadyBuildings()
        self.__building_modules += out.b_modules
        for building in out.buildings:
            self.__buildings[ building.identifier ] = building
    
    def BuyBuildingModules( self, number=0 ):
        number = int( number )
        if number > 0:
            self.__building_modules += number
            return number * BUILDING_MODULE_PRICE
        else:
            return 0

    def SellBuildingModules( self, number=0, all_modules=False ):
        number = int( number )
        if number > self.__building_modules or all_modules:
            bm = self.__building_modules
            self.__building_modules = 0
            return bm * BUILDING_MODULE_PRICE / 2
        elif number < 0:
            return 0
        else:
            self.__building_modules -= number
            return number * BUILDING_MODULE_PRICE / 2

    # It's hardcoded but at least it works.
    def StartConstruction( self, building_type, specialization=None ): 
        if building_type == BUILDINGS.MILITARY_UNIVERSITY.SHORT_NAME:
            building = self.__CreateMilitaryUniversity()
        elif building_type == BUILDINGS.SOLDIER_SCHOOL.SHORT_NAME:
            building = self.__CreateSoldierSchool()
        elif specialization is None:
            return STATUS_CODES.FAILURE
        elif building_type == BUILDINGS.FACTORY.SHORT_NAME:
            building = self.__CreateFactory( specialization )
        elif building_type == BUILDINGS.WAREHOUSE.SHORT_NAME:
            building = self.__CreateWarehouse( specialization )
        else:
            return STATUS_CODES.FAILURE
        self.__construction_yard.AddBuilding( building )
        return building.cost

    def AbortConstruction( self, building_id ):
        res = self.__construction_yard.RemoveBuilding( building_id )
        self.__building_modules += res.b_modules
        return res.remainder

    def AddBuildingModulesToBuilding( self, building_id=0, b_modules=0, all_modules=False ):
        b_modules = int( b_modules )
        if all_modules or b_modules > self.__building_modules:
            result = self.__construction_yard.AddBuildingModulesToBuilding( building_id, self.__building_modules )
            if result == STATUS_CODES.SUCCESS:
                self.__building_modules = 0
                return STATUS_CODES.SUCCESS
            else:
                return STATUS_CODES.FAILURE
        else:
            result = self.__construction_yard.AddBuildingModulesToBuilding( building_id, b_modules )
            if result == STATUS_CODES.SUCCESS:
                self.__building_modules -= b_modules
                return STATUS_CODES.SUCCESS
            else:
                return STATUS_CODES.FAILURE

    def ReduceBuildingModulesAtBuilding( self, building_id=0, b_modules=0, all_modules=False ):
        b_modules   = int( b_modules )
        modules     = self.__construction_yard.TakeBuildingModulesFromBuilding( building_id=building_id, b_modules=b_modules, all_modules=all_modules )
        self.__building_modules += modules

    def ActivateConstructionYard( self ):
        self.__construction_yard.Construct()
        self.__SetInOperation()
