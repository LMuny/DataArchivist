def secure_archive(file_name: str, mode: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(file_name, "r") as f:
                data = f.read()
            return (True, data)
        if mode == "write":
            with open(file_name, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        return (False, "Invalid Option")
    except Exception as e:
        return (False, str(e))
