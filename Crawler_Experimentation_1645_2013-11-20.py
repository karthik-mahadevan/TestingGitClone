import os
url_list =[]
url_positions = []
def GetUrlPositions(Pagestr):
	UrlTag = 'href='
	current_position = 0
	while current_position in range(len(Pagestr)):
		if Pagestr.find(UrlTag,current_position) == -1:
			break
		else:
			current_url_position = Pagestr.find(UrlTag,current_position) + len(UrlTag) + 1
			url_positions.append(current_url_position)
			current_position = current_url_position
			print current_position, Pagestr[current_position], Pagestr[current_position + 1], Pagestr[current_position + 2]

#def NextGetUrl(Pagestr,pos):
#	UrlTag = '<a href ='
#	LinkPos = Pagestr.find(UrlTag,pos) + len(UrlTag) + 1
#	global url_list

os.chdir("/Users/ranjani/Documents/Karthik/Credibase/Python/Code/Data")
Page = open("Crawler_source_ page_ 3.html","r")
PageSource = Page.read()
Page.close()
GetUrlPositions(PageSource)
print url_positions
