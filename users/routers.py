from rest_framework.routers import Route, DynamicRoute, SimpleRouter

#simple router es la base de todos los reuters

class CustomRouter(SimpleRouter):
    """Vamos a definir un arreglo de rutas"""
    routes = [
        Route(
            url = r"^{prefix}$",
            mapping={'get': 'get'},
            name="{basename}-list",
            detail = False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url = r"^{prefix}/{lookup}$",
            mapping={'get': 'retrieve'},
            name="{basename}-detail",
            detail = True,
            initkwargs={'suffix': 'Deetail'}
        )
    ]