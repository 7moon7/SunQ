def list_user(conn, param_dict=None):
    conn.send("HTTP/1.1 200 OK \r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(encoding="utf-8"))
    conn.send("<h1>这是首页!</h1>".encode(encoding="utf-8"))


def detail(conn, param_dict=None):
    conn.send("HTTP/1.1 200 OK \r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(encoding="utf-8"))
    conn.send(("<h1>这是[%s]详情页!</h1>" % param_dict.get('k')).encode(encoding="utf-8"))


def page_not_found(conn, param_dict=None):
    conn.send("HTTP/1.1 404 OK \r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(encoding="utf-8"))
    conn.send(("<h1>Page Not Found</h1>").encode(encoding="utf-8"))


urlpatterns = [
    ('/index', list_user),
    ('/detail', detail),
]


