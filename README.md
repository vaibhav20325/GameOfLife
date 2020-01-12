# Conway's Game Of Life
School Project
By-Vaibhav Agarwal

Make sure to have the pygame library installed on the system.

### Installation
In order to install pygame, use pip in Command Prompt.
```
py -m pip install -U pygame --user
```

Ensure that you have the images in the same folder.

**The design folder has all the designs,you can create your own deisgn by creating a .txt file in the design folder or copy one from <http://www.radicaleye.com/lifepage/glossary.html>**

At the heart of this game are four rules that determine if a cell is live or dead. All depend on how many of that cell's neighbors are alive.

* Births: Each dead cell adjacent to exactly three live neighbors will become live in the next generation.
* Death by isolation: Each live cell with one or fewer live neighbors will die in the next generation.
* Death by overcrowding: Each live cell with four or more live neighbors will die in the next generation.
* Survival: Each live cell with either two or three live neighbors will remain alive for the next generation.

Another important fact about the rules for the game of life is that all rules apply to all cells at the same time.

After clicking on some boxes to make the intial setup, Press ENTER to Start.

To increase the frame rate Press <kbd>→</kbd>
To decrease the frame rate Press <kbd>←</kbd>
Press <kbd>UP</kbd> to set the frame rate to 30

To reset the initial position Press <kbd>Esc</kbd>

**Press <kbd>c</kbd> to change colour**

**Press <kbd>q</kbd> on the first page to enable infinite grid**

