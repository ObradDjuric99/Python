def write_logs(file_name, data):
    with open(file_name, "a") as f:
        f.write(data + "\n")

