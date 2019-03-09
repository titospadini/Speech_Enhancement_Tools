# Speech Enhancement Evaluation Metrics

A flexible and  compact framework for calculating speech enhancement evaluation metrics.

## Usage


```shell
Speech_Enhancement_Evaluation_Metrics

optional arguments:
  -h, --help            show this help message and exit
  -n NOSIY_DIR, --nosiy_dir NOSIY_DIR
  -dn DENOSIY_DIR, --denosiy_dir DENOSIY_DIR
  -c CLEAN_DIR, --clean_dir CLEAN_DIR
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        必须以 xls 的拓展名结尾
  -l LIMIT, --limit LIMIT
                        默认为0，表示不限制数量
  --offset OFFSET       默认为0，表示无偏移
  --sr SR               采样率

e.g. python main.py -n /media/imucs/DataDisk/haoxiang/Release/speech_enhancement/release_-5_0_30_50/test/noisy/ -dn ../se_-5_0_30_50_VCC/output/ -c /media/imucs/DataDisk/haoxiang/Release/speech_enhancement/release_-5_0_30_50/test/clean
```

## ToDo

- [x] 实现测试 stoi 和 metric 的评价功能
- [x] 生成表格