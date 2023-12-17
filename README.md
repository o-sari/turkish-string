# turkish-string
Provides alternative string methods to Python's built-in upper(), lower(), capitalize() and title() that work for turkish characters.

## Description
While working with Turkish strings some of the Python's built-in string methods does not work as expected.
Especially Turkish characters **İ**, **I**, **i** and **ı** won't correctly be translated to lower and upper case versions.

***turkish-string*** package provides alternative methods that solve this problem.

## Requirements
This package is tested with Python>=3.8 versions.

## Installation
```
pip install turkish-string
```

## Usage

#### To upper case
```python
from turkish_string import upper_tr

string = 'istanbul Kadıköy'

upper_case = upper_tr(string)

print(upper_case)
```
> `İSTANBUL KADIKÖY`


#### To lower case
```python
from turkish_string import lower_tr

string = 'İSTANBUL KADIKÖY'

lower_case = lower_tr(string)

print(lower_case)
```
> `istanbul kadıköy`


#### Title
```python
from turkish_string import title_tr

string = 'istanbul kadıköy'

titled = title_tr(string)

print(titled)
```
> `İstanbul Kadıköy`


#### Capitalize
```python
from turkish_string import capitalize_tr

string = 'istanbul kadıköy'

capitalized = capitalize_tr(string)

print(capitalized)
```
> `İstanbul kadıköy`


## License
Distributed under the BSD License. See LICENSE for more information.

## Contact
Omer Faruk Sari - info@aqilan.com
