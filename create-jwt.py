#! /usr/bin/env python
import jwt
import time
import argparse


def create_jwt(app_id, private_key):
    now = int(time.time())

    payload = {
        # issued at time
        "iat": now,
        # JWT expiration time (10 minute maximum)
        "exp": int(now + (9 * 60)),
        # GitHub App's identifier
        "iss": app_id
    }
    token = jwt.encode(payload, private_key, algorithm='RS256')
    file = open('jwt.txt', 'w')
    file.write(token.decode("utf-8"))


parser = argparse.ArgumentParser()
parser.add_argument("app_id")
parser.add_argument("private_key_file")

args = parser.parse_args()

create_jwt(args.app_id, open(args.private_key_file).read())