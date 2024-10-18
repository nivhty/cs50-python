fileext = input("Filename: ")
fileext = fileext.strip().lower()
if fileext.endswith(".gif"):
    filetype = 'image/gif'
elif fileext.endswith(".jpg") or fileext.endswith(".jpeg"):
    filetype = 'image/jpeg'
elif fileext.endswith(".png"):
    filetype = 'image/png'
elif fileext.endswith(".pdf"):
    filetype = 'application/pdf'
elif fileext.endswith(".txt"):
    filetype = 'text/plain'
elif fileext.endswith(".zip"):
    filetype = 'application/zip'
else:
    filetype = 'application/octet-stream'
print(filetype)
