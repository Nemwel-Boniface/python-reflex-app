# Welcome to Reflex!
# Python Reflex App

This repository outlines the steps to create a basic app using the Reflex framework. [Reflex](https://reflex.dev/) is a library to build full-stack web apps in pure Python. Reflex packs around the following key features:

1. Built your applications using pure Python - Write your app's frontend and backend all in Python, no need to learn Javascript.
2. Reflex offers full Flexibility - Reflex is easy to get started with, but can also scale to complex apps.
3. Reflex allows you to easily deploy your applications Instantly - After building, deploy your app with a [single command](https://reflex.dev/docs/hosting/deploy-quick-start/) or host it on your own server.

## Description

This project is a simple web application built with Reflex, a Python library. The app displays a "Hello World!" message and includes a button that, when clicked, fetches details about cat facts from a specified URL and displays the content.

## Installation

To get started with this project, follow these steps:
### Prerequisites
1. Make sure that you have Python installed on your local machine. Check your version using ```python3 --version```. If you do not receive your Python Version, please install Python for your respective operating system.
2. You now need to install Reflex using ```pip install reflex```. If you do not have "pip' installed you will have to install it by running ```sudo apt install python3-pip```

![installpythonandpip](https://github.com/Nemwel-Boniface/bookstore_api/assets/86318284/b33dc101-867f-43c9-bf11-3fe47a278db2)

**For the prerequisites you are now set to start :rocket:**

### Setup the project locally
1. Clone the repository:
    ```bash
    git@github.com:Nemwel-Boniface/python-reflex-app.git
    cd python-reflex-app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install reflex requests
    ```
4. Initialize your reflex application by running this cmd
```
reflex init
```
5. Once that completes, you can run the application with the below command. If successful, your application can be found here: ```http://localhost:3000/```
```
reflex run
```

**If you were successful above, you will see the following result in the browser when you open it:**

[Screencast from 29-05-2024 07:40:13 ASUBUHI.webm](https://github.com/Nemwel-Boniface/bookstore_api/assets/86318284/0429c925-a964-4916-9956-def2fd545a45)


## Configuration

The app is configured using a `Config` object from Reflex:

```python
config = rx.Config(
    app_name="reflex_dev",
)
```

# Project deployment
Reflex offers an easy way to deploy your applications which can be checked out from their main docs [here](https://reflex.dev/docs/hosting/deploy-quick-start/). I was able to deploy my own project and if you are interested in having a look at it online, please do so from this URL ```https://python-reflex-app.reflex.run/```


**If you would like to have a better view of each individual feature implemented, please visit the [Pull Requests page](https://github.com/Nemwel-Boniface/python-reflex-app/pulls) and have a look at the closed PRs where you will be able to see what was changed at what specific point in time.**


## Authors

👤 **Nemwel Boniface**

- GitHub: [@Nemwel Boniface](https://github.com/Nemwel-Boniface)
- Twitter: [@Nemwel Boniface](https://twitter.com/nemwel_bonie)
- LinkedIn: [@Nemwel Bonifacej](https://www.linkedin.com/in/nemwel-nyandoro/)


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/Nemwel-Boniface/python-reflex-app/issues).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments
- To God be the Glory :pray: 
- Me for believing that I can! :sunglasses: 

## 📝 License

This project is [MIT](./MIT.md) licensed.