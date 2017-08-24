import glob
import os

from bs4 import BeautifulSoup

html_docs = glob.glob(os.path.join('./jsc_print100k/', '*'))
if not os.path.exists('jsc_plain_pages_100k'):
    os.mkdir('jsc_plain_pages_100k')
for i, doc in enumerate(html_docs):
    print('process ', doc)
    out_file = "./jsc_plain_pages_100k/jsc_{}.txt".format(str(i).zfill(5))
    file_writer = open(out_file, mode='w')
    text = open(doc).read()
    soup = BeautifulSoup(text, 'html.parser')
    title = soup.find(attrs={'id': "lblHeadLine"}).get_text().strip()
    file_writer.write(title + "\n")
    date = soup.find(attrs={'id': "lblPublishDate"}).get_text().strip()
    file_writer.write(date + "\n")
    body = soup.find(attrs={'class': "PDA_jazeera_Body"}).get_text()
    lines = [s.rstrip() for s in body.split("\n") if s.rstrip()]
    for line in lines:
        file_writer.write(line + "\n")



