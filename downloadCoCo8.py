# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from datasets import load_dataset

dataset = load_dataset("Ultralytics/COCO8")
# 数据会加载到内存，或保存到本地
dataset.save_to_disk("path/to/coco8")
