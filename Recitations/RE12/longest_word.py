
def longest_word(url):
    import urllib.request as urlreq
    response = urlreq.urlopen(url)
    html = set(response.read().decode().split())

    with open("words") as f:
        words = f.read().split()
    
    common_words = html.intersection(words)
    
    return min(common_words, key=lambda x: (-len(x), x))