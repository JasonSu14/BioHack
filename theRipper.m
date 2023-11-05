/* This program is designed to read the information off of a web page and store it as a string. */

%reads the information off of a web page and stores it as a string

%save url
url = "https://www.merckmanuals.com/home/drug-names-generic-and-brand";

%read the html off the web
code = webread(url);

%extracts the shown text from the html code
str = extractHTMLText(code)
