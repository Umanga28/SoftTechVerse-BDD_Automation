Feature: Verifying Login Functionality
Scenario: Login with valid data
Given user is on Login Page
When user enters username
And user enters password
And user click on Login button
Then user should be entered on Dashboard

Scenario: Login with invalid username
Given user is on Login Page
When user enters username
And user enters password
And user click on Login button
Then user should get message "Username or Password is incorrect"