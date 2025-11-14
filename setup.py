from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='gnanesh',
    author_email='gnanesreddy1603@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF-2"],
    packages=find_packages()
)