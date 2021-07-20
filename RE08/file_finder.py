def file_finder(dirs, name):
    if dirs == name:
        return name

    if type(dirs) == list:
        dir_name = dirs[0]
        for dir in dirs[1:]:
            f = file_finder(dir, name)
            if f:
                return dir_name + "/" + f