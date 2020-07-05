''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 05-07-2020
DESCRIPTION: Uso de la arquitectura MVC. Formulario HTML5, haciendo uso de Bulma y Web.py. 
'''

import web

urls = [
    '/','mvc.controllers.index.Index', 
    '/index/?','mvc.controllers.index.Index',
    '/insertar/?','mvc.controllers.insertar.Insertar',
    '/borrar/?','mvc.controllers.borrar.Borrar',
    '/view/?','mvc.controllers.view.View',
    '/modificar/?','mvc.controllers.modificar.Modificar',
    '/list/?','mvc.controllers.list.List',
    '/profile/?','mvc.controllers.profile.Profile',

] # COLOCAMOS LA RUTA

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()