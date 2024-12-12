from fasthtml.common import *



app, rt = fast_app()

@app.get("/fasthtml-deploy-test/")
def home():
    page = Html(
        Head(
            Title('Test'),
            picolink,
        ),
        Body(
            header,
            Main(
                H1('Welcome to the Main Page'),
                P('Content goes here...'),
                cls='container',
            ),
            style,
        ),
        data_theme="light"
    )
    return page

@app.get("/fasthtml-deploy-test/miembros")
def miembros():
    page = Html(
        Head(
            Title('Miembros'),
            picolink,
        ),
        Body(
            header,
            Main(
                H1('Welcome to the Members Page'),
                P('Hello members!'),
                cls='container',
            ),
            style,
        ),
        data_theme="light"
    )
    return page

@app.get("/fasthtml-deploy-test/publicaciones")
def publicaciones():
    page = Html(
        Head(
            Title('Publicaciones'),
            picolink,
        ),
        Body(
            header,
            Main(
                H1('Welcome to the Publications Page'),
                P('Publications here'),
                cls='container',
            ),
            style,
        ),
        data_theme="light"
    )
    return page

picolink = Link(rel="stylesheet", href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css")
header = Header(
    Nav(
        A('LOGO', href='/fasthtml-deploy-test/', cls='logo'),
        Div(
            A('Miembros', href='/fasthtml-deploy-test/miembros'),
            A('Publicaciones', href='/fasthtml-deploy-test/publicaciones'),
            cls='tabs'
        ),
    ),
    cls='banner'
    )
style = Style(
    ".content {margin: 0 auto; max-width: 1200px; background-color: white;}" +
    ".banner {height: 50px; background-color: #332c2f; color: white; padding: 0 20px; margin: 0 auto; width: 100%;}" +
    ".logo {font-size: 1.5em; font-weight: bold;}" +
    ".tabs {display: flex; gap: 40px; justify-content: center; align-items: center; margin: 0 auto;}"
    )

serve()