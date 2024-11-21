# Statistics

Let's get some statistics from the companies and their employees.

As you can see every company has warnings and every person can have law violations, let's find out what these companies are up to.

Create a commandline based application where:
- we can request which company has the most and least warnings
- we can request which person has the most law violations

- Each violation has a level that indicates the seriousness of the crime. Find out who are the top 5 most dangerous men in our database.
- Make a statistic about the companies in a new json file with the following system. Every company has a violation_score. If the company has warnings with the  "light" level than it adds 5 violation_score if it's "hard" than it adds 50 and for every employee that works in the company for every law_violation they get scores equal to the employee's scrime level. Make a functionality that can display this information on the terminal but these statistics also have to saved in a dedicated file (crime_stats.json).