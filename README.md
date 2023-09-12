# Django Demo Website 01

This is the first of a series of websites you can easily deploy on digital ocean to learn about deploying websites on Linux servers.

This repo is associated with The Linux Workbook, a class on Udemy.

## Dependencies

### Install with apt
```
$ sudo apt install apache2 libapache2-mod-wsgi-py3
$ sudo apt install python3-dev
$ sudo apt install python3-pip python3.11-venv
$ sudo apt install wget unzip
```
### Create a virtual env and install with pip3
```
$ cd /var/www/demowebsite
$ python3 -m venv djangoEnv
$ source djangoEnv/bin/activate
$ pip3 install django
```
### Copy the website to your computer
```
$ wget https://github.com/melvyniandrag/DjangoDemoWebsite01/archive/refs/heads/master.zip
$ unzip master.zip
```

And now we should have everything we need! Now follow along with the video as we put everything in the proper locations and turn on our website. We'll discuss the config files. They are super simplified to have the bare minimum necessary to run, but you'll want to know more so you can ace your job interviews.

## References
* https://django-project-skeleton.readthedocs.io/en/latest/apache2_vhost.html
* https://modwsgi.readthedocs.io/en/develop/configuration-directives/WSGIDaemonProcess.html
* https://stackoverflow.com/questions/76454056/mod-wsgi-concise-comparison-of-application-groups-process-groups-processes
* https://stackoverflow.com/questions/29881400/which-value-for-wsgiapplicationgroup-when-running-multiple-django-virtual-hosts/29883760#29883760
