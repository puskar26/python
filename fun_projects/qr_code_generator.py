import qrcode

link = input("Enter a link to generate QR :").strip()

qr_code = qrcode.make(link)

file_name = input("Enter the name for your image (Ex:- qrcode): ").strip() 

file_name = file_name +".png"

qr_code.save(file_name)
print(f"QR code generated and saved as {file_name}")
print("Check your current directory for the image.")
