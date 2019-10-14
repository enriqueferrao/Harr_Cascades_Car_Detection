# ***README***

* This repository has the code along with all the needed files to perform detection of cars in an image or video.
* The explaination of how harr cascades works is available in the file called Working_of_Harr_Cascades.odt
* The Harr Cascades Classifier is trained on a dataset consisting of around 2000 positive images and 5800 negative images.
* The dataset of the positive and negative images is provided in the repository folder cars_dataset and negatives respectively.
* The dataset was downloaded from the following links:-
  
  [Link1](http://lars.mec.ua.pt/public/Media/ResearchDevelopmentProjects/HaarFeatures_RoadFilms/HaarFeaturesTests/CarsRear/Caltech/PNGImages/cars/)

  [Link2](https://www.kaggle.com/prasunroy/natural-images)
  
* The trained cascade.xml file is available in the folder called data.
* If you wish to train the classifier on your own, I have made a file called harr_cascades_training.odt with the required terminal commands to perform the training.
* The video on which I have performed the car detection was downloaded from the following [Link](https://www.youtube.com/watch?v=wqctLW0Hb_0)
* If the code doesn't perform the detection well, play around with the values of the parameters in the car_cascade.detectMultiScale() function in the car_detection.py code.