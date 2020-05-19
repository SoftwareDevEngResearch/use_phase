# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:55:39 2020

@author: melis
"""
#doing yaml stuff
import yaml
with open (r ')
    use_case= yaml.load(file, loader-yaml.FullLoader)
    print(use_case)

#need calculations done to get total values
min_use_1=min_time_per_use*min_use_per_month*12
max_use_1=max_time_per_use*max_use_per_month*12
average_use_1=(min_use_1+max_use_1)/2*env_impact
stdev_1=(min_use_1+max_use_1)/6*env_impact

#need mu and sigma foro everything
use_1= np.random.normal(average_use_1, stdev_1, 1000)
    
#sum evrythin
total_use=use_1