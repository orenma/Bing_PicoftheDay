# Bing_Wallpaper
Download Bing picture of the day


#### FOR OSX users:

In order for crontab to run a python script under OSX envirement you will have to grant cron access to disk operation, or cron will fail with permission not permitted.

https://blog.bejarano.io/fixing-cron-jobs-in-mojave/


(source: https://stackoverflow.com/questions/58593877/crontab-cant-execute-python-script-with-error-errno-1-operation-not-permitt)

&nbsp;  
&nbsp;


For easy implemting, you can point it to run the bash script (osx_bing_cron.sh)


cron schedule example:

`
1 1 * * * /Users/USER-CHANGE_ME/Bing_Wallpaper/osx_bing_cron.sh
`

&nbsp;  
&nbsp;
  
Images will be saved under your home directory/Pictures/bing-wallpapers
`
~/Pictures/bing-wallpapers
`
