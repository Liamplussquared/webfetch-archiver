from requests_html import HTMLSession

session = HTMLSession()

# get URL from user
print("Enter a URL")
u = input()
# make initial GET request

r = session.get(u)
print("The payload from:", u, "is", r.content)

# scrape GET requests from the payload
print("\nUsing the requests_html library to scrape any GET requests from HTML.")
gets = r.html.absolute_links
print("There were", len(gets), "URLs scraped from the HTML. The parsed GETS were to the following urls\n", gets, "\n")


count = 1
# make GET request for each scraped URL
for url in gets:
    req = session.get(url)
    print("\nMaking GET request to:", url)
    print("Status code:", req.status_code)
    print("Payload is:", req.content[0:100], "...")

    # create new file and write payload into it
    fn = "url" + str(count) +".txt"
    f = open(fn, "x")
    # write content to file
    f.write(str(req.content))
    count += 1
