# CampusLink_WebMobileApp


Project Title: CampusLink Web App

Project Description

CampusLink is a web application designed to serve as a centralized hub for university students. The application aims to simplify a student’s academic and social life by providing a single, portable platform to manage schedules, discover events, stay informed through a community bulletin board, and access critical emergency contacts, accessible from any device, anywhere.

Key Features

	User Authentication & Account Management: A secure system to create unique accounts, log in, and log out and a space for displaying user information and managing sessions

	Activities & Task Schedule Manager: A user friendly interface to add, view, and edit a weekly schedule of classes, appointments, and personal tasks optimized for touch interaction and mobile screens.
	
 	Event Calendar: An interactive calendar to view and subscribe to various campus events. Categorized by interest such as academic, sports, clubs, and more, with responsive display across devices.
	
 	Bulletin Board: A dedicated section for Browse and posting announcements relevant to the campus community, including news, queries, and student led activities/initiatives, designed for easy readability and posting on the go.
	
 	Emergency Contacts: A quick access panel with one click buttons to contact essential campus services like security, health, and counseling.


Development Methodology

This project is being developed using an agile methodology with an emphasis on iterative development, continuous feedback, testing, and collaboration through version control.


Basic Usage Instructions

To get a local copy of this project up and running on your machine, follow these simple steps.

Prerequisites 

	Python 3.x installed on your system
	git command line tool

Installation 

	For collaborators: Clone this repository directly.
	For public users: First, fork this repository to your own Github account, then clone your fork.
		
  		git clone [repository-URL]
	
	Navigate to the project directory:
 
		cd [repository-name]
	
 	Create and activate a virtual environment to manage project dependencies
  
		python -m venv virt
		Source virt/bin/activate
  
	Run the application
 
		python main.py


Agile Planning

Team members and Roles

	Joanna Rios - Technical Lead & System Architect
 
	Responsibilities: Drives the technical vision, sets up the Git/GitHub repository and development environment, designs the overall software architecture, creates UML diagrams, and ensures code quality. The “swiss army knife” responsible for the technical documentation and ensuring deadlines are met.

 
	Alicia Cortina - UI/UX Specialist/Prototyper & Feature Developer
 
	Responsibilities: Focuses on the user interface design ( layouts, widgets, user flow), implements specific features like the "Activities/Task Schedule Manager" and "Bulletin Board," ensuring a good user experience.

 
	Emma Pacheco - Backend Logic & Data Specialist / Tester
 
	Responsibilities: Develops the underlying logic for features (e.g., notification systems, data handling for events/schedules), manages data storage, sets up and runs testing procedures, and might focus on aspects like the "Event Calendar" data integration or "Emergency Contacts" logic.


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

	As a student, I want to view my weekly schedule of activities and tasks on my mobile device/browser, so I can quickly see my commitments for the day or week.


	1.2	Add/Edit Activities/Tasks

	As a student, I want to be able to add new activities or tasks(ex: class, study group, appointment,etc.) with details like title, description, date, and time, so I can keep my schedule updated from anywhere.


	1.3	Receive Activity Reminders

	As a student,  I want to be able to receive timely notifications (ex: browser push notifications, in-app alerts, etc.), so I can keep 


	1.4	Mark Tasks as Complete
	As a student,  I want to mark tasks as complete, so I can track my progress and organize my pending items.


	2	Event Calendar
	As a student,  I want to find and subscribe to campus events categorized by my interests (academic, sports, clubs), so I can discover relevant activities and participate in campus life.
	

	2.1	Browse Campus Events

	As a student,  I want to browse a list or grid of upcoming campus events, so I can discover activities relevant to my interests.


	2.2	Filter Events by Category

	As a student,  I want to filter events by categories (ex: Academic, Sports, Civil, Clubs, etc.), so I can easily find events that match my preferences.


	2.3	View Event Details

	As a student, I want to click on an event to view detailed information (ex: date, time, location, full description, etc.), so I can decide whether to attend. 


	2.4	Add Event to Personal Schedule

	As a student,I want to be able to add a campus event to my personal schedule within the app, so I can integrate it into my daily plan.


	3	Bulletin Board

	As a student, I want to browse and post campus-relevant announcements, news, and student initiatives, so I can stay informed and connect with the campus community.


	3.1	View Announcements

	As a student, I want to view a scrollable feed of announcements posted on the bulletin board, sorted by recency, so I can stay informed about campus news and opportunities.


	3.2	Post New Announcements

	As a student,I want to be able to compose and post new announcements (ex: lost and found, study group invites, club promotions, etc.), so I can share information with the community.


	3.3	Search/Filter Announcements

	As a student,  I want to search or filter announcements by keywords or categories (if applicable), so I can quickly find relevant information.


	4	Emergency Contacts

	As a student,  I want quick, one-click access to essential campus services like security, health, and counseling, so I can get help immediately in an emergency.


	4.1	Access Emergency Contacts

	As a student,  I want quick access to a clearly displayed list of emergency and support contacts (ex: Campus Security, Health Services, Counseling) within a dedicated section, so I can get help when needed.


	4.2	View Contact Details

	As a student, I want to be able to tap/click on a contact to view their full phone number and any additional relevant details, so I can easily reach out for assistance.


