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
11. Now you can run the program by running one of the following commands:
- 
