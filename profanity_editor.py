import urllib

def read_text():
    quotes = open("/Users/rejoice/Downloads/Ewart /Python/profanity editor/movie_quotes.txt")
    contents_of_files = quotes.read()
    print(contents_of_files)
    quotes.close()
    check_profanity(contents_of_files)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    
read_text()
