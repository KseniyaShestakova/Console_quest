# Quest
A small console quest. It makes you able to create a console quest with your own scenario writing file with the format similar to the ones presented in parameters_study.txt/ rules_parameters.txt (file with parameter description) and study_quest.txt / rules_quest.txt (file with the description of positions) 


To run the quest:
```
git clone git@github.com:KseniyaShestakova/Console_quest.git
cd Console_quest/
git checkout checkpoint_3
python3 main.py parameters_study.txt study_quest.txt
```
(for playing a quest about MIPT life)
or 
```
cd Console_quest/
git checkout checkpoint_3
python3 main.py parameters_again.txt nodes_again.txt
```
(for playing a quest with rules explanation)
or
```
cd Console_quest/
git checkout checkpoint_3
python3 main.py <my_parameters> <my_position>
```
(if you have your own file with parameters and positions)

### Installing necessary libraries:
Make sure you have installed python libraries, which are necessary for running this quest!
They are 'keyboard','termcolor','random', 'os' and 'sys'
```
apt install python3 python3-pip
apt install python3-termcolor
pip3 install keyboard
pip3 install random
pip install os-sys
```
Note: if you write 'sudo' before installing one of this libraries you should execute the project with 'sudo' also:
```
sudo python3 main.py <parameters> <position>
```
### Something about playing the quest
Before playing the game you should choose either keyboard model or input one.  
You can choose the right option in this quest pressing Ctrl and confirm your choice pressing Enter in keyboard model.
You can choose the right option in this quest printing the number of the option ( 1 ... <amount_of_options>) in input model.
During the quest you will be asked to play the game '2048' (adding this part of game into your quest is made with keywords 'game' and 'score' in the scenario)
For moving the table 2048 input the next keys: "a" - left, "w" - up, "d" - right, "s" - down.
