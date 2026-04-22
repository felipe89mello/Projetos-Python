import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.plusprintautomacao.com/')
except urllib.error.URLError:
    print('\33[0;31mO site Plusprint não está acessível.\33[m')
else:
    print('\33[0;32mConsegui acessar o site Plusprint com sucesso.\33[m')