"""
为Django实现装饰器绑定路由表
Usage:
    in urls.py module call getRoute() first:
        urlpatterns = []
        route = getRoute(urlpatterns)
        from . import views

    in views.py use route as decoractor
        from .urls import route
        @route(regex)
        def view_func(request, ...):...
"""
def getRoute(urlpatterns):
    def route(url_path):
      def bind(func):
        urlpatterns.append(url(url_path, func))
        return func
      return bind
    return route
