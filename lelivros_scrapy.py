#!/usr/bin/python3
import requests, bs4, sys
arq = open('links_lelivro','w')
file = open('livros_lelivros', 'w')
ant = 0
x=int(input('Qual a número de páginas que você quer examinar?'))
def examinalink(store):
	sitio=requests.get(store)
	s=bs4.BeautifulSoup(sitio.content, "lxml")
	for link in s.find_all("a"):
		if str(link.get('href')).find('=.epub')!=-1:
			file = open('livros_lelivros', 'a')
			file.write (str(link.get('href'))+'\n')
			file.close()
		
for i in range(x):
	site=requests.get('http://lelivros.love/page/'+str(i)+'/')
	try:
		site.raise_for_status()
	except Exception as exc:
		print('Ocorrem problemas: %s' %(exc))
	sitesp=bs4.BeautifulSoup(site.content, "lxml")
	for link in sitesp.find_all("a"):
		if len(str(link.get('href'))) > 65:
			atual = link.get('href')
			if atual != ant:
				arq.write (str(link.get('href'))+'\n')
				ant=atual
				examinalink(str(link.get('href')))
	arq.write('Pagina '+str(i+1)+ '\n')
arq.close()