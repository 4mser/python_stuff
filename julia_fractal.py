# Python code for Julia Fractal
from PIL import Image
   
if __name__ == "__main__":
    
    # Definimos el Width Height y Zoom
    # of the image to be created
    w, h, zoom = 1920,1080,1
   
    # Creamos la nueva imagen en modo RGB
    bitmap = Image.new("RGB", (w, h), "white")
  
    # Cargamos el mapa de píxeles.
    pix = bitmap.load()
     
    # Declaramos las variables de acuerdo a la
    # Ecuación para crear fractales
    cX, cY = -0.7, 0.27015
    moveX, moveY = 0.0, 0.0
    maxIter = 255
   
    for x in range(w):
        for y in range(h):
            zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
            zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
            i = maxIter
            while zx*zx + zy*zy < 4 and i > 1:
                tmp = zx*zx - zy*zy + cX
                zy,zx = 2.0*zx*zy + cY, tmp
                i -= 1
  
            # Convertimos byte a RGB (3 bytes) 
            # Magia para obtener colores wapos
            pix[x,y] = (i << 21) + (i << 10) + i*8
  
    #M ostramos el Fractal creado
    bitmap.show()