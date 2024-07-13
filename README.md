# QOTD-Discord-Status
QOTD for your Discord status using the [zenquotes.io](https://zenquotes.io/) API

## Usage

### Install Requirements
```
pip install requests
```

### Running Script
```
python main.py
```

## Crontab Setup

```
chmod +x /path/to/script/main.py
```
```
crontab -e
```
- Add crontab config
- Get timing using [crontab.guru](https://crontab.guru/)

```
5 0 * * * /usr/bin/python3 /path/to/script/main.py >> /path/to/logfile.log 2>&1
```
> This crontab timing will make it run everyday at 12:05am

- Save and exit

- Check if crontab changes were made successfully
```
crontab -l 
```
