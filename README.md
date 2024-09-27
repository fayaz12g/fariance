## Visit the website showcase at 
### fayaz.one/fariance

# What is Fariance?
- Fariance is a mod made by Fayaz adding tons of variations to vanilla minecraft items and blocks!

# How to Build

- start by cloning the repo
- open intellij idea and select open project 
- open the fariance folder from the root directory of the repo
- open the terminal from the bottom left and enter "./gradlee genIntellijRuns" and hit enter
- wait for the process to complete and generate important dependencies


    this next part will be essential going forward as the output and resources folders will be excluded in the future .gitignore

from the python folder in the fariance subdirectory, open the base textures subfolder
- run base_main.py
- go up a directory (cd ..)
- run main.py

now everything is ready to build, simply go to intellij and with the project open enter
./gradlew build

it will build under ./build/liba 