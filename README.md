# strict-security-finder
This does your work easier when you want to look for the HSTS header on a website. No need to configure Proxy or opening dev tools 

## Requirment:

### packages 

- requests
- re
- bcolors
- sys
- argparse

### python > 3.x 

## usage: 

hsts.py  -u < Valid website URL with http:// or https:// >

OPTIONS: 

```
-h             --help    
             	 < show the available options >
-u            valid website URL with http:// or https://
  		< website where you want to check HSTS header value >
```
