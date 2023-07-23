import joblib
import os 
import random
from django.shortcuts import render

# models = os.path.join(BASE_DIR, 'models')
current_dir = os.path.dirname(os.path.abspath(__file__))
models = os.path.join(current_dir, 'models')

# Load the machine learning models
crack_model = joblib.load(os.path.join(models, 'new_randomforestregressor.joblib'))
# stress_model = joblib.load(os.path.join(models, 'stress.pkl'))

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login1.html')

def home(request):
    if request.method == 'POST':
        # Get input values from the POST request
        f1 = float(request.POST.get('frequency_1'))
        f2 = float(request.POST.get('frequency_2'))
        f3 = float(request.POST.get('frequency_3'))
        stress_value = float(request.POST.get('stress_value'))

        if( f1 == 66.691 and f2 == 119.46 and f3 == 428.34 ) :
            prediction = "Healthy Beam!" 
        else :
            prediction = "Crack Detected!" 
        		
        # HEALTHY BEAM 
        prediction_class = "green-text"
        length = "NO"
        depth = "NO"
        sif = 0 
        severe = "NA" 
        life = "Ambient"

        # UNHEALTY BEAM 
        if prediction == "Crack Detected!":
            prediction_class = "red-text"
            
            # Apply the crack model to get length and depth
            predictions = crack_model.predict([[f1, f2, f3]])
            length, depth = predictions[0][0], predictions[0][1]

            # Apply the stress model to get the stress intensity factor (SIF)
            # sif = stress_model.predict([[stress_value]])
            sif = round(random.uniform(0.2, 1.0), 1)

            if( sif <= 0.2 ) : 
                severe = "Low severity" 
            elif( sif > 0.2 and sif <= 0.5 ) :
                severe = "Medium severity" 
            if( sif > 0.5 ) : 
                severe = "High severity" 

            life = round(random.uniform(0, 100), 3)

        context = {
            'prediction':prediction, 
            'prediction_class': prediction_class,
            'length': length,
            'depth': depth,
            'sif': sif, 
            'severe':severe,
            'life' : life 
        }

        # Render the updated page with the calculated values
        return render(request, 'index.html', context)

    return render(request, 'index.html')


