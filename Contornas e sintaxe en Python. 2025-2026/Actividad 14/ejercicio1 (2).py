import qrcode

url = input('Introduce una URL: ')
imagen = qrcode.make(url)
imagen.save("url.png")
