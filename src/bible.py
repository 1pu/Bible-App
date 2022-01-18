import requests
import json

book = ""
verse = ""
url = "https://getbible.net/json?passage="
# Added For Python Applications
end = "&raw=true" shsj

def specific_bible():
    global book
    try:
        book = input(f"What book are you looking for: ").capitalize()
        chapter = input(f"What chapter are you looking for: ")
        verse = input(f"What verse are you looking for: ")
        url_response = url + book + chapter + ":" +verse + end + "&version=asv"
        response = requests.get(url_response).json()
        verse_upper = response["book"][0]["chapter"]
        verse_lower = verse_upper[verse]["verse"]
        print(verse_lower)
    except KeyError:
        print(f"I think you spelled the book wrong")
    except json.decoder.JSONDecodeError:
        print(f"There's not that many chapters in " + book)


def search_bible():
    global book, verse
    try:
        book = input(f"What Book Are You Looking For: ").capitalize()
        chapter = input(f"What Chapter Are You Looking For: ")
        # verse = input("[?] What verse are you looking for: ")
        verse_int = 1
        while True:
            verse = str(verse_int)
            url_response = url + book + chapter + ":" + verse + end + "&version=asv"
            response = requests.get(url_response).json()
            verse_upper = response["book"][0]["chapter"]
            verse_lower = verse_upper[verse]["verse"]
            print(f"Verse " + verse + ": " + verse_lower)
            verse_int = verse_int + 1
    except KeyError:
        print(f"End of chapter")
    except json.decoder.JSONDecodeError:
        print(f"That's all the verses in " + book + ".")

# specific_bible()
search_bible()
