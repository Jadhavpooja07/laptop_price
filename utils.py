import pickle
import json
import numpy as np
import config


class LaptopPrice():
    def __init__(self,processor_brand,ram_gb,ssd,hdd,os_bit,Touchscreen,brand):
        print("****** INIT Function *********")
        self.processor_brand = processor_brand
        print(self.processor_brand)
        self.ram_gb = ram_gb
        self.ssd = ssd
        self.hdd = hdd
        self.os_bit = os_bit
        self.Touchscreen = Touchscreen
        self.brand = brand

       
    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):
        self.__load_saved_data()

        processor_brand = self.json_data["Processor_brand"][self.processor_brand]
        ram_gb = self.json_data['Ram_gb'][self.ram_gb]
        ssd = self.json_data['Ssd'][self.ssd]
        hdd = self.json_data['Hdd'][self.hdd]
        os_bit = self.json_data['Os_bit'][self.os_bit]
        Touchscreen = self.json_data['TOUCHSCREEN'][self.Touchscreen]
        brand = 'brand_'+ self.brand

        brand_index = self.json_data["Column Names"].index(brand)

        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = processor_brand
        test_array[0,1] = ram_gb
        test_array[0,2] = ssd
        test_array[0,3] = hdd
        test_array[0,4] = os_bit
        test_array[0,5] = Touchscreen
        test_array[0,brand_index] = 1

        predicted_price = np.around(self.model.predict(test_array)[0],3)
        return predicted_price
    