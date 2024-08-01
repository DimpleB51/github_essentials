# github_essentials
### Bold face instructions
**Hello** World. Good __morning__

### Italics face instructions
*Hello* World. Good _morning_

### Bullets
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
| Layer         		| Description    	        					|
|:---------------------:|:---------------------------------------------:|
| Input         		| 160x320x3 RGB Image                 	   		|
| Normalization     		| Normalize batch	                            |
| Cropping layer		| 65x320x3
| Convolution 5x5   | 2x2 stride, outputs 31x158x24 	|
| ELU activation		|												|
| Convolution 5x5	  | 2x2 stride, outputs 14x77x36   |
| ELU activation    |                                               |
| Convolution 5x5	  | 2x2 stride, outputs 5x37x48    |
| ELU activation    |                                               |
| Convolution 3x3	  | 1x1 stride, outputs 3x35x64    |

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

### Notes
[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
[Basic syntax](https://www.markdownguide.org/basic-syntax/)
