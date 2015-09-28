import json
import sys
import urllib2
import csv

if __name__ == '__main__':
    key = sys.argv[1]
    busline = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=' + key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + busline
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    
    output = open(sys.argv[3],'w')
    writer = csv.writer(output)
    headers = ['Latitude','Longitude','Stop Name','Stop Status']
    writer.writerow(headers)

    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    number_buses = len(buses)

    for i in range(number_buses):
        lat =  buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon =  buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        try:
            StopName = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        except KeyError:
            StopName = "N/A"
        try:
            StopStatus = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        except KeyError:
            StopStatus = "N/A"
        writer.writerow([lat,lon,StopName,StopStatus])
    
