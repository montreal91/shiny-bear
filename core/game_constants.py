# coding: utf-8

from helpers import AStruct

SPECIALIZATIONS = {
    "WEAPONS": "weapons",
    "ARMOURS": "armours"
}

GENDERS         = {
    "MALE"  : "m",
    "FEMALE": "f",
}

FACTORY         = {
    "PRODUCT_PRICE"             : 100,
    "DEFAULT_TECH_LEVEL"        : 1,
    "DEFAULT_PROD_LEVEL"        : 1,
    "DEFAULT_PRODUCTIVITY"      : 1.0,
    "DEFAULT_EFFICIENCY"        : 1,
    "DEFAULT_STORAGE_CAPACITY"  : 1000,

    "EXPONENT"                  : 2,
    "PRICE_FACTOR"              : 100,

    "PRODUCTIVITY_GROWTH_FACTOR": 0.1,
    "EFFICIENCY_GROWTH_FACTOR"  : 1,
    "TECH_LEVEL_GROWTH_FACTOR"  : 1,

    "PRODUCTIVITY_FACTOR"       : 100,
}

DIVISION        = {
    "COMMANDER_LEADERSHIP_FACTOR": 5
}

HUMAN           = {
    "GAUSS_MU"          : 65,
    "GAUSS_SIGMA"       : 5,

    "MAX_HEALTH"        : 100,
    "VALIDITY_FACTOR"   : 50,
}

SKILL           = {
    "TALENT_MU"     : 2,
    "TALENT_SIGMA"  : 1,

    "MAXIMUM_MU"    : 15,
    "MAXIMUM_SIGMA" : 5,
}

WAREHOUSE       = {
    "CAPACITY_FACTOR"       : 100,
    "INCREASE_CAPACITY_COST": 1000,
    "DECREASE_CAPACITY_COST": 500,
}

BUILDINGS                                   = AStruct()

BUILDINGS.FACTORY                           = AStruct()
BUILDINGS.FACTORY.COST                      = 100000
BUILDINGS.FACTORY.COMPLEXITY                = 50
BUILDINGS.FACTORY.VERBOSE_NAME              = "factory"
BUILDINGS.FACTORY.SHORT_NAME                = "fc"

BUILDINGS.MILITARY_UNIVERSITY               = AStruct()
BUILDINGS.MILITARY_UNIVERSITY.COST          = 10000
BUILDINGS.MILITARY_UNIVERSITY.COMPLEXITY    = 10
BUILDINGS.MILITARY_UNIVERSITY.VERBOSE_NAME  = "military university"
BUILDINGS.MILITARY_UNIVERSITY.SHORT_NAME    = "mu"

BUILDINGS.SOLDIER_SCHOOL                    = AStruct()
BUILDINGS.SOLDIER_SCHOOL.COST               = 5000
BUILDINGS.SOLDIER_SCHOOL.COMPLEXITY         = 15
BUILDINGS.SOLDIER_SCHOOL.VERBOSE_NAME       = "soldier school"
BUILDINGS.SOLDIER_SCHOOL.SHORT_NAME         = "ss"

BUILDINGS.WAREHOUSE                         = AStruct()
BUILDINGS.WAREHOUSE.COST                    = 1000
BUILDINGS.WAREHOUSE.COMPLEXITY              = 5
BUILDINGS.WAREHOUSE.VERBOSE_NAME            = "warehouse"
BUILDINGS.WAREHOUSE.SHORT_NAME              = "wh"

BUILDING_MODULE_PRICE                       = 500