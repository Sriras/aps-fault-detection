from setuptools import find_packages, setup
from typing import List


class Get_Requirements(object):

    def __init__(self,requirement_file_name,removal_string):

        self.req_file:str = requirement_file_name
        self.removal_str:str = removal_string

    
    def get_requirments(self)->List[str]:

        with open(self.req_file) as requirement_file:
            list_of_req_pakages = [pkgs.replace("/n","") for pkgs in requirement_file.readlines()]
            if self.removal_str in list_of_req_pakages:
                list_of_req_pakages.remove(self.removal_str)
            return list_of_req_pakages





if __name__ == "__main__":
    
    setup(
        
        name='sensor',
        version='0.0.1',
        author='sahas',
        author_email='shsrnmn23@gmail.com',
        packages=find_packages(),
        requires=Get_Requirements("requirements.txt","-e .")        
    )
