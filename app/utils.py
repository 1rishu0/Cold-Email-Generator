import re

def clean_text(text):
    # Remove HTML Tags
    text = re.sub(r'<[^>]*?>','',text)
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))','',text)
    # Remove special Characters 
    text = re.sub(r'[^a-zA-Z0-9]','',text)
    # Replace Multiple Spaces with a Single space 
    text = re.sub(r'\s{2,}','',text)

    text = text.strip()
    # Remove extra Whitespaces 
    text = ' '.join(text.split())
    return text