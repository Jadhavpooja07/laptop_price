from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import LaptopPrice
import config
import traceback
app = Flask(__name__)

@app.route('/laptop_price')
def home1():
    
    return render_template('laptop_price.html')

@app.route('/predict_price', methods = ['GET', 'POST'])
def predict_price():
    try:
        if request.method == 'GET':
            print("+"*50)
            data = request.args.get
            print("Data :",data)
            processor_brand = data('processor_brand')
            ram_gb = data('ram_gb')
            ssd = data('ssd')
            hdd = data('hdd')
            os_bit = data('os_bit')
            Touchscreen = data('Touchscreen')
            brand = data('brand')

            Obj = LaptopPrice(processor_brand,ram_gb,ssd,hdd,os_bit,Touchscreen,brand)
            pred_price = Obj.get_predicted_price()
            
            return render_template('laptop_price.html', prediction = pred_price)

        elif request.method == 'POST':
            print("*"*40)
            data = request.form.get
            print("Data :",data)
            processor_brand = data('processor_brand')
            ram_gb = data('ram_gb')
            ssd = data('ssd')
            hdd = data('hdd')
            os_bit = data('os_bit')
            Touchscreen = data('Touchscreen')
            brand = data('brand')

            Obj = LaptopPrice(processor_brand,ram_gb,ssd,hdd,os_bit,Touchscreen,brand)
            pred_price = Obj.get_predicted_price()
            
            
            return render_template('laptop_price.html', prediction = pred_price)

    except:
        print(traceback.print_exc())
        return redirect(url_for('laptop_price'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)