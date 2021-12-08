# HPC backup overview

*Contents*
* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
* [Disclaimer](#disclaimer)

<br>

### Description

Some HPC's makes use of work directories that have a set time limit before files are removed.

**SAGA uses 42 days autocleanup period, but if the system is at 70% this gets moved down to 21 days**

To keep track of this one can use this simple script to have a list of objects that are on work directory. 


<br>


### Installation

Downlad the code repository, add the python script to your aliases if you want to use it from anywhere.


<br>

### Usage

To add a new elemnt to the list.

```python
bkup.py --name Task1
```
which results in a file that has the task name and the timestamp written to it,

```
Task1    28-12-2021 12:04
```
<br>

Remove object from list.

```python
bkup.py --remove Task1
```
<br>

List objects in file.

```python
bkup.py --reminder
```

<br>

Get some help

```python
bkup.py --help
```

which prints,

```python
usage: bkup.py [-h] [--name NAME] [--remove REMOVE] [--remind]

optional arguments:
  -h, --help       show this help message and exit
  --name NAME      Name for backup object that needs to be updated in 20 days.
  --remove REMOVE  Remove backup object from list of objects to be backed up.
  --remind         List of backup objects and their end date before backup
```

<br>


### Disclaimer

You could also just use the timestamps on your files, but if your work on multiple objects at the same time in can be cleaner to have every object in one list. This was written for personal usage, so use at your own risk.