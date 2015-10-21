# lapcounter-backend
For 10/28, make sure that you have a flask instance of Heroku running, everyone has been added to it, and all the code has also been pushed to this repository.
Hardcode the following routes to return the following information via json:

/info/users
* A method to return an array of all users
/user/info
* A method to return all information of a specific user
  * Name
  * Year
  * When they registered
  * Average Lap Completion Time
  * Average Speed
  * Fastest Lap Time
  * Total Laps Completed
  * Total Distance Ran
  * Total time spent running

/session/info
* A method to return all information of a specific running session
  * Average Lap Speed
  * Fastest Lap Speed
  * Duration of Session
  * Start and End time of Session