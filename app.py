from exif_service import ExifService

exif_svc = ExifService("./images/DSCN0012.jpg", 'DSCN0012.jpg')

data = exif_svc.get_data()
print(data)