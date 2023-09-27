import toga
from toga.style import Pack
from toga.style.pack import COLUMN, FLEX
from android import android_url_open
import os

class WebViewApp(toga.App):
    def startup(self):
        # Crea una ventana principal
        self.main_window = toga.MainWindow(title=self.name)

        # Crea un contenedor para organizar los componentes
        container = toga.Box(style=Pack(direction=COLUMN))

        # Crea un WebView para mostrar el contenido HTML
        self.webview = toga.WebView(style=Pack(flex=FLEX))
        container.add(self.webview)

        # Ruta al archivo HTML local
        html_file = os.path.join(os.path.dirname(__file__), 'archivo.html')

        # Carga y muestra el archivo HTML en el WebView
        self.webview.url = android_url_open(html_file)

        # Agrega el contenedor a la ventana principal
        self.main_window.content = container

def main():
    return WebViewApp('WebView App', 'org.example.webviewapp')

if __name__ == '__main__':
    app = main()
    app.main_loop()
