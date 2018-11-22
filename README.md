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

# How to get the project to work?

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
* Create a new directory and store the EyeClient.py, randompic2.jpg and the xml file - all of these 3 items in that directory
* Save the eyeServer.py code on the raspberryPi attached to the robot
* Establish a connection between the RaspberryPi and laptop by connecting them to the same WiFi network
* Now, run the eyeServer.py code on the raspberryPi. It will display a message saying "waiting for sender to recieve data"
* Then go to your laptop, run the eyeClient.py code, with the webcam in front of your eye. A live video window of your eye will appear and it will continuously show the direction in which you are looking (left'right/forward). This data is sent to the raspberry pi and the robot will implement the corresponding command.
