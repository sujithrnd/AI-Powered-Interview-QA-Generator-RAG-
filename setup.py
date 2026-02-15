from setuptools import find_packages, setup
def get_requirements(file_path):
    with open(file_path) as f:
        return f.read().splitlines()
    
setup(
    name = "Generative AI RAG Project",
    version= '0.1.0',
    author= "Sujith K S",
    author_email="ensujithks81@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)