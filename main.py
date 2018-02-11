import optparse
import pprint

from twitteranalysis import TwitterAnalysis


def main():
    tw = TwitterAnalysis()
    p = optparse.OptionParser(description='Executes a function on the Twitter data set',
                              usage='main.py -f [1-5]')
    p.add_option("--function", "-f", help="Mandatory. Choose the function number to execute. It goes from 1 to 5, both inclusive")
    p.add_option("--server", "-s", help="Optional. Set database server address. Default is 'localhost'")
    p.add_option("--port", "-p", help="Optional. Port of the database server/instance. Default is '27017'")
    p.add_option("--dbname", "-n", help="Optional. Database name. Default is 'social_net'")
    p.add_option("--collection", "-c", help="Optional. Collection to get the data from. Default is 'tweets'")

    options, arguments = p.parse_args()

    if options.server != None:
        tw.set_db_server(options.server)
    if options.port != None:
        tw.set_port(options.port)
    if options.dbname != None:
        tw.set_db_name(options.dbname)
    if options.collection != None:
        tw.set_db_collection(options.collection)

    tw.connect()

    if options.function != None:
        if options.function == '1':
            print("Total number of distinct users")
            pprint.pprint(tw.number_of_users())
            return
        if options.function == '2':
            print("Users mentioning others most")
            pprint.pprint(list(tw.users_mentioning_others_most()))
        if options.function == '3':
            print("Most mentioned users")
            pprint.pprint(list(tw.most_mentioned_users()))
        if options.function == '4':
            print("Top ten active users")
            pprint.pprint(list(tw.top_ten_active_users()))
        if options.function == '5':
            print("Most grumpy users are...")
            pprint.pprint(list(tw.most_grumpy_users()))

            print("Most happy users are...")
            pprint.pprint(list(tw.most_happy_users()))

if __name__ == "__main__":
    main()