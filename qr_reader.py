import zxing

def Read_QR(img):

    reader = zxing.BarCodeReader()
    barcode = reader.decode(img)

    if barcode.type == None:
        return "Fail to read"

    return barcode.parsed