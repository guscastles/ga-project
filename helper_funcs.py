from urllib.parse import urlparse
from urllib.parse import parse_qs
import socket

# HTTP Status Code Functions

def http_status_is_200_parser(http_status_code):
    """
    Call this function parsing the HTTP status code as parameter.
    It will return True if the status is 200, otherwise False.
    """
    if http_status_code == 200:
        return True
    else:
        return False


def http_status_range_parser(http_status_code):
    """
    Call this function parsing the HTTP status code as parameter.
    It will return a string with the status code range.
    """
    if str(http_status_code).startswith('1'):
        return '1xx'
    elif str(http_status_code).startswith('2'):
        return '2xx'
    elif str(http_status_code).startswith('3'):
        return '3xx'
    elif str(http_status_code).startswith('4'):
        return '4xx'
    elif str(http_status_code).startswith('5'):
        return '5xx'
    else:
        return 'other'

    
def http_status_main(http_status_code):
    
    is_200 = http_status_is_200_parser(http_status_code)
    
    status_range = http_status_range_parser(http_status_code)
    
    return (is_200, status_range)

    
# Parameter Functions

def get_query_string(url):
    """
    Call this function passing a URL as the parameter.
    It returns the full query string of the URL.
    """
    parsed_url = urlparse(url)

    return parsed_url[4]


def parse_query_string(query_string):
    """
    Call this function passing the full query string as the parameter.
    It returns a string with parameters separated by a space.
    """
    params_dict = parse_qs(query_string)

    params_list = list(params_dict.keys())

    return ' '.join(params_list)


def get_parameters(url):
    """
    This is the main function that calls the two above.
    """
    query_string = get_query_string(url)
    
    return parse_query_string(query_string)


# User Agent Functions
googlebot = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
googlebot2 = "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36"
googlebot3 = "Googlebot/2.1 (+http://www.google.com/bot.html)"
googlebot_smartphone = "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
googlebot_images = "Googlebot-Image/1.0"
googlebot_news = "Googlebot-News"
googlebot_video = "Googlebot-Video/1.0"


def user_agent_lookup(log_ua):
    """
    Call this function on a DataFrame user_agent column with apply().
    Returns a string of the Googlebot user agent.
    """
    if log_ua == googlebot:
        return 'Googlebot'
    elif log_ua == googlebot2:
        return 'Googlebot'
    elif log_ua == googlebot3:
        return 'Googlebot'
    elif log_ua == googlebot_smartphone:
        return 'Googlebot Smartphone'
    elif log_ua == googlebot_images:
        return 'Googlebot Images'
    elif log_ua == googlebot_news:
        return 'Googlebot News'
    elif log_ua == googlebot_video:
        return 'Googlebot Video'
    else:
        return 'Other'
    
    
# Verify Googlebot Function

def verifying_googlebot(bot_ip):
    """
    Call this function to verify Googlebot is real on each row of the CSV.
    Returns True or False.
    """
    try:
        host = socket.gethostbyaddr(bot_ip)
        bot_name = host[0]
    except:
        return False

    if bot_name.find("googlebot.com") < 0:
        return False

    try:
        ip = socket.gethostbyname(bot_name)
    except:
        return False

    return bot_ip == ip