import sys
import requests
import BeautifulSoup as bs

## This function returns the number of results for a given search keyword
def numberOfResults(kw):
    pg_number = 1

    num_results = 0

    ##print kw

    while(True):
        ## Requesting the a single page result for the keyword
        res = requests.get(
            "http://www.shopping.com/products~PG-%d?KW=%s"%(pg_number, kw))

        ## Ensuring that the request was successful
        if (res.status_code != requests.codes.ok):
            break

        soup = bs.BeautifulSoup(res.text)

        ## Finding all the results for keyword
        ## in the page
        elems = soup.findAll('div', 'gridItemTop')

        ##print len(elems)

        if (len(elems) == 0):
            break

        num_results += len(elems)

        pg_number += 1

    return num_results

## This function returns the search results for a key word in a
## page with specified page number
def getResults(page, kw):
    ## Requesting the a single page result for the keyword
    my_url = "http://www.shopping.com/products~PG-%d?KW=%s"%(page, kw)
    res = requests.get(my_url)

    ## Ensuring that the request was successfuls
    if (res.status_code != requests.codes.ok):
        print "Keywords not found"

    soup = bs.BeautifulSoup(res.text)

    ## Finding all the results for keyword
    ## in the page
    elems = soup.findAll('div', 'gridItemTop')

    ## Extracting the title for each result in the page
    results = [elem.img['title'] for elem in elems]

    return results
    
def main():
    if (len(sys.argv) == 2):
        kw = sys.argv[1]
        print numberOfResults(kw)

    if (len(sys.argv) > 2):
        page = int(sys.argv[1])
        kw = "+".join(sys.argv[2:])
        for result in getResults(page, kw):
            print result, "\n"

if __name__ == "__main__":
    main()
