# Lab : hello-class

## Step 1
Crete a python script named **hello-class.py** that prints the following output.

```bash
My Name is: <your_name>.
My Major is: <your_major>.
I attend: <your_college>.
My python version is: <your_python_version>.
It is nice to meet everyone.
```

Replace your name, major, and college with your personal information. Use python's sys module to get the version information.

## Step 2
## Step 6
Follow the instructions in the README.md within the hello-class branch.
```yaml
language: python
python:
  - 3.6
install:
  - pip install -r requirements.txt
branches:
  only:
    - hello-class
script:
  - pytest
```

## Step 3
Push your code to GitHub.

```bash
git add .
git commit -m "hello-class lab complete"
git push
```

## Step 4
Copy your GitHub URL and TravisCI URL and submit them to the related assignment in your universities learning management system (e.g. Canvas, BlackBoard, Desire2Learn, etc.).

* Link 1 - Your GitHub URL e.g. <https://github.com/drk-data-science/hello-class>
* Link 2 - Your TravisCI URL e.g. <https://travis-ci.org/drk-data-science/hello-class>