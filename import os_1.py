import os
from ppdet.core.workspace import load_config

# 打印默认配置路径
print(os.path.abspath('configs'))

# 验证配置文件加载
cfg = load_config('configs/ppyoloe/_base_/optimizer_300e.yml')
print(f"配置文件路径：{cfg['__file__']}")