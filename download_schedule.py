import urllib.request
import os
import schedule
import time
from datetime import datetime
from datetime import timedelta
import sys

def jobTo():

	err=0
	#error handling:
	def job():

		dateTime= datetime.now()
		schTime= dateTime.strftime('%H:%M')

		formatDtime= dateTime.strftime('%d_%m_%Y_%H_%M')
		print('Download attempt starting')

		#urllib.request.urlretrieve('http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv.zip', 'sample_csv_' +formatDtime+'.zip')
		urllib.request.urlretrieve('http://s3.kiva.org/snapshots/kiva_ds_csv1.zip', 'kiva_ds_csv_' +formatDtime+'.zip')
		
	try:
		job()
		print('Requested file has finished downloading')
	#except urllib.error.HTTPError:
	except:
		print('The file is not available for downloading, will try again in 10 seconds')
		print(err)
		while err < 3:	
			time.sleep(10)
			try :
				job()
			except:
				print('The file is not available for downloading , will try again for ' + str(2- err) + ' more times')
				err += 1

dateTime= datetime.now()+ timedelta(seconds=60)
schTime= dateTime.strftime('%H:%M')
print('Scheduled time to run the job is: ' + str(schTime))
schedule.every().tuesday.at(schTime).do(jobTo)
#schedule.every(20).seconds.do(jobTo)
#schedule.clear()

while True:
    schedule.run_pending()
    time.sleep(50)
    print('The scheduler is active and set to run at the specified time')
	        