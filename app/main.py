from selenium.webdriver import Firefox
from time import sleep

url = "https://curso-python-selenium.netlify.app/aula_03.html"
navegador = Firefox()
navegador.get (url)
sleep (20)

a = navegador.find.element_by_tag_name("a")
p = navegador.find.element_by_tag_name("p")

print (f"texto de a: {a.text}")
print (f"texto de p: {b.text}")
