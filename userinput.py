# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:55:39 2020

@author: melis
"""
import numpy as np
from matplotlib import pyplot as plt
import yaml
import calculating_env
# =============================================================================
if __name__ == '__main__':

    file= open('use1.yaml', 'r')
    use_dict = yaml.load(file, Loader=yaml.UnsafeLoader)
    for key, value in use_dict.items():
       print(key + " : " + str(value))

# 
# =============================================================================


#need to make variables
    water= use_dict.get('water',' ')
    water_avg_use=use_dict.get('water_avg_use',' ')
    water_std=use_dict.get('water_std',' ')
    electricity= use_dict.get('electricity',' ')
    elect_avg_use=use_dict.get('elect_avg_use',' ')
    elect_std=use_dict.get('elect_std',' ')
    diesel= use_dict.get('diesel',' ')
    diesel_avg_use=use_dict.get('diesel_avg_use',' ')
    diesel_std=use_dict.get('diesel_std',' ')
    gas=use_dict.get('gas',' ')
    gas_avg_use=use_dict.get('gas_avg_use',' ')
    gas_std=use_dict.get('gas_std',' ')
    al=use_dict.get('al',' ')
    al_avg_use=use_dict.get('al_avg_use',' ')
    al_std=use_dict.get('al_std',' ')
    steel=use_dict.get('steel',' ')
    steel_avg_use=use_dict.get('steel_avg_use',' ')
    steel_std=use_dict.get('steel_std',' ')
    HDPE=use_dict.get('HDPE',' ')
    HDPE_avg_use=use_dict.get('HDPE_avg_use',' ')
    HDPE_std=use_dict.get('HDPE_std',' ')


    avg_env, min_env, max_env = calculating_env.calc_env(use_dict)