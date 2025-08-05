# Edit this program by defining a child class of Folder called CertificateFolder
# - Give it a constructor which declares an instance variable for the list of certificates in the folder (starts empty)
# - Override open() and output all the files in the list of files
# - Override add_file() and add the parameter file to the list of files
# Instantiate a CertificateFolder object and call its add_file() and open() functions to test
from abc import ABC, abstractmethod


class Folder(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def add_file(self, file_name: str):
        pass
