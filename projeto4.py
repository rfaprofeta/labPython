#!/usr/bin/python3
import requests, bs4
ax=requests.get('http://www.bmfbovespa.com.br/pt_br/produtos/listados-a-vista-e-derivativos/renda-variavel/empresas-listadas.htm')
#type(ax)
try:
	ax.raise_for_status()
except Exception as exc:
	print('Ocorrem problemas: %s' %(exc))
axsoup=bs4.BeautifulSoup(ax.content, 'html.parser')
print(axsoup.prettify())
