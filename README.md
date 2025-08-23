# CampusLink_WebMobileApp


Project Title: CampusLink Web App

Project Description

CampusLink is a web application designed to serve as a centralized hub for university students. The application aims to simplify a student’s academic and social life by providing a single, portable platform to manage tasks, discover events/activities through a community bulletin board, and access critical emergency contacts, accessible from any device, anywhere.

Key Features

	User Authentication & Account Management: A secure system to create unique accounts, log in, and log out and a space for displaying user information and managing sessions

	Task Schedule Manager: A user friendly interface to add, view, and edit a schedule of personal tasks & bulletin events/activities.

 	Bulletin Board: A dedicated section for Browse and posting announcements relevant to the campus community, including news, queries, and student led activities/initiatives, designed for easy readability and posting on the go.
	
 	Emergency Contacts: A quick access panel with one click buttons to contact essential campus services like security, health, and counseling.


Development Methodology

This project is being developed using an agile methodology with an emphasis on iterative development, continuous feedback, testing, and collaboration through version control.


Basic Usage Instructions

To get a local copy of this project up and running on your machine, follow these simple steps.

Prerequisites 

	Python 3.x installed on your system
	
	Django
	
	git command line tool (Git Bash)

Installation 

	For collaborators: Clone this repository directly.
	For public users: First, fork this repository to your own Github account, then clone your fork.
		
  		git clone [repository-URL]
	
	Navigate to the project directory:
 
		cd [repository-name]
	
 	Create and activate a virtual environment to manage project dependencies
  
		python -m venv virt
		source virt/bin/activate
  	
	Install Django
		
		pip install django

	Go to main folder

	    cd main

	Add/update Database

        python manage.py make migrations
        python manage.py migrate  [note: this creates/updates db.sqlite for your local]
	
	Run the application
 
		python manage.py runserver

	Copy server address [URL] to browser to see app


Agile Planning

Team members and Roles

	Joanna Rios - Technical Lead, Code Reviewer, & System Architect
 
	Responsibilities: Drives the technical vision, sets up the Git/GitHub repository and development environment, designs the overall software architecture, creates UML diagrams, and ensures code quality. The “swiss army knife” responsible for the technical documentation and ensuring deadlines are met. 

 
	Alicia Cortina - UI/UX Specialist/Prototyper & Feature Developer
 
	Responsibilities: Focuses on the user interface design ( lfigma ayouts, widgets, user flow), implements specific features like the "Activities/Task Schedule Manager" and "Bulletin Board," ensuring a good user experience.

 
	Emma Pacheco - Contacts Information Implementer
 
	Responsibilities: Meant to focus on emplementation of "Emergency Contacts". A static page that presents dummy data of University Emergency and General Contacts.


Sprint Schedule
 
	Sprint 1
		Start Date: Aug 1
		End Date: Aug 5
		Activities: 
			Set up a repository (and any other channels of communication Google Docs, Discord, Whatsapp, etc.)
			Define features (user stories)
			Draft documentation (User Manual - README & Technical Doc.)

	Sprint 2
		Start Date: August 6
		End Date: August 11
		Activities: 
			Core UI Setup: Setup basic structure for interactivity.
			Responsive Layout: Setup layout that responds to mobile/web views.
			Navigation: Setup the primary navigation structure to switch between sections.
   			Log In/ Create Account: Get the login and account creation flow running.
			Placeholder Sections: Create empty frames/sections/pages for each of the main features (Activities, Events, Bulletin Board, Emergency Contacts, Account Info. with logout).
			Initial Wireframes: Finalize basic UI wireframes & prototypes for the overall app layout.

	Sprint 3
		Start Date: August 12
		End Date: August 20
		Activities: 
			High Priority UI Implementation: Implement basic UI for all priority 1 user stories.
			Attempt Priority 2
			Documentation Update: Ensure all project documentation is up-to-date with current state.
			Final Presentation Prep: Prepare for final presentation.


User Stories


	0	User Authentication & Account Management
	
	As a student, I want a secure and personalized experience, so I must first create an account and log in to access my personal data and the app’s features

 
	0.1	Create an Account
	
	As a new student, I want to create an account by providing a unique username and password, so that I can securely access the CampusLink application for the first time.

 
	0.2	Log In to Account

	As a student, I want to log in to my account with my username and password, so that I can access my personalized schedule, tasks, and campus information.

 
	0.3	View Account Details
	
	As a student, I want to see my username and account details in an “Account” tab, so that I can verify I am logged in and feel a sense of ownership over my data.

 
	0.4	Log Out of Account
	
	As a student, I want to log out of my account from the “Account” tab, so that my personal information is protected when I am no longer using the application.


	1	Activities/Task Manager	

	As a student, I want to easily manage my weekly schedule, including classes, appointments, and personal tasks, so I can stay organized and on top of my commitments.


	1.1	View Personal Schedule

	As a student, I want to view my weekly schedule of activities and tasks on my browser, so I can quickly see my commitments for the day or week.


	1.2	Add Activities/Tasks

	As a student, I want to be able to add new activities or tasks(ex: class, study group, appointment,etc.) with details like title, description, date, and time, so I can keep my schedule updated from anywhere.


	1.3	Receive Activity Reminders

	As a student, I want to be able to receive timely notifications (ex: browser push notifications, in-app alerts, etc.), so I can keep 


	1.4	Mark Tasks as Complete
	As a student, I want to mark tasks as complete, so I can track my progress and organize my pending items.


	2	Bulletin Board

	As a student, I want to browse and post campus-relevant announcements, news, and student initiatives, so I can stay informed and connect with the campus community.


	2.1	View Announcements

	As a student, I want to view a scrollable feed of announcements posted on the bulletin board, so I can stay informed about campus news and opportunities.


	2.2	Post New Announcements

	As a student, I want to be able to compose and post new announcements (ex: lost and found, study group invites, club promotions, etc.), so I can share information with the community.


	3	Emergency Contacts

	As a student, I want quick, one-click access to essential campus services like security, health, and counseling, so I can get help immediately in an emergency.


	3.1	Access Emergency Contacts

	As a student, I want quick access to a clearly displayed list of emergency and support contacts (ex: Campus Security, Health Services, Counseling) within a dedicated section, so I can get help when needed.


	3.2	View Contact Details

	As a student, I want to be able to tap/click on a contact to view their full phone number and any additional relevant details, so I can easily reach out for assistance.


