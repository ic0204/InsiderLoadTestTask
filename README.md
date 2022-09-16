# InsiderLoadTestTask

Test Scenarios:
-   Checks whether the anonymous user can reach n11.com home page.
-   Checks whether the anonymous user can search for random products from the search engine.

Load : 

      ->Locust -f N11LoadTest\load.py
      
      When you can this command , you go to Locust home page from http://localhost:8089/
      Click the New test button on the page that opens.
      In the popup screen that opens, enter the number of users,spawn rate and host address
      Click the start swarming button
      You can see the statistical values of the load test you have done on the page that opens.
      
     
      
