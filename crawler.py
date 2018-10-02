
#Crawler
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

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl:
		page = tocrawl.pop()
		if(page not in crawled):
			content = get_page(page)
			add_page_to_index(index, page, content)
			union(tocrawl, get_all_links(content))
			crawled.append(page)
	return index

#Index

def add_to_index(index, keyword, url):
	for entry in index:
		if(entry[0] == keyword):
			entry[1].append(url)
			return
	index.append([keyword,[url]])

def lookup(index, keyword):
	for entry in index:
		if(entry[0] == keyword):
			return entry[1]
	return []

def add_page_to_index(index, url, content):
	words = content.split()
	for word in words:
		add_to_index(index, word, url)
