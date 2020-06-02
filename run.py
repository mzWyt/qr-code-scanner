from camera import Take_Image
from qr_reader import Read_QR

img = 'qr.png'

if __name__ == '__main__':
    
    Take_Image(img)
    print(Read_QR(img))
