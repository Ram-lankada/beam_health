import joblib
from django.shortcuts import render

# Load the machine learning models
crack_model = joblib.load('crack.pkl')
stress_model = joblib.load('stress.pkl')
life_model = joblib.load('life.pkl')

def home(request):
    if request.method == 'POST':
        # Get input values from the POST request
        frequency_1 = float(request.POST.get('frequency_1'))
        frequency_2 = float(request.POST.get('frequency_2'))
        frequency_3 = float(request.POST.get('frequency_3'))
        stress_value = float(request.POST.get('stress_value'))

        # Apply the crack model to get length and depth
        length, depth = crack_model.predict([[frequency_1, frequency_2, frequency_3]])

        # Apply the stress model to get the stress intensity factor (SIF)
        sif = stress_model.predict([[stress_value]])

        # finding life 
        life = life_model.predict([[stress_value]])


        if( sif <= 0.2 ) :
            severe = "Low severity" 
        elif( sif > 0.2 and sif <= 0.5 ) : 
            severe = "Medium severity"
        if( sif > 0.5 ) :
            severe = "High severity" 


        context = {
            'length': length, 
            'depth': depth, 
            'sif': sif, 
            'severe':severe, 
            'life' : life 
        }
        # Render the updated page with the calculated values
        return render(request, 'result.html', context )

    return render(request, 'input_form.html')
