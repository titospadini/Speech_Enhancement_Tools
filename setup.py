#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='Speech_Enhancement_Evaluation_Metrics ',
    version=1.0,
    description='计算语音增强相关的评价指标，计算结果会被保存为 Excel 表格',
    author='haoxiang',
    author_email='haoxiangsnr@gmail.com',
    maintainer='haoxiang',
    maintainer_email='haoxiangsnr@gmail.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/haoxiangsnr/Speech_Enhancement_Evaluation_Metrics.git',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: Linux',
        'Intended Audience :: Developers',
        'License :: Linux :: MIT License',
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
