import partA
import partB
from collections import defaultdict
import os

def calculateStatistics():
    directory = 'Downloads'
    common_words = defaultdict(int)
    unique_pages = set()
    longest_page = ['None', -1]
    subdomain_urls = defaultdict(int)

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        
        all_tokens = partA.tokenize(f)
        if len(all_tokens) < 10000:
            with open(f, 'r') as curr_file:
                url = curr_file.readline()
                defrag_url = url.split('#')[0]
                unique_pages.add(defrag_url.rstrip('\n'))

            # with open(filename, 'r') as f:
            #print(f'{url} has {len(all_tokens)} number of words')
            if longest_page[0] == 'None' or len(all_tokens) > longest_page[1]:
                longest_page[0], longest_page[1] = str(url), len(all_tokens)
            partA.countFrequencies(all_tokens, common_words)

    
    with open('results.txt', 'w') as results:
        for page in unique_pages:
            if 'ics.uci.edu' in page:
                parsed = page.split('/')
                domain =parsed[2]
                subdomain_urls[domain] += 1

        results.write('Number of Unique Pages: ' + str(len(unique_pages))+ '\n')
        results.write('Longest Page: ' + longest_page[0]+ '\n')

        # for token, count in sorted(counts.items(), key=lambda token : token[1]):
        i = 0
        while i < 50 and i < len(common_words):
            results.write(f'{i+1}. ' + sorted(common_words.items(), key=lambda token:token[1], reverse=True)[i][0]+ '\n')
            i += 1

        for subdomain, count in sorted(subdomain_urls.items(), key = lambda x: x[0]):
            output = f'{subdomain}, {count}\n'
            results.write(output)

if __name__ == '__main__':
    calculateStatistics()