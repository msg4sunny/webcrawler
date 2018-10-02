def get_page(url):
	try:
	    import urllib
	    return urllib.urlopen(url).read()
	except:
	    return "error"

def get_next_target(page):
    start_link = page.find('<a href=')
    if(start_link == -1):
        return None, 0
    else:
        start_url = page.find('"',start_link)+1
        end_url = page.find('"',start_url)
        url = page[start_url:end_url]
    return url, end_url

def union(list1, list2):
	for element in list2:
		if(element not in list1):
			list1.append(element)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
