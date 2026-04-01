from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="medical_rag",
    version="0.1.0",
    author="S.dahiya",
    description="A medical retrieval-augmented generation (RAG) system for question answering.",
    packages=find_packages(),
    install_requires=requirements,
)