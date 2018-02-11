import optparse
import pprint

from twitteranalysis import TwitterAnalysis


def main():
    tw = TwitterAnalysis()
    p = optparse.OptionParser(description='Executes a function on the Twitter data set',
                              usage='main.py -f [1-5]')
    p.add_option("--function", "-f", action="store_true", help="Mandatory. Choose the function number to execute. It goes from 1 to 5, both inclusive")
    p.add_option("--database", "-b", action="store_true", help="Optional. Set database address. Default is 'localhost'")
    p.add_option("--port", "-p", action="store_true", help="Optional. Port of the database server/instance. Default is '27017'")

    options, arguments = p.parse_args()

    if options.database != None:
        tw.set_db_name(options.database)
    if options.port != None:
        tw.set_port(options.port)

    tw.connect()

    if options.function != None:
        if options.function == '1':
            print("Total number of distinct users")
            pprint.pprint(tw.number_of_users())
            return
        if options.function == '2':
            pprint.pprint(list(tw.users_mentioning_others_most()))
        if options.function == '3':
            pprint.pprint(list(tw.most_mentioned_users()))
        if options.function == '4':
            pprint.pprint(list(tw.top_ten_active_users()))
        if options.function == '5':
            print("Most grumpy users are...")
            pprint.pprint(list(tw.most_grumpy_users()))

            print("Most happy users are...")
            pprint.pprint(list(tw.most_happy_users()))

if __name__ == "__main__":
    main()