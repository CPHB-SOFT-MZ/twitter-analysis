import optparse
import pprint

from twitteranalysis import TwitterAnalysis


def main():
    tw = TwitterAnalysis()
    p = optparse.OptionParser()
    pprint.pprint(list(tw.most_mentioned_users()))

if __name__ == "__main__":
    main()