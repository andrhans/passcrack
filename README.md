# README.md
Files in the repository:
* [pass-cracker.py](#zip-password-cracker)
* [hash-cracker.py](#hash-cracker)

## ZIP Password Cracker
`file:pass-cracker.py`

This is a script for cracking the password of protected zip files.

First written following a course, with more development to e.g. beautify and eliminate the use of `os` library and to allow for custom wordlist to be set.

Further versions may come...

### Usage

```
$ python pass-cracker.py info.zip wordlist.txt
 ______          ____                _             
|__  (_)_ __    / ___|_ __ __ _  ___| | _____ _ __ 
  / /| | '_ \  | |   | '__/ _` |/ __| |/ / _ \ '__|
 / /_| | |_) | | |___| | | (_| | (__|   <  __/ |   
/____|_| .__/   \____|_|  \__,_|\___|_|\_\___|_|   
       |_|                                         


unzip -P password info.zip
Archive:  info.zip
   skipping: file.txt                incorrect password

unzip -P james info.zip
Archive:  info.zip
   skipping: file.txt                incorrect password

unzip -P clara info.zip
Archive:  info.zip
   skipping: file.txt                incorrect password

unzip -P 123456 info.zip
Archive:  info.zip
   skipping: file.txt                incorrect password

unzip -P 12345 info.zip
Archive:  info.zip
   skipping: file.txt                incorrect password

unzip -P 123456789 info.zip
Archive:  info.zip
   skipping: file.txt                incorrect password

unzip -P batboys info.zip
Archive:  info.zip
  inflating: file.txt                


************************************************************
Password found: batboys
************************************************************
```

More coming!

## Hash Cracker
`file:hash-cracker.py`

This is a script for cracking md5 hashes.

### Usage
```
$ python hash-cracker.py wordlist.txt
 _   _           _        ____                _             
| | | | __ _ ___| |__    / ___|_ __ __ _  ___| | _____ _ __ 
| |_| |/ _` / __| '_ \  | |   | '__/ _` |/ __| |/ / _ \ '__|
|  _  | (_| \__ \ | | | | |___| | | (_| | (__|   <  __/ |   
|_| |_|\__,_|___/_| |_|  \____|_|  \__,_|\___|_|\_\___|_|   
                                                            

Hash of victim: 5f4dcc3b5aa765d61d8327deb882cf99

**************************************************
Password found

password::5f4dcc3b5aa765d61d8327deb882cf99
**************************************************
```

### Development ideas

- Crack multiple types of hashes specified by user input and later taken as an argument.

```
encoding=input("Encoding algorithm: ")
```

