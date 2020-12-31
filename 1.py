#solution 1
# With regex 
# @Todo : implimentation required for http:// and https://
import re
# website URLs
weblist=['blog.microsoft.com/test.html',
'www.blog.microsoft.com/test',
'www.microsoft.com '
]
for web in weblist:
 subdomainRes =re.search(r'^([a-z0-9]+([\-a-z0-9]*[a-z0-9]+)?\.){0,}([a-z0-9]+([\-a-z0-9]*[a-z0-9]+)?){1,63}(\.[a-z0-9]{2,7})',web)
 print(web, '|', subdomainRes.group(1))
 
 #solution 2
 # Without Regex 
 # @Todo : implimentation required for omiting www as subdomain
websiteUrl = 'https://blog.microsoft.com/test.html'
webhost = websiteUrl.partition('://')[2]
subDomain = webhost.partition('.')[0]
print (subDomain)
