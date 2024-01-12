# twitter profile data extraction
def extractionv1():
    url = input("URL: ").strip()
    # we can use regex to extract the data
    # print(url)
    username = url.replace("https://twitter.com/", "")
    print(username)
    # this is one way to extract the data but its fragile


def extractionv2():
    url = input("URL: ").strip()
    username = url.removeprefix("https://twitter.com/")
    # this way we can handle one case like if there is input
    # my name is https://twitter.com/username it would have omitted the https://twitter.com/ part
    # but after using removeprefix it will only remove the prefix if it is present.
    print(username)


def extractionv3():
    import re
    # re.sub(pattern, repl, string, count=0, flags=0)
    url = input("URL: ").strip()
    # fine and replace the regex https://twitter.com/ with empty string
    # ^ means start of the string but we dont want use $ as it means end of the string
    usrname = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
    # so we use \ to escape it
    print(usrname)


def extractionv4():
    import re
    url = input("URL: ").strip()
    # m = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
    if m := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$",
                      url, re.IGNORECASE):
        print(m.group(3))
    else:
        print("Invalid URL")


def extractionv5():
    import re
    url = input("URL: ").strip()
    # ?:means yeah there is a group but dont capture it
    if m := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$",
                      url, re.IGNORECASE):
        print(m.group(1))
    else:
        print("Invalid URL")
# improve the code by using ?: to make the group non capturing
# WE CAN IMPROVE IT FURTHUR AS the usrname only contains alphanumeric characters\


def extractionv6():
    import re
    url = input("URL: ").strip()
    # ?:means yeah there is a group but dont capture it
    if m := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$",
                      url, re.IGNORECASE):
        print(m.group(1))
    else:
        print("Invalid URL")


extractionv6()
