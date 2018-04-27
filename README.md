# ThesisToolBox

# A simple webapp to scrape the Hansard database, organize sources and link them together with tags and comments 

The British parliamentary database (hansard / https://api.parliament.uk/historic-hansard/index.html) leaves a lot to be desired. They are updating the website but this will take time and much of the search functionality has been disabled during the migration process. 

ThesisToolBox comes equipped with a scraper to download the sources of the hansard archive to its own postgres database. 
The site itself looks rather spartan (A am using it as I write my Thesis, leaving little time for luxuries such as interface design - something which my colleagues will attest is one of my strong points), but it is functional enough. 

You either access the database or perform queries to find the results that you need . You can also add additional sources, such as books and articles. All objects can be commented and all receive tags. By accessing these tags the user can get a quick overview of all sources, debates, search results and comments that are associated with this tag – allowing for a quick way of organizing both your sources and keeping notes. 


# Search the database
![Alt text](/images/queries.png?raw=true)

# View the results
![Alt text](/images/abrresults.png?raw=true)

# View the debates
![Alt text](/images/debateoverview.png?raw=true)

# Investigate the Speakers
![Alt text](/images/speaker.png?raw=true)

# Read their speeches
![Alt text](/images/speaker.png?raw=true)

# Add comments and tags
![Alt text](/images/text.png?raw=true)

# Add sources, link them to tags
![Alt text](/images/sources.png?raw=true)


# Installation - extra steps!
1. Add the required variables to the 'settings.py' file
2. Run migrations and start the program either locally or on a server. 



