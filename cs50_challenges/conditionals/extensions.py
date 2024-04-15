file_type = input("File type: ")

if file_type.endswith(".gif"):
    print("image/gif")

elif file_type.endswith(".jpg") or file_type.endswith(".jpeg"):
    print("image/jpeg")

elif file_type.endswith(".pdf"):
    print("image/png")

elif file_type.endswith(".pdf"):
    print("image/pdf")

elif file_type.endswith(".zip"):
    print("image/zip")
else:
    print("application/octet-stream")