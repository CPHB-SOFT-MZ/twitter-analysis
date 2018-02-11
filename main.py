import optparse
import pprint

from twitteranalysis import TwitterAnalysis


def main():
    tw = TwitterAnalysis()
    p = optparse.OptionParser()
    p.add_option("--function", "-f")

    options, arguments = p.parse_args()

    if options.function != None:
        if options.function == '1':
            pprint.pprint(list(tw.number_of_users()))
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