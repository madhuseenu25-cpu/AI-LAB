# AI-Based Traffic Density Prediction
 
print("TRAFFIC DENSITY PREDICTION SYSTEM")
 
vehicles = int(input("Enter number of vehicles: "))
 
if vehicles < 20: 
     print("Traffic Density: LOW") 
     print("Prediction: Traffic is clear.")
 
elif vehicles < 50: 
     print("Traffic Density: MEDIUM") 
     print("Prediction: Moderate traffic expected.")
 
else: 
     print("Traffic Density: HIGH") 
     print("Prediction: Heavy traffic expected.") 

print("Traffic prediction completed!")