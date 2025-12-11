import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from ultralytics import YOLO

if __name__ == '__main__':

    # Load a pretrained YOLO11n model
    model = YOLO("yolo11m-seg.pt")

    # Train the model on the COCO8 dataset for 100 epochs
    train_results = model.train(
        data="Custom-seg.yaml",  # Path to dataset configuration file
        epochs=100,  # Number of training epochs
        imgsz=640,  # Image size for training
        # device="cpu",  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
        device=0,  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
        batch=64,  # batchSize
        workers=8,  #
        mosaic=0.0,    # 关闭 Mosaic（4图拼接）
        mixup=0.0,     # 关闭 MixUp（图像混合）
        copy_paste=0.0,# 可选：也关闭 Copy-Paste
        augment=True,           # 必须开启
        auto_augment=None,      # 关闭 randaugment

    # 颜色
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,

    # 几何
    degrees=10.0,
    translate=0.1,
    scale=0.9,              # 强烈推荐！比 0.5 更好
    shear=2.0,
    perspective=0.0,        # 分割任务关闭

    # 翻转
    fliplr=0.5,
    flipud=0.5,

    # 拼接
   # mosaic=0.0,
   # mixup=0.0,              # 少量有益
   # copy_paste=0.0,
    # close_mosaic=0,        # 必须！最后10轮关闭
    )

    # Evaluate the model's performance on the validation set
    metrics = model.val()

    # Perform object detection on an image
    # Predict on an image
    results = model("/hy-tmp/yolo_datasets/images/train/微信图片_20250910133351_3_737_0.jpg")  # Predict on an image
    results[0].show()  # Display results

    # Export the model to ONNX format for deployment
    path = model.export(format="onnx")  # Returns the path to the exported model
