import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from ultralytics import YOLO

if __name__ == '__main__':

    # Load a pretrained YOLO11n model
    model = YOLO("/hy-tmp/ultralytics/runs/segment/train19/weights/best.pt")

    # Train the model on the COCO8 dataset for 100 epochs
    #train_results = model.train(
    #    data="Custom-seg.yaml",  # Path to dataset configuration file
     #   epochs=100,  # Number of training epochs
      #  imgsz=640,  # Image size for training
        # device="cpu",  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
       # device=0,  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
        #batch=64,  # batchSize
        #workers=8,  #
    #)

    # Evaluate the model's performance on the validation set
    metrics = model.val()

    # Perform object detection on an image
    # Predict on an image
    results = model("/hy-tmp/yolo_datasets/images/train/微信图片_20250910133351_3_737_0.jpg")  # Predict on an image
    results[0].show()  # Display results

    # Export the model to ONNX format for deployment
    path = model.export(format="onnx")  # Returns the path to the exported model
