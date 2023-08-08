
print("\n")

from bs4 import BeautifulSoup
import requests

url = "https://example.com/"
response = requests.get(url)

# html_code = """

# <!doctype html>
# <html>
# <head>
#     <title>Example Domain</title>

#     <meta charset="utf-8" />
#     <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <style type="text/css">
#     body {
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
#     }
#     div {
#         width: 600px;
#         margin: 5em auto;
#         padding: 2em;
#         background-color: #fdfdff;
#         border-radius: 0.5em;
#         box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
#     }
#     a:link, a:visited {
#         color: #38488f;
#         text-decoration: none;
#     }
#     @media (max-width: 700px) {
#         div {
#             margin: 0 auto;
#             width: auto;
#         }
#     }
#     </style>    
# </head>

# <body>
# <div>
#     <h1>Example Domain</h1>
#     <p>This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.</p>
#     <p><a href="https://www.iana.org/domains/example">More information...</a></p>
# </div>
# </body>
# </html>

# """

# Parse the HTML code
soup = BeautifulSoup(response.content, 'html.parser')

# Extract header from <h1> element
h_elements = soup.find_all('h1')
extracted_header = "\n".join(h.get_text() for h in h_elements)
# for header in h_elements:
#     print(header.get_text())
# print("--------------")

# Extract content from <p> elements
p_elements = soup.find_all('p')
extracted_paragraph = "\n".join(p.get_text() for p in p_elements)
# for every_line in p_elements:
#     print(every_line.get_text())

# print("--------------------------------------------------------------------------------")
# print("\n")

with open("extracted_data.txt", "w", encoding="utf-8") as file:
    file.write(extracted_header + "\n")
    file.write(extracted_paragraph)

print("Data saved to extracted_data.txt file")



