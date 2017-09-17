888~-_     ,88~-_     ,88~-_   888~~  888 888~~  888~~\    ,88~-_   ~~~888~~~ 
888   \   d888   \   d888   \  888___ 888 888___ 888   |  d888   \     888    
888    | 88888    | 88888    | 888    888 888    888 _/  88888    |    888    
888    | 88888    | 88888    | 888    888 888    888  \  88888    |    888    
888   /   Y888   /   Y888   /  888    888 888    888   |  Y888   /     888    
888_-~     `88_-~     `88_-~   888    888 888___ 888__/    `88_-~      888 
                                                                         v0.1


_**doofieBot** is your favorite foodieFriend!_ a resourceful chatbot who will stop at nothing to fulfill your gluttonous dreams  

#### how it works
- The latest iteration of **doofieBot** lurks on [Slack](https://api.slack.com/), its backend built with [Flask](http://flask.pocoo.org/) & powered by [Amazon EC2](https://aws.amazon.com/). 
- **doofieBot** makes use of IBM's powerful [Watson Visual Recognition API](https://www.ibm.com/watson/services/visual-recognition/) to interpret pictures of delicious food queried by the user. 
- After intelligently recognizing the food, **doofieBot** calls on [Yelp Fusion](https://www.yelp.com/fusion) to generate a list of nearby restaurants or businesses that serve or sell what you are looking for!

#### how it's built
- over the [Flask](http://flask.pocoo.org/) framework, managed by [pip](https://pip.pypa.io/en/stable/), running on an [Apache](https://httpd.apache.org/) server & hosted in the cloud by [Amazon EC2](https://aws.amazon.com/ec2/)
- [Slack SDK for Python](https://slackapi.github.io/python-slackclient/)
- [IBM Watson Visual Recognition V3](https://www.ibm.com/watson/developercloud/visual-recognition/api/v3/)
- [Yelp Fusion API](https://github.com/Yelp/yelp-fusion/tree/master/fusion/python)
- _DEPRECATED_ [Zomato API](https://developers.zomato.com/api)
- _PROVISIONAL_ [pyMessenger SDK/Client](https://github.com/davidchua/pymessenger) c/o [Facebook Messenger Platform](https://developers.facebook.com/docs/messenger-platform) via [Google Firebase](https://firebase.google.com/)

#### how it was done
- **doofieBot** was built by a collaborative team of students from UBC (University of British Columbia) and UTSC (University of Toronto in Scarborough) for [Hack the North 2017](https://hackthenorth.com/) (15-17 September).  

#### development notes & instructions
- Download all the forementioned SDKs / tools, in addition to anything else mentioned on `setup.sh`  
- The bilbo-backend is accessible over AWS console. Make your life easier by doing the following:  
    1. Store the `htn.pem` key to your local `~/.ssh` folder
    2. In your `~/.ssh/config` file, copy in:
        Host bilbo
            Hostname x.x.x.x
            User ubuntu
            IdentityFile ~/.ssh/htn.pem
    3. Access server from your CLI by invoking `$ ssh bilbo`  
- See further instructions inside the `env/` directory for configuration details, API keys etc

