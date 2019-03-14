#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='SPEMM',
    version='1.1.9',
    description='TEST DEMO',
    author='haoxiang',
    author_email='haoxiangsnr@gmail.com',
    maintainer='haoxiang',
    maintainer_email='haoxiangsnr@gmail.com',
    long_description=long_description,
    license='MIT',
    packages=['SPEMM'],
    entry_points={
        'console_scripts':[
            'SPEMM=SPEMM:cal'
        ]
    },
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
        # 'pystoi',
        # 'tqdm',
        # 'librosa',
        # 'tablib',
    ]
)
