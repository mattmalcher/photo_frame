# photo_frame
A go at making a photo frame site that can be locally hosted on a pi &amp; serve up a slideshow of images from a network drive


# How?

I'm thinking a flask app in a container, with a volume containing photos passed in.


# Rough Plan


## MVP
* cycle through a single directory of images



## Version 2
* I want it to be easy to update the photos, so ideally it would periodically re-scan the drive/folder for pictures - maybe build a metadata db, and then pick from this randomly.
  

## Bonuses
* Image Upload
* Metadata Display Toggle
* 


# Questions

## How do I get flask to serve up images from arbirary locations

## How do I get the page to refresh on an interval?

* Use AJAX / JS to reload the page? https://stackoverflow.com/questions/8470431/what-is-the-best-way-to-implement-a-forced-page-refresh-using-flask 



# Research

https://github.com/Digital-Signage-Slideshow/DS_Slideshow

https://runnable.com/docker/python/dockerize-your-flask-application

https://medium.com/swlh/flask-docker-the-basics-66a699aa1e7d