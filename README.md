# APParent
A one-stop Django app for parents to communicate with teachers and professionals to keep track of their child's progress.

# Getting Started
Click [here](http://apparent.herokuapp.com/) to access the app.

# Technologies Used
* Django
* Python
* HTML
* Photo Upload via AWS S3
* CSS
* Materialize
* Google Fonts

# ERD
![image](https://i.imgur.com/bm765lt.png)

# Wireframes 
Login Page
![image](https://i.imgur.com/0cNhzY5.png)

Parent Verification Page
![image](https://i.imgur.com/HiCn0WF.png)

Parent Sign Up Form
![image](https://i.imgur.com/sGRjqsf.png)

Non-Parent Sign Up Form
![image](https://i.imgur.com/47litgD.png)

Child Registration Form
![image](https://i.imgur.com/Mvdh3hk.png)

Select a Child Page
![image](https://i.imgur.com/cOn2GSc.png)

Child Summary Page
![image](https://i.imgur.com/ydysIBD.png)

# Pitch Deck
[Click here to access our pitch deck](https://docs.google.com/presentation/d/1WUmGvr7uZbOqYtDaF9uMTxjoTmfDJF2cADpD9a2oUGU/edit#slide=id.gcb9a0b074_1_0)

# Functionality
Coming Soon

## User Authentication
This app utilizes Django's built-in authentication functionality provided by the 'django.contrib.auth' app which is included within the 'INSTALLED APPS' list in 'settings.py'

## Signing up as a Parent
The app requires a user to specify whether you are signing up as a parent or a non-parent.  Signing up as a parent will allow a user to register a child and invite other users to be a part of a child's team, i.e. School Teachers, Speech and Language Pathologists, Occupational Therapists, Physical Therapists, BCBA's, Registered Behavioral Technicians, Paraprofessional Educators.

## Signing up as a Non-Parent
As a non-parent, you can only access a child's record if a parent invites you to be a part of that child's team.  You will receive this invitation via email which will allow you to sign up as a user and access the records associated to the child that you are working with.

## Daily Reports
Each user can log daily reports on the child's progress.  Each report logs who created the report, when the report was created and shows a color coded status that indicates the report progress.

## Goals
Users can also create Goals for each child assigned to them.  Each goal logs who created the goal, a color coded status report and the deadline on when a goal needs to be met.

## Meetings
Users can also create meeting invites for each user.  A user can setup his/her availability and other users can only invite users during those available times.






