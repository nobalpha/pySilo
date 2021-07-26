class File:
    def __init__(self, *, id, size, cpath, npath, extension, name):
        self.id = id
        self.size = size
        self.cpath = cpath
        self.npath = npath
        self.extension = extension
        self.name = name

    def update_path(self, npath):
        pass
