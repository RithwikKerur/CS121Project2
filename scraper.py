import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os
import base64

def scraper(url, resp):
    links = extract_next_links(url, resp)
    valid = [link for link in links if is_valid(link)]
    return valid

def extract_next_links(url, resp):
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content
    links = []
    parser = None
    
    if resp.status == 200:
        #print(resp.raw_response.content)
        parser = BeautifulSoup(resp.raw_response.content, 'lxml')
        for link in parser.findAll('a'):
            defrag = link.get('href')
            if defrag is not None:
                defrag = defrag.split('#')[0]
                links.append(defrag)
    
    with open ('Downloads/' + str(base64.b64encode(url.encode("utf-8"))), 'w') as file:
        file.write(url + '\n')
        parser = BeautifulSoup(resp.raw_response.content, 'html.parser')

        file.write(parser.get_text())
        #file.write(''.join([x for x in parser.body.find_all(text=True)]))
        
    return links

def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        elif not (re.match(r'.*\.ics\.uci\.edu/.*', url)
                or re.match(r'.*\.cs\.uci\.edu/.*', url)
                or re.match(r'.*\.informatics\.uci\.edu/.*', url)
                or re.match(r'.*\.stat\.uci\.edu/.*', url)
                or re.match(r'today\.uci\.edu/department/information_computer_sciences/.*', url)):
            return False
        
        useless_data = {"pdf", "calendar", "?share", "upload", "?action", "?redirect", "/attachment", "?attachment", "events", "wp-login", "?ical"}
        for data in useless_data:
            if data in url:
                return False
            #print(url)
            #print(path)
            #print(re.match(r'.*\.ics\.uci\.edu/.*', 'https://wwwwics.uci.edu/resources/coronavirus/'))
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|ppsx"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise


    
