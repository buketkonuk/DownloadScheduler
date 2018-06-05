# DownloadScheduler
Python script to schedule downloading a file from a url

The objective is to be able to schedule the download of a file froma website if it's updated regularly.
In case the download fails, the script tries 3 more times before stopping and waits for the next schedule time.

Currently the schedule time is set to start 1 minute after the current time.

If the download is successful, the file name is appended with current datetime. 
