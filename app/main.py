import os


def move_file(command: str) -> None:
    cmd, origin_file, path = command.split()
    if cmd == "mv":
        if "/" in path:
            folders, file = os.path.split(path)
            os.makedirs(folders, exist_ok=True)
            with open(origin_file, "r") as f, open(path, "w") as e:
                data = f.read()
                e.write(data)
            os.remove(origin_file)
        else:
            os.rename(origin_file, path)
