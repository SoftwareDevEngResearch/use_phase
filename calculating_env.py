# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:22:58 2020

@author: melis
"""

import numpy as np
from matplotlib import pyplot as plt

def calc_env(use_dict):
    
    
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

    
    ##calculating things
    water_env= np.random.normal(water_avg_use, water_std, 1000)*water
    electricity_env= np.random.normal(elect_avg_use, elect_std, 1000)*electricity
    diesel_env= np.random.normal(diesel_avg_use, diesel_std, 1000)*diesel
    gas_env= np.random.normal(gas_avg_use, gas_std, 1000)*gas
    al_env= np.random.normal(al_avg_use, al_std, 1000)*al
    steel_env=np.random.normal(steel_avg_use, steel_std, 1000)*steel
    HDPE_env= np.random.normal(HDPE_avg_use, HDPE_std, 1000)*HDPE
    #sum evrythin
    
    total_env=water_env+electricity_env+diesel_env+gas_env+al_env+steel_env+HDPE_env
    avg_env=np.mean(total_env)
    
    print("average: ",avg_env)
    
    min_env=np.min(total_env)
    print("min: ", min_env)
    
    max_env=np.max(total_env)
    print("max: ",max_env)
    
    plt.hist(total_env, 20, density=False, histtype='bar', stacked=True)
    
    return avg_env, min_env, max_env