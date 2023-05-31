# Amazon-Automated-Price-Tracker

A small program I made to practice webscraping with BeautifulSoup and sending emails with smtplib. This program takes a link for a product on Amazon and a "target price." 
Once the price of the product falls to the target price, the program sends an email with a notification. 

I was initially sending text message notifications with a free public Twilio API, but they suspended my account with no explanation provided. So I just used smtplib to send
email notifications.
