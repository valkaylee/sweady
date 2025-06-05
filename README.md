# SWEADY - Non-Invasive Glucose Monitoring

## Motivation
Many individuals with diabetes or high blood sugar must prick their fingertips multiple times a day to monitor their glucose levels. This process is not only painful and inconvenient, but can also lead to long-term issues such as callous formation, scarring, or loss of fingertip sensitivity.

We were inspired to create a non-invasive, painless alternative for monitoring. Emerging research suggests that glucose levels in sweat can reflect blood glucose. To explore this idea, we are using a GSR (Galvanic Skin Response) sensor, which measures the skin's electrical conductance.

## Project Description & Functionality
Our project is a non-invasive glucose monitoring prototype that uses GSR (Galvanic Skin Response) data from sweat and a Decision Tree Classifier (supervised learning ML algorithm) to classify whether a person is in a resting state, experiencing a glucose spike, or sweating due to non-glucose-related physical activity. 

![image](https://github.com/user-attachments/assets/f104be34-35f8-4540-ac61-859a240da887)

## Hardware Components: 
- Grove GSR Sensor- Measures skin conductance and outputs analog signals reflecting moisture levels
- GrovePi+ board- analog-to-digital interface, converts the GSR sensor’s analog data into digital values over the I2C protocol.
- Raspberry Pi 4B- collects data via I2C, runs the machine learning classifier, and hosts Flask-based HTTP server.
- Laptop (client)- Connects via HTTP over Wi-Fi to the Flask server and initiates classification requests through a simple web interface.

## Software Components:
- measure.py: GSR data collection from GrovePi, saves 100 data points to .csv
- classifier.py: trains Decision Tree Classifier (supervised learning ML algorithm) using scikit-learn
- main.py: performs prediction on new GSR data, prints most common predicted state 
- app.py: Flask server, provides REST API for client to start GSR measurement (POST) and check classification result (GET)

## Data Results:
Label	       Kaylee Range	Jason Range
Resting	 	    365–387	   222–270
Sweat	         265–314	  99–127
After Sugar	   450–475	  311–343

Outliers were removed for accurate/consistent data. 

## Implementation:
We collected around 300 data points total, with 100 samples per category (resting, sweating, after sugar intake) across two different types of users: Kaylee (higher resting GSR) and Jason (lower resting GSR). To induce sweating, we performed physical activities like running up and down the stairs, jumping jacks, pushups, and warming our hands. For glucose-based measurements, we each consumed about 30 grams of sugar, about a day’s worth of sugar, and waited 1 to 2 hours to allow the glucose to enter our bloodstream. 

Based on our data, our working hypothesis is that exercise-induced sweat results in overly moist skin, which can reduce surface conductivity, causing a lower GSR value. Conversely, glucose-rich sweat contains more dissolved ions, enhancing electrical conductivity and leading to a higher GSR reading.

## Reflection
Limitations/Lessons Learned: 
Small dataset- collected over only three days from just two users → our classifier is not generalizable and would require significantly more data to be reliable across different individuals. 
Inaccurate data- GSR is also affected by non-glucose factors like stress, which we didn’t account for, making it difficult to isolate signals. 
Need for better sensors- Grove GSR sensor is not designed to detect glucose specifically, and clinical accuracy would likely require more advanced, biochemically tuned sensors.

This project show the potential for non-invasive, low-cost health monitoring using sweat-based biosignals and machine learning, and with more time/research we could potentially accurately predict glucose spikes for diabetes and high glucose level patients—allowing them to take proactive measures like exercising, to bring down their levels before those spikes happen, which we believe can help a lot of people.


## Libraries: 
- `pandas` (for data loading and CSV handling)
- `scikit-learn` (for training and using the decision tree classifier)
- `flask` (to build the web server)
- `grovepi` (to interface with the Grove GSR sensor hardware)

## How to run: run with python3 name_of_file.py
- main.py - take GSR reading and classify result 
- app.py - to launch web interface (flask server)
- measure.py - collects GSR value and stores in .csv 
- classifier.py - train classifier 

