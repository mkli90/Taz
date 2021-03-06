[![Travis-CI Build](https://travis-ci.org/macskay/Taz.svg?branch=master)](https://travis-ci.org/macskay/Taz)
[![Coverage Status](https://coveralls.io/repos/macskay/Taz/badge.svg?branch=master)](https://coveralls.io/r/macskay/Taz)
[![Code Health](https://landscape.io/github/macskay/Taz/master/landscape.svg)](https://landscape.io/github/macskay/Taz/master)
[![PyPI version](https://badge.fury.io/py/tazlib.svg)](http://badge.fury.io/py/tazlib)
[![Python Versions](https://img.shields.io/badge/python-2.7%2C%203.4-blue.svg)](https://pypi.python.org/pypi/tazlib/)
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/macskay/Taz/blob/master/LICENSE)

# Taz: Game Loop and Scene Stack
This project is to aid people in getting started with their own Python based game.
Taz is a small library handling the switching of scenes and making sure your scenes get
updated and rendered on every tick.

The scenes will be organised in a game stack, which will automatically be updated
for all scenes whenever a new scene is registered with the Taz library. 
The user has the opportunity to force scene changes in pushing or popping from the game's
stack. Whenever the user pops the last stacked scene the game will come to an end.

Taz works independent of any python based game library.

# Documentation

To get to the documentation of Taz please follow this link:
http://taz.readthedocs.org/en/latest/

Documentation-Status: [![Documentation Status](https://readthedocs.org/projects/taz/badge/?version=latest)](https://readthedocs.org/projects/taz/?badge=latest)




