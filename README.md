# naive-bayes-classifier

## 1. Setup environment
  ###  Install virtualenv
```
  sudo apt-get install python3-pip
```

```
  sudo pip3 install virtualenv 
```
  ### Create a virtual environment
```
  virtualenv venv 
```

## 2. Executed program
```
   python naivebayes.py
```

## 3. Dữ liệu sử dụng:
#### Cột đầu tiên chưa giá tiền của trò chơi ($)
#### 29 cột tiếp theo lần lượt thể hiện các tag được gán cho trò chơi tương ứng (1: được gán, 0: không được gán) bao gồm các tag sau:
Indie
Action
Adventure
Casual
Simulation
Singleplayer
Strategy
RPG
2D
Early Access
Free to Play
Puzzle
Atmospheric
Violent
Gore
Multiplayer
Great Soundtrack
Story Rich
Fantasy
Anime
VR
Nudity
Difficult
Pixel Graphics
Sexual Content
Retro
Sci-fi
Funny
Sports

#### Cột cuối cùng thể hiện đánh giá của người dùng về trò chơi đó (0: Mixed, -1: Negative, 1: Positive)

