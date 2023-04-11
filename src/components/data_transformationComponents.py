import re
import sys
from src.exception import customException
from urllib.parse import urlparse
from googlesearch import search
from tld import get_tld
import os.path

#Use of IP or not in domain
class transformationFunctions():

    def __init__(self):
        pass

    def having_ip_address(self, url):
        try:
            match = re.search(
                '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
                '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
                '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
                '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
            if match:
                return 1
            else:
                return 0
            
        except Exception as e:
            raise customException(e,sys)
        
    def abnormal_url(self, url):
        try:
            hostname = urlparse(url).hostname
            hostname = str(hostname)
            match = re.search(hostname, url)
            if match:      
                return 1
            else:
                return 0

        except Exception as e:
            raise customException(e,sys)
        

    def count_dot(self, url):
        try:
            count_dot = url.count('.')
            return count_dot

        except Exception as e:
            raise customException(e,sys)
        

    def count_www(self, url):
        try:
            url.count('www')
            return url.count('www')
        except Exception as e:
            raise customException(e,sys)
        
    
    def count_atrate(self, url):
        try:
            return url.count('@')
        except Exception as e:
            raise customException(e,sys)
        

    def no_of_dir(self, url):
        try:
            urldir = urlparse(url).path
        #     print(urldir)
            return urldir.count('/')
        except Exception as e:
            raise customException(e,sys)
        

    def no_of_embed(self, url):
        try:
            urldir = urlparse(url).path
            return urldir.count('//')
        except Exception as e:
            raise customException(e,sys)
        
    
    def suspicious_words(self, url):
        try:
            match = re.search('PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr',
                            url)
            if match:
                return 1
            else:
                return 0
        except Exception as e:
            raise customException(e,sys)
        
    
    def shortening_service(self, url):
        try:
            match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                            'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                            'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                            'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                            'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                            'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                            'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                            'tr\.im|link\.zip\.net',
                            url)
            if match:
                return 1
            else:
                return 0
        except Exception as e:
            raise customException(e,sys)
        
    
    def count_https(self, url):
        try:
            return url.count('https')
        except Exception as e:
            raise customException(e,sys)
        

    def count_http(self, url):
        try:
            return url.count('http')
        except Exception as e:
            raise customException(e,sys)
        

    def count_per(self, url):
        try:
            return url.count('%')
        except Exception as e:
            raise customException(e,sys)
        
    
    def count_ques(self, url):
        try:
            return url.count('?')
        except Exception as e:
            raise customException(e,sys)
        

    def count_hyphen(self, url):
        try:
            return url.count('-')
        except Exception as e:
            raise customException(e,sys)
        

    def count_equal(self, url):
        try:
            return url.count('=')
        except Exception as e:
            raise customException(e,sys)
        

    def url_length(self, url):
        try:
            return len(str(url))
        except Exception as e:
            raise customException(e,sys)
        

    def hostname_length(self, url):
        try:
            return len(urlparse(url).netloc)
        except Exception as e:
            raise customException(e,sys)
        

    #First Directory Length
    def fd_length(self, url):
        try:
            urlpath= urlparse(url).path
            try:
                return len(urlpath.split('/')[1])
            except:
                return 0
        except Exception as e:
            raise customException(e,sys)
        
    
    def tld_length(self, tld):
        try:
            try:
                return len(tld)
            except:
                return -1
        except Exception as e:
            raise customException(e,sys)
        
    
    def digit_count(self, url):
        try:
            digits = 0
            for i in url:
                if i.isnumeric():
                    digits += 1
            return digits
        except Exception as e:
            raise customException(e,sys)
        

    def letter_count(self, url):
        try:
            letters = 0
            for i in url:
                if i.isalpha():
                    letters += 1
            return letters
        except Exception as e:
            raise customException(e,sys)




# if __name__=="__main__":
#     obj = transformationFunctions()
#     url = "https://google.com/"
#     use_of_ip = obj.having_ip_address(url)
#     abnormal_url = obj.abnormal_url(url)
#     countDot = obj.count_dot(url)
#     countWWW = obj.count_www(url)
#     countATR = obj.count_atrate(url)
#     count_dir= obj.no_of_dir(url)
#     count_embed_domain = obj.no_of_embed(url)
#     short_url = obj.shortening_service(url)
#     countPercentage = obj.count_per(url)
#     countQUES = obj.count_ques(url)
#     countHyphen = obj.count_hyphen(url)
#     countEqual = obj.count_equal(url)
#     url_length = obj.url_length(url)
#     count_https = obj.count_https(url)
#     count_http = obj.count_http(url)
#     hostname_length = obj.hostname_length(url)
#     sus_url = obj.suspicious_words(url)
#     fd_length = obj.fd_length(url)
#     tld_length = obj.tld_length(url)
#     count_digits = obj.digit_count(url)
#     count_letters = obj.letter_count(url)

    
