# polar-localiser
download entire Polar Bookshelf library

USAGE:
- pip install selenium
- see [selenium docs](https://selenium-python.readthedocs.io/installation.html) for setting up drivers
- to find total library size, open Polar, hit F12, scroll to the bottom of the library and use the element picker to see the hover over the last PDF. It will say something like ```enhanced-table-checkbox-XXX``` where XXX is the size of your libary. 
- run python3 from terminal, then proceed to run each line in ```dl.py```. You could set it up with pdb and run the whole script at once, but I found it easier to go line by line - plus that makes it easy to go through the Polar email 2FA
- after you run ```driver = webdriver.Firefox()``` and ```driver.get("https://app.getpolarized.io")``` - log in to polar with your email manually. Sorry, but I didn't feel like implementing a fetch for the 2FA code they send. This is quicker
- after you're in to the main polar screen:
  - run each line of the above script. Due to some peculiarities with how polar handles scrolling, the quickest way to get what you want (your library locally) is just to sit and scroll down slowly after you run the ```for i in range(LIB_SIZE):``` loop from terminal
  - keep scrolling
  -
  -
  - keep scrolling
  -
  - done! 

(it took about 5 minutes for me to download all ~900 PDFs in my library by this method, whereas figuring out how to get selenium to implement mouse-scrolling would have taken another 20 at least!)

Enjoy. 
