# Beam Health

## Preview 
https://github.com/Ram-lankada/beam_health/assets/91232198/b7d3e843-0bb2-4eaf-a7e9-410ac7752f11

## Beam health architecture 
![Web_application_architecture](https://github.com/Ram-lankada/beam_health/assets/91232198/c51413f2-ff19-445e-aab7-7594bff04c59)

All the three models used are Machine learning models implementing Random Forest regression. 

### Crack Localization Model 
These models takes in 3 Frequencies as input and outputs the length & the depth of Crack if detected. 
If the sensed frequencies are of ideal frequencies then it is predicted to ba a Healthy Beam & no prediction of length & depth of the crack will be done.

### Stress Intensity Factor Prediction

This model takes in the Stress value sensed by the Strain Guage which is attached to the beam while applying the load. And predicts the Stress intensity factor on a scale from 0.0 to 1.0. 
And based on the, Stress intensity factor the Severity of the damage will be calculated and will be categorized into : 
- Low Severity
- Medium Severity
- High Severity

### Residual life Estimation

This model takes in the Stress value sensed by the Strain Guage which is attached to the beam while applying the load and predicts the maxium possible time till which the beam can be used, which can be termd as Residual life. After which the composite beam has to be discarded to prevent unexpected accidents / mishaps. 

## Project Architecture 
![random_forest_architecture](https://github.com/Ram-lankada/beam_health/assets/91232198/b900dd84-3142-4caa-84c6-2e95cc4ba02d)



