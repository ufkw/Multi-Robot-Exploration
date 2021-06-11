# Multi-Robot-Exploration

This project is an implementation of the algorithm outlined by Martijn N. Rooker and Andreas Birk in their paper "[Multi Robot Exploration Under the Constraints of Wireless Networking](http://robotics.jacobs-university.de/sites/default/files/publicationPDFs/CEP07-CommExplore-RookerBirk.pdf)." 

I tested my project in two different obstacle environments, as well as an environment with no obstacles. Each environment was tested with three, four, or five robots. I performed ten trials for each of these cases. I also ran three, four, and five robots on a blank 50 x 50 environment without obstacles. By looking at the data, Environment 2 was explored quicker than Environment 3 on average. On average, exploring Environment 2 took around twice as long as exploring the blank environment while exploring Environment 3 took between two to three times as long. 

## Exploring Environment 1
Environment 1 has no obstacles.
![Screenshot (53)](https://user-images.githubusercontent.com/42676735/121716574-2ba0a280-caae-11eb-8a07-834812899e7b.png)
![Screenshot (54)](https://user-images.githubusercontent.com/42676735/121716580-2e02fc80-caae-11eb-8f8b-cf36e005b030.png)
![Screenshot (56)](https://user-images.githubusercontent.com/42676735/121716592-2fccc000-caae-11eb-8ba9-9a0dca0f0606.png)
![Screenshot (57)](https://user-images.githubusercontent.com/42676735/121716597-31968380-caae-11eb-949e-d9c9e90a540b.png)


## Exploring Environment 2
![image](https://user-images.githubusercontent.com/42676735/121716084-9ef5e480-caad-11eb-9149-74733b864632.png)
![image](https://user-images.githubusercontent.com/42676735/121716103-a1583e80-caad-11eb-8957-7abfe6828a56.png)
![image](https://user-images.githubusercontent.com/42676735/121716112-a4532f00-caad-11eb-83e2-11be7056144b.png)

The robots can successfully navigate around these obstacles and across a large space of explored cells to the nearest blue (frontier) cells.

![image](https://user-images.githubusercontent.com/42676735/121716147-b0d78780-caad-11eb-9f6a-9c15c3ddca4a.png)
![image](https://user-images.githubusercontent.com/42676735/121716155-b3d27800-caad-11eb-8581-55ff48eb4d59.png)

### Results for Environment 2
My algorithm searches in steps, so I recorded how long the exploration took as in steps in the algorithm as well as in seconds. 
![image](https://user-images.githubusercontent.com/42676735/121715784-46bee280-caad-11eb-9d2d-a5970a027c3a.png)
![image](https://user-images.githubusercontent.com/42676735/121715804-4aeb0000-caad-11eb-8f20-9ec9ad23ca23.png)

By looking at the exploration of Environment 2, no conclusions can be drawn about if increasing the number of robots affects the efficiency of the algorithm. However, more robots did make the environment take more physical time to explore. I assume this is because I calculated the distance between each robot and the nearest frontier using brute force. This inefficiency is clearly represented. In future work on this project I will implement a more efficient algorithm for checking the nearest frontier.

## Exploring Environment 3
![image](https://user-images.githubusercontent.com/42676735/121716286-d795be00-caad-11eb-8f4d-8a7f70c8450f.png)
![image](https://user-images.githubusercontent.com/42676735/121716295-d95f8180-caad-11eb-9797-4fed642ef5fa.png)
![image](https://user-images.githubusercontent.com/42676735/121716300-dc5a7200-caad-11eb-9cb4-4701e5d7c18c.png)
![image](https://user-images.githubusercontent.com/42676735/121716323-e11f2600-caad-11eb-80a1-c800964a8c9d.png)
![image](https://user-images.githubusercontent.com/42676735/121716336-e54b4380-caad-11eb-8852-b5f542a0bea0.png)
![image](https://user-images.githubusercontent.com/42676735/121716345-e8deca80-caad-11eb-9285-99db1a29b837.png)

### Results for Environment 3
In the more complex Environment 3, having more robots did affect how many time steps it had to step through the grid. Looking at the graph it seems that having more robots did help. 

![image](https://user-images.githubusercontent.com/42676735/121716013-884f8d80-caad-11eb-9150-65114655dc4e.png)
![image](https://user-images.githubusercontent.com/42676735/121716020-8ab1e780-caad-11eb-854d-1e45e13e625d.png)
