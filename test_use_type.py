# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:44:03 2020

@author: melis
"""

""" The following script is used to test the yaml checking module in the 
use. """

import yaml
import pytest
import calculating

##reading in the yaml
file= open('use1.yaml', 'r')
use_dict = yaml.load(file, Loader=yaml.UnsafeLoader)
for key, value in use.items():
    print(key + " : " + str(value))

#checking the formatting
def check_water_format(use_dict):
    water = use_dict.get('water')
    assert type(water) == float or int, 'Input requires interger or float input'

    water_avg_use = use_dict.get('water_avg_use')
    assert type(water_avg_use) == float or int, 'Input requires interger or float input'

    water_std = use_dict.get('water_std')
    assert type(water_std) == float or int, 'Input requires interger or float input'

def check_elect_format(use_dict):
    elect = use_dict.get('electricity')
    assert type(elect) == float or int, 'Input requires interger or float input'

    elect_avg_use = use_dict.get('elect_avg_use')
    assert type(elect_avg_use) == float or int, 'Input requires interger or float input'

    elect_std = use_dict.get('elect_std')
    assert type(elect_std) == float or int, 'Input requires interger or float input'

def check_diesel_format(use_dict):
    diesel = use_dict.get('diesel')
    assert type(diesel) == float or int, 'Input requires interger or float input'

    diesel_avg_use = use_dict.get('diesel_avg_use')
    assert type(diesel_avg_use) == float or int, 'Input requires interger or float input'

    diesel_std = use_dict.get('diesel_std')
    assert type(diesel_std) == float or int, 'Input requires interger or float input'
    
def check_gas_format(use_dict):
    gas = use_dict.get('gas')
    assert type(gas) == float or int, 'Input requires interger or float input'

    gas_avg_use = use_dict.get('gas_avg_use')
    assert type(gas_avg_use) == float or int, 'Input requires interger or float input'

    gas_std = use_dict.get('gas_std')
    assert type(gas_std) == float or int, 'Input requires interger or float input'
    
def check_al_format(use_dict):
    al = use_dict.get('al')
    assert type(al) == float or int, 'Input requires interger or float input'

    al_avg_use = use_dict.get('al_avg_use')
    assert type(al_avg_use) == float or int, 'Input requires interger or float input'

    al_std = use_dict.get('al_std')
    assert type(al_std) == float or int, 'Input requires interger or float input'
    
def check_steel_format(use_dict):
    steel = use_dict.get('steel')
    assert type(steel) == float or int, 'Input requires interger or float input'

    steel_avg_use = use_dict.get('steel_avg_use')
    assert type(steel_avg_use) == float or int, 'Input requires interger or float input'

    steel_std = use_dict.get('steel_std')
    assert type(steel_std) == float or int, 'Input requires interger or float input'
    
def check_HDPE_format(use_dict):
    HDPE = use_dict.get('HDPE')
    assert type(HDPE) == float or int, 'Input requires interger or float input'

    HDPE_avg_use = use_dict.get('HDPE_avg_use')
    assert type(HDPE_avg_use) == float or int, 'Input requires interger or float input'

    HDPE_std = use_dict.get('HDPE_std')
    assert type(HDPE_std) == float or int, 'Input requires interger or float input'