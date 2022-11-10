# Brain games

[![Actions Status](https://github.com/borisovaldv/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/borisovaldv/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/8fb3116cd1e82ee64764/maintainability)](https://codeclimate.com/github/borisovaldv/python-project-49/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8fb3116cd1e82ee64764/test_coverage)](https://codeclimate.com/github/borisovaldv/python-project-49/test_coverage)

## Description

'Brain games' is a set of five simple command line interface games. Each game have a question you should ask properly. Conditions: you answer correctly three times in a row = you win. If you're wrong, the program will prompt you to start the game all over again. There are five games:

* Determining if the number is even
* Calculator
* Determining if the number is prime
* Progression game. Finding missing number 
* Determining the largest common divisor

## Installation

Make sure you have everything to install the package:

### Python 3.8.0+  
https://www.python.org/downloads/
### Poetry
https://python-poetry.org/docs/
### Package itself
```bash
# clone via SSH:
>> git@github.com:borisovaldv/python-project-49.git
```

### After installation:
```bash
>> cd python-project-49/
>> poetry build
>> python -m pip install --user dist/*.whl
```

## Usage
### Determining if the number is even
```bash
>> brain-even
```
### Calculator
```bash
>> brain-calc
```
### Determining if the number is prime
```bash
>> brain-prime
```
### Progression game. Finding missing number 
```bash
>> brain-progression
```
### Determining the largest common divisor
```bash
>> brain-gcd
```

## Development

### Useful commands

* `make install` — install all dependencies in the environment
* `make build` — build the wheel
* `make lint` — checking code with linter