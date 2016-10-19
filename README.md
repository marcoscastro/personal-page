# My personal website
My personal page made with Python language and Bottle (web-framework for Python). Python + Bottle = happiness ;-)

The application running:: http://www.mcastrosouza.com

# Deploy on Heroku
I used the cloud platform Heroku. This tutorial helped me for deploy on Heroku: https://github.com/chucknado/bottle_heroku_tutorial

# Setup Heroku and Godaddy
For domain I used Godday, setup Heroku and Godaddy:

1. In your project folder in terminal write: heroku domains:add www.example.com (where www.example.com is the domain you have bought at GoDaddy).

2. Sign in to GoDaddy -> DOMAINS -> choose your domain -> Launch (this will take you to the Domain Details)

3. Click 'DNS Zone File' tab

4. Remove the CNAME record named 'www' (which points to @)

5. Click 'Add record' -> CNAME(Alias) -> 'Host' should be www and 'Points to' should be your Heroku address (example mcastrosouza.herokuapp.com). TTL can be 1 hour.

It can take some time for the DNS to propogate. For me it took about 10 minutes.

That's it! example.herokuapp.com will now be under www.example.com :)

Original tutorial: http://bit.ly/SetupHerokuGoDaddy

# Contact
You can use and do what you want! Doubts? mcastrosouza@live.com