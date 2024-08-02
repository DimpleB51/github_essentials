# github_essentials
### Bold face instructions
**Hello** World. Good __morning__

### Italics face instructions
*Hello* World. Good _morning_

### Bullets
Start(`*`) vs Dash(`-`)
* This is first bullet.
* This is second bullet.
* This is third bullet.

vs 

- This is first bullet.
- This is second bullet.
- This is third bullet.
  
### Adding comments in github
<!---MARKDOWN CHEATSHEET - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet--->

### Linking papers or websites to the file
 NVIDIA's [End to End Learning for Self-Driving Cars](https://arxiv.org/pdf/1604.07316v1) paper.
### Adding images to the file 
![img](./images/Tweety.svg)

### Adding Youtube/Drive etc links to the file
|Lane line detection|
|:------------:|
|[Youtube Link](https://youtu.be/1WB2iHLmNtk)|

### Adding video links to the file along with gif
|Solid White Right|
|:------------:|
|![Solid White Right](./images/solidWhiteRight.gif) |
|[Youtube Link](https://youtu.be/1WB2iHLmNtk)|

### Adding tables to the files
| Layer         		| Description    	        					|addd|
|:---------------------:|:---------------------------------------------:|:---------------------------------------------:|
| Input         		| 160x320x3 RGB Image                 	   		|a|
| Normalization     		| Normalize batch	                            |b|

### Adding coding instructions to the files
##### Single line instructions
In terminal 1 run,
`python3 main.py`

##### Multiple line instructions
```
Terminal 1: bash sim_lidar.sh
Terminal 2: rosrun e2es off_mode
Terminal 3: rosrun e2es main.py
```
### Style
**Paras**
<p/>
Following writeup is an accompaniment to the submitted project 4 of Udacity's Self-Driving nanodegree program. In this project our goal is to train a network using Keras which can successfully emulate human driving behavior autonomously in a simulated enviornment. We had an option to generate data using the simulator or use Udacity's sample dataset. I initially tried generating the data however I wasn't able to navigate through the simulation enviornment properly as I would mostly drive off the roads. Hence I chose to proceed with the dataset provided by Udacity. Following the Udacity lectures I built the CNN based on NVIDIA's End to End Learning for Self-Driving Cars paper. To avoid overfitting I have added a dropout layer after the first fully connected layer. The training and testing was done in Udacity' workspace.<p/>

vs **Justified text** 

<p align="justify"> Following writeup is an accompaniment to the submitted project 4 of Udacity's Self-Driving nanodegree program. In this project our goal is to train a network using Keras which can successfully emulate human driving behavior autonomously in a simulated enviornment. We had an option to generate data using the simulator or use Udacity's sample dataset. <br/>I initially tried generating the data however I wasn't able to navigate through the simulation enviornment properly as I would mostly drive off the roads. Hence I chose to proceed with the dataset provided by Udacity. Following the Udacity lectures I built the CNN based on NVIDIA's End to End Learning for Self-Driving Cars paper. To avoid overfitting I have added a dropout layer after the first fully connected layer. The training and testing was done in Udacity' workspace. </p>

### Notes
[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) <br/>
[Basic syntax](https://www.markdownguide.org/basic-syntax/)
