# Welcome to Link Shortener

## The why I built it and how does it work
I wanted to create the tool for shortening links the way I wanted it to be, however flexible I wanted and with a simple UI. The user will simply access the main page, paste the link he/she wants to shorten and press Enter. If the link is valid, then a message will appear to the user containing the shortened link.

Using the link is as easy as copying the shortened link and placing in into the browser's search bar. The search will be immediately redirected to the target page (if the link was registered in the database).


## How does it work in a more technical level
When the user submits the original link, the backend of the website will verify the URL in question (check if it exists and is reachable, and check for redunduncy in the database) and return the shortened link if it is valid. In case that it is not, the user will be notified via Django flash messages telling what was the problem.

For checking for reachability, the backend uses `requests`, a popular Python module for (naturally) calling requests from the web. If the status code of the request is positive for rechability, then the backend will verify if the link is already in the database and return if it is. If it is a unique URL, the link will be saved as an object of class `Link`, while the randomly generated shortened link will be saved as an object of class `ShortLink`.


