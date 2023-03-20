# Knowledge-Kiosk
## Introduction
This application is basically empowered by OpenAI API and can be customized based on your need. It can anwer any question and play the role of assistance. 


## :ledger: Index

- [About](#beginner-about)
- [Usage](#zap-usage)
  - [Installation](#electric_plug-installation)
  - [File Structure](#file_folder-file-structure)
- [Gallery](#camera-gallery)


##  :beginner: About
Lonowledge-Kiosk is a fancy name that is choosen for this application just for fun. It is developed using Python on the backend and Vue 3 on the frontend. The information are being exchanged with the help of Socket.io. OpenAI API makes the application powerfull enough to answer any question. Because Python is used on the backend, any good idea of text manipulation can be implemented in the future.

### Watch the demo video of the application here
![Demo video of the pplication](https://user-images.githubusercontent.com/115637390/226401890-500e0a6e-f61f-4e5d-ae79-65dc38abbafa.mp4)

## :zap: Usage
If you want to use this project, you should install the dependencies of Python and Vue.js. Furthermore a key for the OpenAI API must be generated and saved in the key text file on the backend. 

###  :electric_plug: Installation
- For the frontend you need to install Vue.js, Tailwind and Socket.io client. 
```
$ npm install 
```
- For the backend you need to install OpenAI API, Flask and Scoket.io
```
$ pip install -r requirements.txt
```


###  :file_folder: File Structure


```
Project
├── Knowledge-Kiosk
│   ├── Backend
│   │   ├── env folder
│   │   └── App.py
│   │   └── key.txt
│   │   └── requirements.txt
│   ├── Frontend
│   │   ├── node_modules
│   │   ├── public
│   │   ├── srce
│   │   │   ├── assets
│   │   │   │   ├── logo.png
│   │   │   │   ├── profile.png
│   │   │   │   ├── search.png
│   │   │   └── components
│   │   │   │   ├── aboutApp.vue
│   │   │   │   ├── askSomething.vue
│   │   │   │   ├── footerComp.vue
│   │   │   │   ├── loadingComp.vue
│   │   │   │   ├── mottoComp.vue
│   │   │   │   ├── navComp.vue
│   │   │   └── utils
│   │   │   │   ├── nextElementList.js
│   │   ├── App.vue
│   │   └── index.css
│   │   └── main.js
│   └── -
│       ├── jsconfig.json
│       └── package.json
│       ├── tailwind.config.js
│       └── vue.config.js
├── README.md

```

##  :camera: Gallery
### Main Page
<img src="https://user-images.githubusercontent.com/115637390/226377768-d0a9523f-0198-4142-9de0-0bafa4413b22.png" />

<img src="https://user-images.githubusercontent.com/115637390/226379168-73334156-2206-4286-9db1-aaadc0d98949.png" />
