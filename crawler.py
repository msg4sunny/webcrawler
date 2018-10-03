
#Crawler
def get_page(url):
	"""
	   Given the url, get page using urllib
	"""
	try:
	    # Read page in try-catch block to catch any exception that may happen
	    import urllib
	    return urllib.urlopen(url).read()
	 
	except:
	    return "error"

def get_next_target(page):
    """
    returns next URL link in the page 
    """
    # find next html tag '<a href='
    start_link = page.find('<a href=')
    if(start_link == -1):
	# if there is no link, return None
        return None, 0
    else:
	# Make URL using " and append it in variable url
        start_url = page.find('"',start_link)+1
        end_url = page.find('"',start_url)
        url = page[start_url:end_url]
    return url, end_url

def union(list1, list2):
	"""
	Take union of 2 list
	"""
	
	for element in list2:
		# loop on list2
		if(element not in list1):
			# append element in list1 if not present already
			list1.append(element)

def get_all_links(page):
    """
    Get all the links present in page
    """

    links = []
    while True:
        url,endpos = get_next_target(page)
	# loop endlessly untill we are getting urls
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
	"""
	Given seed, crawl all the pages and inner-pages of those links
	"""
	
	tocrawl = [seed]
	crawled = []
	index = []
	# Loop till tocrawl gets empty
	while tocrawl:
		page = tocrawl.pop()
		if(page not in crawled):
			# Get content of the page
			content = get_page(page)
			
			# Add content/words to index for ref
			add_page_to_index(index, page, content)
			
			# Take union of content to get inner-links of the pages
			union(tocrawl, get_all_links(content))
			
			# Add current page into crawled list
			crawled.append(page)
	return index

#Index

def add_to_index(index, keyword, url):
	"""
	Update index list: keep track of words occuring in different urls
	"""
	for entry in index:
		if(entry[0] == keyword):
			entry[1].append(url)
			return
	index.append([keyword,[url]])

def lookup(index, keyword):
	"""
	Lookup for word in index and returns list of URLs if present
	"""
	
	for entry in index:
		if(entry[0] == keyword):
			return entry[1]
	return []

def add_page_to_index(index, url, content):
	"""
	Update index list: keep track of words occuring in different urls using add_to_index()
	"""
	words = content.split()
	for word in words:
		add_to_index(index, word, url)
