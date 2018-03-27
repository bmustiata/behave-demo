Feature: list can list files.

@1
Scenario: Listing all the files works as expected.
Given I have a copy of my test folder
When I execute 'ls'
Then 'a.txt' is in the test folder
And 'b.txt' is not in the test folder

@2 @details
Scenario: Listing a file with -a should list the file
Given I have a copy of my test folder
When I execute 'ls -la a.txt'
Then I get the full listing of 'a.txt' including attributes

