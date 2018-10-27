from getAPIKeyPackage.getAPIKeys import getAPIKey

print ("------Test getAPIKeys Function------")
print
google_api_key = getAPIKey("Google", "GeocodeLocation", "google_api_key")
print ("google_api_key=%s" % (google_api_key))
print
foursquare_client_id = getAPIKey("Foursquare", "Foursquare", "client_id")
print ("foursquare_client_id=%s" % (foursquare_client_id))
print
foursquare_client_secret = getAPIKey("Foursquare", "Foursquare", "client_secret")
print ("foursquare_client_secret=%s" % (foursquare_client_secret))
print
