# Twitter data analysis
### How to make it run
1. Run `docker run --rm -v $(pwd)/data:/data/db --publish=27017:27017 --name dbms -d mongo:latest`
2. Run `docker exec -it {id returned from last command} bash`
3. Run `apt-get update`
4. Run `apt-get install -y wget unzip git python3 python3-pip`
5. Run `wget http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip`
6. Run `unzip trainingandtestdata.zip`
7. Run `sed -i '1s;^;polarity,id,date,query,user,text\n;' training.1600000.processed.noemoticon.csv`
8. Run `mongoimport --drop --db social_net --collection tweets --type csv --headerline --file training.1600000.processed.noemoticon.csv`
9. Run `git clone https://github.com/ziemerz/twitter-analysis.git && cd twitter-analysis/`
10. Run `pip3 install -r requirements.txt`
11. Now you can run the program with the following command: `python3 main.py -f 1`

The `1` after the `-f` flag, indicated what function you want to execute. They map as follow:
- 1: Total number of distinct users
- 2: Users mentioning others most
- 3: Most mentioned users
- 4: Top ten active users
- 5: Most grumpy, and most happy users based on tweets

12. If your database has another name, server or port than the default, you can run `python3 main.py --help` to see all available flags


## The 5 answers
1. 659774
2. 
```js
[{'_id': 'lost_dog', 'count': 546},
 {'_id': 'tweetpet', 'count': 302},
 {'_id': 'VioletsCRUK', 'count': 251},
 {'_id': 'what_bugs_u', 'count': 244},
 {'_id': 'SallytheShizzle', 'count': 226},
 {'_id': 'Karen230683', 'count': 216},
 {'_id': 'mcraddictal', 'count': 214},
 {'_id': 'keza34', 'count': 211},
 {'_id': 'TraceyHewins', 'count': 202},
 {'_id': 'DarkPiano', 'count': 199}]
 ```
3.
```js
[{"_id": '@mileycyrus', 'count': 4310},
 {'_id': '@tommcfly', 'count': 3837},
 {'_id': '@ddlovato', 'count': 3349},
 {'_id': '@Jonasbrothers', 'count': 1263},
 {'_id': '@DavidArchie', 'count': 1222},
 {'_id': '@jordanknight', 'count': 1105},
 {'_id': '@DonnieWahlberg', 'count': 1085},
 {'_id': '@JonathanRKnight', 'count': 1053},
 {'_id': '@mitchelmusso', 'count': 1038},
 {'_id': '@taylorswift13', 'count': 973}]
```
4.
```js
[{'_id': 'lost_dog', 'count': 549},
 {'_id': 'webwoke', 'count': 345},
 {'_id': 'tweetpet', 'count': 310},
 {'_id': 'SallytheShizzle', 'count': 281},
 {'_id': 'VioletsCRUK', 'count': 279},
 {'_id': 'mcraddictal', 'count': 276},
 {'_id': 'tsarnick', 'count': 248},
 {'_id': 'what_bugs_u', 'count': 246},
 {'_id': 'Karen230683', 'count': 238},
 {'_id': 'DarkPiano', 'count': 236}]
```
5.1 Grumpy users
```js
[{'_id': 'lost_dog', 'count': 549},
 {'_id': 'tweetpet', 'count': 310},
 {'_id': 'webwoke', 'count': 264},
 {'_id': 'mcraddictal', 'count': 210},
 {'_id': 'wowlew', 'count': 210}]
```
5.2 Happy users
```js
[{'_id': 'what_bugs_u', 'count': 246},
 {'_id': 'DarkPiano', 'count': 231},
 {'_id': 'VioletsCRUK', 'count': 218},
 {'_id': 'tsarnick', 'count': 212},
 {'_id': 'keza34', 'count': 211}]
```
