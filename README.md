# WebSocketRace

A tool for exploiting race condition type vulnerabilities with websockets. 

Some applications have switched from using HTTP as the primary protocol for interacting with data to using the Websockets protocol. However, many race conditions still remain to be found, which is why I created this tool. It can be used to simultanously send 2 websocket requests to an endpoint and break the state-machine of an application.