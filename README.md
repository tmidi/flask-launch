# flask-launch

## Build Status:
[![Build Status](https://travis-ci.org/tmidi/flask-isitpublic.svg?branch=master)](https://travis-ci.org/tmidi/flask-isitpublic)

## Description:
Launch is simple Flask project to track upcoming space launches and display information about the mission, rocket and agency.
This project is using [Launch Library](http://launchlibrary.net/docs/1.4/api.html) a publicly available API.

## Install:
### Build:
You can clone this repository to manually build the container image:

```bash
# Clone Repo:
git clone git@github.com:tmidi/flask-launch.git

# Build Docker image:
docker build -t flask-launch --file Dockerfile

# Run image:
docker run -p 5000:5000 flask-launch

```
### Use public image:
```bash
# Pull image:
docker pull taleeb/launch

# Run container
docker run -p 5000:5000 taleeb/launch
```

## License

This repo is available under [GNU General Public License v3.0](https://github.com/tmidi/flask-launch/blob/master/LICENSE). Feel free to use the set in both personal and commercial projects. Attribution is much appreciated but not required.
