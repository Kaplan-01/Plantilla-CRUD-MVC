''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 05-07-2020
DESCRIPTION: Uso de la arquitectura MVC. Formulario HTML5, haciendo uso de Bulma y Web.py. 
'''

import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/")

class List():
    
    def GET(self):
        try:
            return render.list() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.
