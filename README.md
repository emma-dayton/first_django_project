# First Django Project

Here you'll find my first project using Django, it displays a few basic
route in order to understand the basic file structure and the routing
format of Django.

To see the various routes in action, run the file and navigate the browser to
localhost:8000

Paths
* /  --  home path with placeholder text for a blog homepage
* /new  --  set path with placeholder text
* /create -- set path that redirects to homepage
* /<num>  -- variable path that fits a number variable, using regex matching
* /<num>/edit  -- variable path using regex matching
* /<num>/delete  -- variable path that redirects to homepage

# Random Words App

As a further assignment, I added a second app to this project. If you run the django
server and then go to localhost:8000/random_word you'll find the fruits of this
assignment. Very basic styling just to get further practice in linking style sheets
according to Django syntax.

Paths
* /random_word  -- home path for this app, will display a random string upon loading
* /random_word/new -- redirects to home path, which increments the session count
* /random_word/clear -- redirects to home path after clearing session count
