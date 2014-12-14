import pandas
from geopy.geocoders import Nominatim

#reading two csv files and converting them to pandas dataframes
awards = pandas.read_csv('awards.csv')
contracts = pandas.read_csv('contracts.csv')

#merging two csv with common column 'contracts'
final_output = pandas.merge(contracts, awards, on='contractname' , how = 'outer')
#invoking Nomiatim function from geopy
geolocator = Nominatim()

#calculating the row length of dataframes 

row_len = len(final_output['status'])

#the Total sum of the awards
Total_sum = 0.0
#list for storing the latitude and longitude of the awardee locations
lati = []

#eliminating the amount having null value with 0
final_output['Amount'].fillna(0, inplace=True)

#calculating the latitude and longitude also checking the status of contract to calulate the total sum
for i in range(0,row_len):
	#adding Nepal to the location 
	item = str(final_output['awardeeLocation'][i]) + " Nepal"
	location = geolocator.geocode(item)
	latilon=str(location.latitude) + ' , ' + str(location.longitude)
	lati.append(latilon)

	if (final_output['status'][i] == 'Closed'):
		Total_sum += final_output['Amount'][i]

final_output['latilon'] = lati

final_output.to_csv(str('final_output.csv'),header = True, index = False,na_rep = "0" ,engine = 'python')

print "The Total Amount  of closed  contract is " ,Total_sum
