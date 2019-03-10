#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='SPEEM ',
    version='1.0.0'
    description='Calculate the evaluation indicators about speech enhancement and saved as an Excel',
    author='haoxiang',
    author_email='haoxiangsnr@gmail.com',
    maintainer='haoxiang',
    maintainer_email='haoxiangsnr@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=False,
    zip_safe=True,
    platforms=["all"],
    url='https://github.com/haoxiangsnr/Speech_Enhancement_Evaluation_Metrics.git',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'pesq',
        'stoi',
        'tqdm',
        'lxml',
        'librosa',
        'tablib',
    ]
)
