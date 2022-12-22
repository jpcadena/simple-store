# simple-store

## Simple Store Web app based on Flask Framework and Peewee
Simple store web app to log in, register, add and delete products.

## Tools
Flask is a micro web framework written in Python. It is classified as a
microframework because it does not require particular tools or libraries.[2] It
has no database abstraction layer, form validation, or any other components
where pre-existing third-party libraries provide common functions. However,
Flask supports extensions that can add application features as if they were
implemented in Flask itself. Extensions exist for object-relational mappers,
form validation, upload handling, various open authentication technologies and
several common framework related tools

![Flask Microframework](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1280px-Flask_logo.svg.png)

Peewee is a simple and small ORM. It has few (but expressive) concepts, making
it easy to learn and intuitive to use that supports sqlite, mysql, postgresql
and cockroachdb.

![Peewee ORM](http://docs.peewee-orm.com/en/latest/_images/peewee3-logo.png)

### Requirements

Python 3.10+

### Git

+ First, clone repository:

```
git clone https://github.com/jpcadena/simple-store.git
```

+ Change directory to root project with:

```
  cd simple-store
```

+ Create your git branch with the following:

```
git checkout -b <new_branch>
```

For *<new_branch>* use some convention as following:

```
yourgithubusername
```

Or if some work in progress (WIP) or bug shows up, you can use:

```
yourgithubusername_feature
```

+ Switch to your branch:

```
git checkout <new_branch>
```

+ **Before** you start working on some section, retrieve the latest changes
  with:

```
git pull
```

+ Add your new files and changes:

```
git add .
```

+ Make your commit with a reference message about the fix/changes.

```
git commit -m "Commit message"
```

+ First push for remote branch:

```
git push --set-upstream origin <new_branch>
```

+ Latter pushes:

```
git push origin
```

### Environment

+ Create a **virtual environment** 'sample_venv' with:

```
python3 -m venv sample_venv
```

+ Activate environment in Windows with:

```
.\sample_venv\Scripts\activate
```

+ Or with Unix or Mac:

```
source sample_venv/bin/activate
```

### Installation of libraries and dependencies

```
pip install -r requirements.txt
```

### Execution

```
python main.py
```

### Environment credentials

Rename **sample.env** to **.env** and replace your credentials.

### Documentation

Use docstrings with **reStructuredText** format by adding triple double quotes
**"""** after function definition.\
Add a brief function description, also for the parameters including the return
value and its corresponding data type.

### Additional information

If you want to give more style and a better format to this README.md file,
check documentation
at [Github Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).\
Please use **linting** to check your code quality
following [PEP 8](https://peps.python.org/pep-0008/). Check documentation
for [Visual Studio Code](https://code.visualstudio.com/docs/python/linting#_run-linting)
or
for [Jetbrains Pycharm](https://github.com/leinardi/pylint-pycharm/blob/master/README.md).\
Recommended plugin for
autocompletion: [Tabnine](https://www.tabnine.com/install)
