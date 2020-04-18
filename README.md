# FTP-Farmer
This tool make an easy way to test Anonymous login and Brute force attacks on FTP.

## Installation
```bash
pip install colorama
pip install requests
```

## Usage
```python3
FTPFarmer -a 
```
:+1: Test Anonymous login.

```python3
FTPFarmer -b 
```
:+1: Test BruteForece attack.

### Hint:
  - **Target:** FTP url or IP without \'http://\' or \'https://\'.
  - **User:** Username to login with FTP.
  - **Password:** Password list file path.
