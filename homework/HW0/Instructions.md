# Homework 0

### Purpose:
The purpose of this assignment is to help you set up your computational environment so you can complete and submit subsequent homework and project assignments.

### Important Assumptions:

1. **Unix**: These instructions will assume that you have access to a `Unix`-friendly computational environment (MacOS, Ubuntu, Redhat, etc.). I will not provide support for non-unix operating systems in this class.  If you would prefer to use a non-Unix operating system (e.g. Windows), I suggest you install a virtual machine to obtain access to a emulated Unix environment, consider using a virtual desktop, or find a way to perform the instructions below within your operating system of choice.
2. **Python**: I assume that you have `Python3` installed on your machine and have basic familiarity with the langugage, including the `pip` package manager.
3. **Git**: I assumethat you have  basic familiarity with `Git`; specifically: `clone`, `add`, `pull`, `commit` and `push`.
4. **Markdown**: I assume basic familiarity with `Markdown`.



### Homework Instructions

##### STEP 1: Subscribe to the Class YouTube Channel:

1. Navigate to the course's [Youtube Channel](https://www.youtube.com/channel/UCYGBs23woNtXUSl6AugHNXw)
2. Click the red Subscribe button on the top right of the page. This should keep you informed when new lecture materials are posted.
3. Go to the playlists section, and note that there is a playlist for Lecture 1. Future playlists for other lectures will be uploaded to the channel as the semester continues.

##### STEP 2: Access and Configure your MSU Gitlab Account:

1. Navigate to [MSU's Gitlab](https://gitlab.msu.edu/)
2. Sign into Gitlab using your MSU `netID` and password. 
3. If you are unable to sign into MSU's Gitlab, please email `ithelp@msu.edu` requesting Gitlab access and and be sure to CC me (`ghassem3@msu.edu`).

##### STEP 3: Access the Course's Gitlab Group:
1. Navigate to the [Course Gitlab Page](https://gitlab.msu.edu/cse842-fall-2020)
2. On the page, you should see two project rows: (1) `Course Materials` and (2) a project with the same name as you `netID`. The `Course Materials` project is where I will store the materials and assignments for the class. The project with the same name as your `netID` is where you will upload your personal assigments for the class.
3. Please make sure that you can access both projects by clicking them. Note that the project with your `netID` should be currently empty.

##### STEP 4: Explore the Course Materials: 
1. Navigate to the [Course Materials Repository](https://gitlab.msu.edu/cse842-fall-2020/course-materials)
2. Note that the repository contains 5 directories and a README.md file, which is displayed automatically on the page.
3. The directories contain raw files for the course: the `homework` directory contains instructions for Homework assignments, the `project` directory contains instructions for the project, and so on. You don't need to investigate these directories unless you want to. I'll provide links to pertinent materials through the course calendar seen in the  `README.md`, as content is uploaded.

##### STEP 5: Pull Course Materials and Your Personal Course Repository 
1. Clone a copy of the course materials to your local machine by running the following command from the Unix terminal: 
    * `git clone https://gitlab.msu.edu/cse842-fall-2020/course-materials.git`
2. Clone a copy of your personal class directory to your local machine by running the following command from the Unix terminal: 
    * `git clone https://gitlab.msu.edu/cse842-fall-2020/<YOUR-NET-ID>.git`
    * Note that the above command assumes you will swap out `<YOUR-NET-ID>` for your actual `netID` value.

##### STEP 6: Initialize your course directory
1. From the command line, copy the `setup.sh` utility to your personal course repository: 
    * `cp course-materials/utilities/setup.sh <YOUR-NET-ID>/.`
2. From the command line, change `setup.sh` script permissions :
    * `cd <YOUR-NET-ID>`
    * `chmod 755 setup.sh`
3. Run the setup script:
    * `./setup.sh`
4. Ensure that the script created the following directories: `Project/`, `Homework`, and `FinalReport`.
5. within your personal course directory, navigate to the submission directory for Homework 0:
    * `cd Homework/HW0/`
6. Ensure that the directory contains a `materials/` subdirectory and an empty file for python library requirements `requirements.txt`. As implied by the name and `requirements.txt` is where you document all `Python` libraries required to run your code, and `materials/` is where you will add supporting scripts, data, and so on that supplement your homework submissions.

##### STEP 7: Install JupyterLab and open Notebook
1. You will be using `jupyterlab` to create your homework and project submissions. To prevent conflicts with any local installations, we will be installing Jupyterlab within a virtual environment (the `setup.sh` script above should have taken care of installing the virtualenvironment package). 
2. To begin, add `jupyterlab` to your `requirements.txt` file:
3. Create, activate and install `requirements.txt` in your virtual environment using the following command:
    * `virtualenv venv; source venv/bin/activate; pip install -r requirements.txt`
4. Open the Jupyterlab application using the following command:
    * `jupyter-lab`
5. Now open your web browser, and visit `http://localhost:8888/lab`. You should see an iPython notebook environment.
6. Under the Notebook pane of the interface, click Python3. This should create and open a new iPython notebook instance called `Untitled.ipynb`.
7. Rename your new notebook instance to `submission.ipynb`

##### STEP 8: Update Your Submission
1. From within `submission.ipynb`, create a new Markdown cell and inlcude (1) the name of the assignment, and (2) your full name.
2. From within `submission.ipynb`, create a Python code cell and include the following lines:
    * `sentence = 'I just completed Homework 0!'; sentence.split()`
3. Be sure to run all cells and save your notebook.

##### STEP 9: Submit Homework 0
1. To submit the assignment, navigate to the main directory of your assignment on the command line and run the following command
2. `git add .; git commit -m 'submitting Homework 0'; git push`
3. You have now submitted Homework 0. 
4. Check your submission online:
    * `https://gitlab.msu.edu/cse842-fall-2020/<YOUR-NET-ID>/-/blob/master/Homework/HW0/submission.ipynb`

##### STEP 10: Practice Replying to Gitlab Issues

1. General announcements in this course, along with Q&A will be performed through Gitlab's Issue's fucntionality. To begin, you will practice how to respond to Gitlab issues.
2. From the [Course Materials Page](https://gitlab.msu.edu/cse842-fall-2020/course-materials), Click the Issues option on the left-side panel.
3. Notice that there is one open issue called `Homework 0: Introduce yourself`. 
4. Click the open issue and respond to the instructions provided in the issue. **Please do not close the issue**.

##### STEP 11: Create and Delete a Gitlab issue

1. From the [Issues Page](https://gitlab.msu.edu/cse842-fall-2020/course-materials/-/issues), create a new issue by clicking the green button in the top-right corner.
2. Provide a Title and Description (choosing a template, if relevant). Be sure to include an appropriate value for the labels  `Labels` field.
3. Edit your issue by clicking the pen icon to the right of the issue's title.
4. Delete your issue by clicking the red delete button.
