# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
from requests import get

def save(link, flag):
	if flag == 0:
		with open('livros_lelivros.txt','a',encoding='utf-8') as first:
			first.write(link)
	else:
		with open('livros_index.txt','a',encoding='utf-8') as second:
			second.write(link)

def examinalink(store):
	sitio = get(store)
	s = bs(sitio.content, "lxml")
	for link in s.find_all("a"):
		if str(link.get('href')).find('=.epub')!=-1:
			save(str(link.get('href')) + '\n',1)

def examinapage(page):
	ant = 0
	sitesp = bs(page.content, "lxml")
	for link in sitesp.find_all("a"):
		if len(str(link.get('href'))) > 65:
			atual = link.get('href')
			if atual != ant:
				save(str(link.get('href')) + '\n',0)
				ant=atual
				examinalink(str(link.get('href')))

def queue(pages):
	for i in range(x):
		site = get('http://lelivros.love/page/'+str(i)+'/')
		examinapage(site)
		save('Pagina '+str(i+1)+ '\n',0)

if __name__ == "__main__":
	x = int(input('Qual a número de páginas que você quer examinar?'))
	with open('livros_lelivros.txt','w') as first, open('livros_index.txt','w') as second:
		pass
	queue(x)