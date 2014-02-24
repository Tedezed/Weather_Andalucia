import requests
import json
capital = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']
val = 1

for num in capital:
	print val,'.',num
	val = val + 1

parametro = int(raw_input("De que ciudad quieres saber la temperatura actual?"))
parametro = parametro - 1

fichero = requests.get('http://api.openweathermap.org/data/2.5/weather/', params={'q':'%s,spain' %capital[parametro]})
dicc=json.loads(fichero.text)
fel = int(dicc['main']['temp'])
cent=fel-273
print ""
print 'La temparatura actual de',capital[parametro],'es',cent,'grados centigrados'
