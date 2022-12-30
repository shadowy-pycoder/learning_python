#!/usr/bin/env python3

# url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = "cnet"


def domain_name(url: str) -> str | None:
    '''
    Takes an url-address and extracts and returns domain name.
    '''
    if len(url.split('.')) < 2:
        return
    url_list = url.split('/')
    if url_list[0].startswith('http'):
        if url_list[2].startswith('www') or len(url_list[2].split('.')[0]) == 2:
            url_list = url_list[2].split('.')
            domain = url_list[1]
        else:
            url_list = url_list[2].split('.')
            domain = url_list[0]
    elif url_list[0].startswith('www') or len(url_list[0].split('.')[0]) == 2:
        url_list = url_list[0].split('.')
        domain = url_list[1]
    else:
        url_list = url_list[0].split('.')
        domain = url_list[0]
    return domain


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("youtube.com") == "youtube"
assert domain_name("https://www.youtube.com") == "youtube"
assert domain_name("https://en.youtube.com") == "youtube"
assert domain_name("en.youtube.com") == "youtube"
assert domain_name("en") == None
