JOURNALISM++ Web Site
=====================

## Requirements

### System dependances

	$ sudo apt-get install build-essential python-dev python-pip virtualenv sqlite3

### Node Dependances (coffeescript & Less)
	
	$ npm install


## Installation

This script will

- install a virtualenv
- download all the python dependances inside
- initialize the database (with sqlite)  

```
$ make install
```

## Launch the developement server

	$ make run
