# WebSocketRace

A tool for exploiting race condition type vulnerabilities with websockets. 

Some applications have switched from using HTTP as the primary protocol for interacting with data to using the Websockets protocol. However, many race conditions still remain to be found, which is why I created this tool. It can be used to simultanously send 2 websocket requests to an endpoint and break the state-machine of an application.

## Installation

To install run the following:

```bash
git clone https://github.com/jakubjn/WebSocketRace.git
pip install -r requirements.txt
```

## Usage

To Run:

```bash
python3 WebSocketRace.py -gate 'GATE' -r
```

To Set First Request:

```bash
python3 WebSocketRace.py -gate 'GATE' -data_one "REQUEST"
```

To Set Second Request:

```bash
python3 WebSocketRace.py -gate 'GATE' -data_two "REQUEST"
```

To Set Origin Url:

```bash
python3 WebSocketRace.py -gate 'GATE' -o "URL"
```

To Set Connection Request:

```bash
python3 WebSocketRace.py -gate 'GATE' -c "REQUEST"
```

To Set Cookies:

```bash
python3 WebSocketRace.py -gate 'GATE' -b "COOKIES"
```

To Set Variables:

```bash
python3 WebSocketRace.py -gate 'GATE' -v "NAME:VALUE NAME:VALUE"
```
