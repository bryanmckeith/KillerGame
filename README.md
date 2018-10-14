# KillerGame

The "Killer Game", also known as Assassin, Gotcha, Killer or paranoïa is a live-action game in which players try to eliminate one another using mock weapons, in an effort to become the last surviving player.

## About Killer Game

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them :

* Python 3.4 or higher
* Django 2.0.2 or higher

### Customizing config.json

If you intend to use the Killer Game, you will need to change settings in the config.json file.

In this initial version, we send missions and targets to the players via SMS using esendex APIs. Create your account and fill in the specific tokens :

```bash
"username":"<YOUR_USERNAME>",
"password":"<YOUR_PASSWORD>",
"accountReference":"<YOUR_ACCOUNT_REFERENCE>",
"expeditor":"Killer Game"
```

In a coming version, you will be able to connect to your Slack workspace.

### Limitations

Killer Game is a "one shot" app that I developed "as it is" :)
It is still work in progress and may have a lot of potential optimizations.
Among potential new features :

* Be multi_lingual (app is in French in its initial version)
* Be connected to Slack
* Enable multiple games

### Rules and screenshots

![alt text](https://github.com/bryanmckeith/KillerGame/blob/master/home-screenshot.png)
![alt text](https://github.com/bryanmckeith/KillerGame/blob/master/ranking-srceenshot.png)
![alt text](https://github.com/bryanmckeith/KillerGame/blob/master/SMS-screenshot.png)

Every player should subscribe via the dedicated page. Players will need to give Firstname, Name, Phone number and a pseudo.

Once everyone has subscribed, the admin will need to start game via start_game page. When it's done, every player receives a SMS message on his/her smartphone to tell him/her who his/her target is, and what action to perform as a murder as well as a personal secret code.

Every player can see the game's ranking.

## Contributing

Please feel free to contact us for details on our code of conduct, and the process for submitting pull requests to us.

## Author

* **Bruno MARQUET** - *Initial work*

See also the list of [contributors] who participated in this project.
