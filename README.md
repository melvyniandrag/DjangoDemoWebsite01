# Django Demo Website 01

This is the first of a series of websites you can easily deploy on digital ocean to learn about deploying websites on Linux servers.

This repo is associated with The Linux Workbook, a class on Udemy.

## Instructions

### Check if webserver is running #1
Type the ip address of your droplet into your browser. You should get an error.

### Install with apt
```
$ sudo apt update
$ sudo apt install apache2 libapache2-mod-wsgi-py3
$ sudo apt install python3-dev
$ sudo apt install python3-pip python3.11-venv
$ sudo apt install wget unzip
```

### Check if webserver is running #2
Type the ip address of your droplet into your browser. You should see the default apache webserver page!
Try typing it into your cellphone now too - you'll see the same thing there!


### Copy the website code to your computer
```
$ wget https://github.com/melvyniandrag/DjangoDemoWebsite01/archive/refs/heads/master.zip
$ unzip master.zip
$ cd DjangoDemoWebsite01
$ mv demowebsite /var/www
```
Then add your IP Address to the allowed hosts in your `/var/www/demowebsite/demowebsite/settings.py` file.

The ALLOWED_HOSTS should now look like this:

```
ALLOWED_HOSTS = [
    'your.ip.address.here',
    'localhost'
]
```

BE CAREFUL with the above thing! Make sure there are 4 spaces before the ip address and 4 spaces before localhost.
Make sure to put a comma as shown above. Do not make any other changes to the file!!


### Create a virtual env and install with pip3
```
$ cd /var/www/demowebsite
$ python3 -m venv djangoEnv
$ source djangoEnv/bin/activate
$ pip3 install django
```

### Put the website config file in the proper location
```
$ cd Apache2ConfFiles
$ mv demowebsite.conf /etc/apache2/sites-available/
```

### Disable the default site, enable your site.
```
$ a2dissite 000-default.conf
$ a2ensite demowebsite.conf
```

### Check if webserver is running #3
Type the ip address of your droplet into your browser. You should see your about nj website. Feel free to go modify the HTML now in `/var/www/demowebsite/myapp/templates/myapp/about_nj.html`, then reload your server with `systemctl reload apache2` and you'll see your own website! 

## Conclusion
And now we should have everything we need! Now follow along with the video as we put everything in the proper locations and turn on our website. We'll discuss the config files. They are super simplified to have the bare minimum necessary to run, but you'll want to know more so you can ace your job interviews.

## References
* https://django-project-skeleton.readthedocs.io/en/latest/apache2_vhost.html
* https://modwsgi.readthedocs.io/en/develop/configuration-directives/WSGIDaemonProcess.html
* https://stackoverflow.com/questions/76454056/mod-wsgi-concise-comparison-of-application-groups-process-groups-processes
* https://stackoverflow.com/questions/29881400/which-value-for-wsgiapplicationgroup-when-running-multiple-django-virtual-hosts/29883760#29883760
