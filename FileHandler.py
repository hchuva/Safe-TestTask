import os

# File Handlers define how we read and write files. This means we can either manage files using our file system, or we can manage files using a database.

class FileSystemHandler:

    @staticmethod
    def SaveFile(path: str, file: str, data: str, overwrite: bool = False):
        mode = "w" if overwrite else "a"
        with open(path + '/' + file, mode) as file:
            file.write(data)

    @staticmethod
    def ReadFile(path: str) -> str:
        fileData = ""
        fileSize = 0
        with open(path, "r") as file:
            fileData = file.read()
            fileSize = len(fileData)
        return fileData, fileSize
    
    @staticmethod
    def DeleteFile(path: str):
        os.remove(path)

    @staticmethod
    def CreateFile(path: str, file: str, data: str = ""):
        os.makedirs(path, exist_ok=True)
        with open(path + '/' + file, "w") as file:
            file.write(data)

    @staticmethod
    def GetFileSize(path: str):
        return os.path.getsize(path)
    
    @staticmethod
    def DeleteDirectory(path: str):
        os.rmdir(path)

    @staticmethod
    def GetEmptyDirectories(path: str) -> list:
        emptyDirList = []
        for dirpath, _, _ in os.walk(path):
            if len(os.listdir(dirpath)) == 0:
                emptyDirList.append(dirpath)
        return emptyDirList
    
    @staticmethod
    def Walk(path: str) -> dict:
        fileList = {}
        for dirpath, _, filenames in os.walk(path):
            for file_name in filenames:
                fileList[dirpath.replace(path, "") + "/" + file_name] = {
                    "path": dirpath.replace(path, ""),
                    "file": file_name
                }
        
        return fileList
