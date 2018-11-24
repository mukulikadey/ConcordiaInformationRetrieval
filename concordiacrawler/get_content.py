from bs4 import BeautifulSoup
from glob import iglob

def getDocuments():
    files = []
    documents = {}
    id = 0

    for pathname in iglob('FILES/zz*.html'):
        files.append(pathname)

    for file in files:
        with open(file, 'rb') as f:
            soup = BeautifulSoup(f.read(), "html.parser")

            for script in soup(["script", "style"]):  # remove all javascript and stylesheet code
                script.extract()
            # get text
            text = soup.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)

            id += 1
            documents[id] = text
    return documents


