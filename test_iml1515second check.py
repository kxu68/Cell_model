#!/usr/bin/env python
# coding: utf-8

# In[13]:


import unittest
# import pytest
import cobra
import copy
# generate a sample for loading the models in the origin way for comparison
# model_origin= cobra.io.read_sbml_model('iML1515.xml')
# OV_origin= model_origin.optimize()
# #this is objective value

# model_test = cobra.io.read_sbml_model('IMPROVED_iML1515.xml')
# OV_test= model_test.optimize()
# SM_test= model_test.summary()


class TestIML1515(unittest.TestCase):
# # generate a sample for loading the models in the origin way for comparison
#     model_origin= cobra.io.read_sbml_model('iML1515.xml')
#     OV_origin=model_origin.optimize()
# #this is objective value

#     model_test = cobra.io.read_sbml_model('IMPROVED_iML1515.xml')
#     OV_test= model_test.optimize()
#     SM_test= model_test.summary()    

    def setUp(self):
        print('setup...')
        # generate a sample for loading the models in the origin way for comparison
        model_origin= cobra.io.read_sbml_model('iML1515.xml')
        OV_origin= model_origin.optimize()
        #this is objective value
        model_test = cobra.io.read_sbml_model('IMPROVED_iML1515.xml')
        OV_test = model_test.optimize()
        SM_test = model_test.summary()
#    SETUP is only used for each test therefore the variables can not be passed on to other cases. 
#    NEED to use fixture to pass the variables(OV_test  e.g.) to give other testcases values 
    
#     @pytest.fixture
#     def OV_test():
#         model_test = cobra.io.read_sbml_model('IMPROVED_iML1515.xml')
#         OV_test = model_test.optimize()
        
#     @pytest.fixture
#     def OV_origin():
#         model_origin= cobra.io.read_sbml_model('iML1515.xml')
#         OV_origin= model_origin.optimize()
        
        
    def test_objectivevaluepass(self):
        self.assertTrue(isinstance(OV_test, cobra.core.Solution))
        self.assertTrue(isinstance(OV_origin, cobra.core.Solution))
    
    def test_randomreactiondeletioncheck(self):
        modifymodel= copy.deepcopy(model_origin)
        print('complete model: ', modifymodel.optimize())
        with modifymodel:
#             model_origin.genes.b3940.knock_out()
#             print('metL knocked out: ', model_origin.optimize())
            modifymodel.genes.b4034.knock_out()
            print(' knocked out: ', modifymodel.optimize())
            self.assertNotEqual(modifymodel.optimize().objective_value,0)
      
#     def test_summary_uptake_check(self):
#         modefymodel
            
#     def test_fluxchange(self):
#         self.assert
        
# also need a for checking flux 100%
# and another for checking gene is essential or not(this is using the deletions)
#     def tearDown(self):
#         print('tearDown...')

# this is for test script to be able to run in python as a normal python script
if __name__ == '__main__':
    unittest.main()

# this is for test script to be able to run in ipython shell with notebook
# if __name__ == '__main__':
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[14]:


# # testing the isinstance function
# import unittest
# import pytest
# import cobra
# import copy
# # generate a sample for loading the models in the origin way for comparison
# model_origin= cobra.io.read_sbml_model('iML1515.xml')
# OV_origin= model_origin.optimize()
# #this is objective value

# model_test = cobra.io.read_sbml_model('IMPROVED_iML1515.xml')
# OV_test= model_test.optimize()
# SM_test= model_test.summary()


# isinstance(OV_test, cobra.core.Solution)


# In[ ]:





# In[ ]:




