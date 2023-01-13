# chatgpt-python-gui

### Super simple Chat-GPT-GUI

#### Needed Python Module:
```
pip3 install openai
```
#### Generate API-Key:
```
https://beta.openai.com/account/api-keys
```
#### Command:
```
python3 chat_gpt.py
```

![GUI](https://github.com/actionschnitzel/chatgpt-python-gui/blob/main/py_chat.png)

### Linux Integraton:    
    
Go to:
```
/home/USER/.local/bin
```
Create File "chat-gpt" with:
```
#!/usr/bin/bash    
cd /[PATH TO FILE]/chatgpt-python-gui    
python3 chat_gpt.py
```
Make File Executeble:
```
chmod +x /home/USER/.local/bin/chat-gpt
```
In Terminal App can be started via "chat-gpt"
