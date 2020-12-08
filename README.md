# 🖼Image_Classifier
A template for any image classification problem with [Teachable Machine](https://teachablemachine.withgoogle.com/) and its real-time detection with OpenCV in Python.
I have written a blog post about this work and you can find it [here](https://harikrishnan6336.medium.com/multi-class-image-classification-in-teachable-machine-and-its-real-time-detection-with-opencv-282a1409006f)

Start an image project in Teachable machine and export the Tensorflow model and then extract the downloaded folder and place the "keras_model.h5" and "labels.txt" in the working directory. 

For more awesome Teachable Machine resources visit [The Awesome Teachable Machine List](https://github.com/SashiDo/awesome-teachable-machine)

### 👨🏻‍🏫  Prerequisites

To install all the dependencies, run:

``` pip install --user -r requirements.txt ```


### 🔧 How to Use

1.👯 Clone the Repository:
```sh
$ git clone https://github.com/Harikrishnan6336/Image_Classifier.git
```

2. Then move to the working directory.
```sh
$ cd Image_Classifier
```

2. Place the "keras_model.h5" and "labels.txt" in the working directory and replace the `"Label : " + labels[str(result)]` with the label name.
.

3. Setup the game by providing images of Rock paper scissors and Nothing in the order while the program captures it when executing the command below
```sh
$ python3 setup.py 
```

4. Run the program
```sh
$ python3 main.py
```

## Built With ❤️ 

* [Python3.6](https://docs.python.org/3.6/) - ⚠️️ Warning : Tensorflow is not supported on any version of python above 3.6 as of now.
* [Teachable Machine](https://teachablemachine.withgoogle.com/) - An easy tool to create machine learning models for your use without any coding.
* [OpenCV4](https://opencv.org/) - A library of programming functions mainly used for real-time computer vision

## 💁🏻 Contributing


Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. 🍴 Fork the Project
2. Create your Feature Branch (`git checkout -b feature/newFeature`)
3. Commit your Changes (`git commit -m 'Add some newFeature'`)
4. Push to the Branch (`git push origin feature/newFeature`)
5. Open a Pull Request

Please feel free to raise any issue...
