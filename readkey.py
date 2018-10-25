from getAPIKeys import getAPIKey

apptab = getAPIKey("Google", "GeocodeLocation")
print (apptab.key1)
print (apptab.value1)
print (apptab.key2)
print (apptab.value2)
apptab = getAPIKey("Foursquare", "Foursquare")
print (apptab.key1)
print (apptab.value1)
print (apptab.key2)
print (apptab.value2)
