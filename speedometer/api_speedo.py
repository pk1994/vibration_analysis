

import json
import sys
from flask import Flask, url_for, send_from_directory, request, jsonify,g,send_file
import logging, os
import requests
import wave
import time
import pickle
from scipy.io import wavfile
import numpy as np
from binascii import a2b_base64
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
CORS(app)
## Logs are logged into the server.log file.
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))



@app.route('/testpost', methods = ['POST'])
def test_post():
    print("Inside Post")
    print(request.data)
    url=str(request.data)
    filename = url.split("/")
    print("url",filename[-1])
    
    if filename[-1] == "normal.wav'":
	    
        print("Inside if")
        img1 = "normal.jpg"
        img2 = "normal_1.jpg"
        img3="pitting.jpg"
        img4="pitting_1.jpg"
        AudioName = "normal.wav" # Audio File
        fs, Audiodata = wavfile.read(AudioName)
        list1=[]
        for i in range (0,len(Audiodata),1):
             list1.append(Audiodata[i])
        ans=pd.Series(list1).to_json(orient='values')
		
        resp = {"data1":img1 ,"data2":img2,"data3":img3,"data4":img4,"data8":ans }
 
    if filename[-1] == "pitting.wav'":
        img3="pitting.jpg"
        img4="pitting_1.jpg"
        img1 = "normal.jpg"
        img2 = "normal_1.jpg"
        img5="amppittsub.png"
        img6="specpttsub.png"
        AudioName = "pitting.wav" # Audio File
        fs, Audiodata = wavfile.read(AudioName)
        list1=[]
        for i in range (0,len(Audiodata),1):
            list1.append(Audiodata[i])
        ans=pd.Series(list1).to_json(orient='values')
		
        #print(list1)
        #t = np.arange(len(Audiodata)) / float(fs)
        

        

        resp = {"data1":img1 ,"data2":img2,"data3":img3 ,"data4":img4,"data6":img5,"data7":img6,"data8":ans }
        
 
    if filename[-1] == "tooth_fracture.wav'":
        print("inside if tooth")
        img5="tooth_fracture_spectogram.jpg"
        img6="tooth_fracture_amplitude.jpg"
        img3="pitting.jpg"
        img4="pitting_1.jpg"
        img1 = "amptoothdiff.png"
        img2 = "spectoothdiff.png"
        AudioName = "tooth_fracture.wav" # Audio File
        fs, Audiodata = wavfile.read(AudioName)
        list1=[]
        for i in range (0,len(Audiodata),1):
            list1.append(Audiodata[i])
        ans=pd.Series(list1).to_json(orient='values')
        resp = {"data1":img1 ,"data2":img2,"data3":img3 ,"data4":img4,"data6":img5,"data7":img6,"data8": ans}
 
    if filename[-1] == "wear.wav'":
        print("inside if wear")
        img5="wear_spectogram.jpg"
        img6="wear_amplitude.jpg"
        img3="pitting.jpg"
        img4="pitting_1.jpg"
        img1 = "ampweardiff.png"
        img2 = "specweardiff.png"
        AudioName = "wear.wav" # Audio File
        fs, Audiodata = wavfile.read(AudioName)
        list1=[]
        for i in range (0,len(Audiodata),1):
            list1.append(Audiodata[i])
        ans=pd.Series(list1).to_json(orient='values')
        resp = {"data1":img1 ,"data2":img2,"data3":img3 ,"data4":img4,"data6":img5,"data7":img6,"data8":ans }
		
    if filename[-1] == "combined_changed_final.wav'":
        print("inside if combined")
        
        AudioName = "combined_changed_final.wav" # Audio File
        fs, Audiodata = wavfile.read(AudioName)
        list1=[]
        for i in range (0,len(Audiodata),1):
            list1.append(Audiodata[i])
        ans=pd.Series(list1).to_json(orient='values')
        resp = {"data8":ans }
		
    if filename[-1] == "overlaid_final.wav'":
        print("inside if mix multi")
        
        AudioName = "overlaid_final.wav" # Audio File
        fs, Audiodata = wavfile.read(AudioName)
        list1=[]
        for i in range (0,len(Audiodata),1):
            list1.append(Audiodata[i])
        ans=pd.Series(list1).to_json(orient='values')
        resp = {"data8":ans }
	
    return jsonify(resp)
    
  



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005, debug=False)
