#!/usr/bin/env python3

'''
Exercise in interacting w/ ReST APIs
'''

import argparse             # Accept and use input parameters to script
import requests             # Interact w/ API using HTTP
import sys                  # Exit script


def setup_args():
    '''
    Funtion builds parsing object to pass to main function.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", type=str.lower, default=None,
                        help="Provide name of the GitHub user to lookup.\n")
    return parser


def main():
    '''
    Script's main function
    '''
    p = setup_args()
    args = p.parse_args()

    if args.user:
        user = args.user
    else:
        user = str(input("Which user do you want to look for?: "))
    user_url = "https://api.github.com/users/{}".format(user)
    repos_url = "https://api.github.com/users/{}/repos".format(user)

    user_r = requests.get(user_url)
    if not user_r.ok:
        print("Unable to find that user. Error code", user_r.status_code)
        sys.exit()
    repos_r = requests.get(repos_url)
    user_parsed = user_r.json()
    repos_parsed = repos_r.json()

    join_date = user_parsed["created_at"]
    public_repos = user_parsed["public_repos"]
    followers, following = user_parsed["followers"], user_parsed["following"]

    print("{} joined GitHub on {}.".format(user, join_date))
    print("They are following {} users and has {} followers.".format(following, followers))
    print("They have {} public repos.".format(public_repos))
    print("The names of their repos are:")
    for repo in repos_parsed:
        print("\t{}".format(repo["name"]))


if __name__ == "__main__":
    main()

sys.exit()
