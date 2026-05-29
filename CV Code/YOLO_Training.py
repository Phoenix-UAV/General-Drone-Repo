from ultralytics import YOLO


def main():
    model = YOLO("yolo26n.pt")
    dataset_yaml = ""  # Location of YAML
    batch_size = -1
    device = 0
    imgsz = 640
    epochs = 100

    results = model.train(
        data=dataset_yaml,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch_size,
        device=device,
        workers=8,
        plots=True,
        cache=True,
        rect=True,
    )

    print("Training Done")


if __name__ == "__main__":
    main()
