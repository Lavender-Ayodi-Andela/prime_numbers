from urllib2 import Request, urlopen, URLError

request = Request('https://github.com/Lavender-Ayodi-Andela/prime_numbers')

try:
	response = urlopen(request)
	code = response.read()
	print code[559:1000]
except URLError, e:
    print 'No site. Got an error code:', e