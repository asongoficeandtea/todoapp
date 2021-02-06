# My Flask Project

## Project overview

> The aim of this project was to design a web application with CRUD functionality.

### Design Process

> I started with designing and ER diagram and first design was a table called List which would be the parent table and a table called Task which would be the child table. The design was meant to allow a user to create different lists for different purposes such as a list for shopping, one for daily tasks and another for weekly goals.

> In the end due to issues in understanding relationship configuration between the two tables led me to create an app with one table in order to create tasks. I decided to do so in order to create a functioning product but also demonstrate the extent of my learning within this training course. 

### Application Development

> I started off using vi editor on my Linux machine in order to be more comfortable using the editor. I had trouble at first but as I continued writing the code, it became easier. I then had issues with this as the installation of Jenkins significantly slowed down my instance and I had to switch to a vritual box. This had its issues as well as my keyboard wasn't corresponding with the commands that appeared on the terminal within the virtual box machine. 

> I then decided to develop my application on VS Code editor and finish my work on a new GCP instance. This worked out very well and I was able to utilise Git from VS Code editor and practice adding and committing changes as well as branching and merging.

> Project management aspect of this process was challenging. I had not worked in this manner before and it took getting used to. I however understood the benefit of utilising a Kanban board and having user stories and tasks to organise the development process. 

#### Unit testing

The unit testing portion was a significant challenge at first. I had issues with tests failing and understanding how to rectify the issues. I did not reach the goal I hoped of all tests passing however I did make pogress. The tests started off with only 2 of the tests passing out of 6. I managed to get that number to 4 tests passing and two failing.

### Risk Assessment

* Limitations
    * No personalisation to the user
    * No CSRF Protection as form.hidden_tag() and secret key not utilised
    * No form of encryption utilised as information provided by the user is not intended to be sensitive

## Conclusion

> I did enjoy writing the code and understanding how an application is built and deployed utilising cloud-enabling technology. I have an improved knowledge of automation and how to set up automation in my processes. This was very evident in unit testing and this module was incredibly useful for my learning process. 

> In my next project, I aim to develop an app utilising two database tables in order to produce applications with extended functionality. 


