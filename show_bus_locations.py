import json
import sys
import urllib2

if __name__ == '__main__':
    key = sys.argv[1]
    busline = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + busline
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    
    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    number_buses = len(buses)
    print "Bus Line: "+ str(busline)
    print "Number of Active Buses : " + str(number_buses)
    for i in range(number_buses):
        lat =  buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon =  buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print "Bus %s is at latitude %s and longitude %s" %(str(i),str(lat),str(lon))
        
