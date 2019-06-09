# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:44:42 2019

@author: R.ManchenahalliRajg2
"""

#generate  UUID
import uuid

def generate_uuid(user = "R@mya!", unit = "U10600", equip = "V10615", model = 1):
    value = str(user)+"_"+unit+"_"+equip+"_"+str(model)
#    str(uuid.uuid3(uuid.NAMESPACE_DNS,'U10610_Eq1_M1'))
    str(uuid.uuid3(uuid.NAMESPACE_DNS,value))


