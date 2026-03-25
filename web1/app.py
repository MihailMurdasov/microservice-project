import os
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
import signal
import sys


class WebHandler(BaseHTTPRequestHandler):
    """
    Обработчик HTTP запросов для микросервиса
    Поддерживает два эндпоинта:
    1. / — основной, возвращает имя контейнера
    2. /health — для проверок стостояний Docker и Nginx
    """
    
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
            return
        
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        
        hostname = socket.gethostname()
        app_name = os.environ.get("APP_NAME", "UNKNOWN")
        
        message = f"Hello from {app_name} ({hostname})\n"
        self.wfile.write(message.encode("utf-8"))


    def log_message(self, format, *args):
        """
        Отключаем стандартное логирование Python http.server
        (чтобы не засорять вывод логов Docker)
        """
        pass


def signal_handler(sig, frame):
    """
    Корректно останавливаем сервер при SIGTERM от Docker
    """
    print("\nПолучен SIGTERM. Останавливаем сервер...")
    sys.exit(0)


def main():
    """
    Запускает HTTP сервер на порту 8000.
    """
    signal.signal(signal.SIGTERM, signal_handler)
    
    server_address = ("0.0.0.0", 8000)
    httpd = HTTPServer(server_address, WebHandler)
    
    print(f"Микросервис запущен на порту 8000 (APP_NAME={os.environ.get('APP_NAME', 'UNKNOWN')})")
    print(f"Healthcheck: http://localhost:8000/health")
    
    httpd.serve_forever()


if __name__ == "__main__":
    main()
