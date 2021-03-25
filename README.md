# Bing_Wallpaper
Download Bing picture of the day


#### FOR OSX users:

In order for crontab to run a python script under OSX envirement , you will need to point it to run the bash script (osx_bing_cron.sh)


cron schedule example:

`
1 1 * * * /Users/USER-CHANGE_ME/Bing_Wallpaper/osx_bing_cron.sh
`

&nbsp;  
&nbsp;
  
Other option will be to grant cron access to disk operation

https://blog.bejarano.io/fixing-cron-jobs-in-mojave/


(source: https://stackoverflow.com/questions/58593877/crontab-cant-execute-python-script-with-error-errno-1-operation-not-permitt)
