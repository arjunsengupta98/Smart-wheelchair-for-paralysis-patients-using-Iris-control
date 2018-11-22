# Iris Controlled Smart Wheelchair for paralysis patients

## The main idea
I have created a robot that can be wirelessly controlled simply through eye movement. This robot serves as a prototype for a wheelchair that can be made for paralysis patients. 
All that is required is a small camera to be attached near the eye. Paralysis patients are capable only of eye movement. Hence they can move their wheelchair through eye movement only. My robot demonstrates a small scale prototype of this wheelchair. 
I am also adding an obstacle avoidance feature for emergency braking, in case an obstacle arrives.

## Current stage of the project
Currently, the robot is capable of detecting only left, right and forward commands by the eye. I have created my own algorithm for left right and centre detection of the Iris and it is a rather weak algorithm at the current stage. I am working on further refining it to make the algorithm stronger. OpneCV in python has been used for digital image processing to detect Iris commands. The code uploaded currently enables the robot to function in the following ways:
* Look straight to continuously move forward
* Look right to turn right
* Look left to turn left

As you have noticed, the code that I have currently uploaded is in a very rough and preliminary stage. I am currently working on a code that will have considerable improvements:
* Better accuracy for left and right detection
* Feature to detect blinks and stop movement of bot on double blinking
* Feature to activate and deactivate Iris control by a combination of blinks
* Feature for obstacle avoidance in case of emergency braking due to sudden appearance of obstacle

## How to get the project to work?

Hardware plays an essential role in the project. First of all, gather the components:
* Raspberry Pi 3b 
*	L293D Motor Driver 
*	Breadboard 
*	Jumper wires 
*	Wifi Hotspot for wireless data transfer
*	Chassis 
*	DC motors 
*	Battery/Power bank for power source
*	Laptop + webcam for Digital Image Processing

I wont't go much into hardware assembly of the robot. You need to make a normal 2 wheel driven robot using the Raspberry Pi. The internet is flooded with numerous tutorials for this purpose.
Diving into the software, you need to perform the following steps:
* Install openCV for python on your laptop
* Create a new folder and give it any name such as Smart_Wheelchair. Store the following 3 files in the Smart_Wheelchair folder:
1) EyeClient.py 
2) randompic2.jpg  
3) parojosG.xml 
* Access the OS of the raspberryPi (that is fixed on the robot) either through remote desktop applications such as VNCViewer, or directly view the OS through a separate computer monitor using HDMI output.
* Save the eyeServer.py code in the Desktop directory of the raspberryPi (or any other convenient directory on the Raspberry Pi)
* Establish a connection between the RaspberryPi and laptop by connecting them to the same WiFi network
* Now, run the eyeServer.py code on the raspberryPi. It will display a message saying "waiting for sender to recieve data"
* Next, on your laptop, run the EyeClient.py code, with the webcam in front of your eye. A live video window of your eye will appear where the processing is being done and there will be an output on the screen which shall continuously show the direction in which you are looking (left/right/forward). This data is sent to the raspberry pi and the robot will implement the corresponding command by movement combinations of wheels.

If you are familiar with basic image processing on OpenCV, you will easily be able to understand the algorithm that I have created by extrapolating from the EyeClient.py code itself. I have used a 'haarcascade' of an eye, thereby identifying the eye in the live video window being recorded, and done processing on that part of the image (applying my algorithm only to the right eye). Live video feed of the Iris was taken as input, and the entire frame was converted to grayscale. Then I performed binary thresholding so that the Iris turns completely black and the surrounding area is completely white. Now I fixed 3 points on the frame- left, centre and right. If the person is looking left, then the left point is identified as black. The same thing happens for the case of left and right. This code shall be written in the client side (Data sender). This data(direction) shall be sent wirelessly to the Raspberry pi. As you can see, a bit of socket programming has also been used in this project. The upcomming versions of the codes shall import various other python libraries such as dlib etc. which you will need to download before running the code. But for now, these simple procedures shall work.

Stay tuned for the improved, upcomming version of code. Meanwhile, try running these on an actual robot. Play around and have some fun with code!
Any positive contributions to the codes/ suggestions for the project would be much appreciated.
Cheers!
