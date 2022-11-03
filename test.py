import scraper
val = 1

def test_download():
    global val
    with open ('Test/' + str(val), 'w') as file:
        file.write(str(val) + '\n')
        #parser = BeautifulSoup(resp.raw_response.content, 'html.parser')

        #file.write(parser.get_text())
        #file.write(''.join([x for x in parser.body.find_all(text=True)]))
        val += 1



if __name__ == '__main__':
    class Val:
        status = 200
        