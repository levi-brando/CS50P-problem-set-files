def main():
    file_name = input("File name: ")
    suffix = file_name.lower().strip()
    suffix = suffix.split(".")[-1]

    match suffix:
        case "gif":
            print("image/gif")
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
