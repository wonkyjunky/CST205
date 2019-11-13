from urllib.request import urlopen
# Use the web page you chose here:
my_site = "https://csumb.edu/"
html = urlopen(my_site)
# Print out a portion of the HTML
print(html.read())