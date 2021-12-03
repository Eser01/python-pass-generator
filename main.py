#!/usr/bin/env python3

import sys
import random
import string
import argparse

def normalize_probabilities(probabilities:list):
    if len(probabilities) > 0:
        total = sum(probabilities)
        return [ (value/total)*100 for value in probabilities ]
    return probabilities

def generate_password(length:int, samples:list, weights:list):
    if len(samples) == 0 or len(weights) == 0:
        raise Exception('There are no character sets!')

    if len(samples) != len(weights):
        raise Exception('The lists are not linked!')
    
    if length < 4:
        raise Exception('A password must have at least 4 characters!')

    password = ''
    for i in range(length):
        sample = random.choices(samples, weights=weights, k=1)
        sample = sample[0]
        character = random.choice(sample)
        password += character
    
    return password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Random characters password generator.',
        add_help=False
    )
    parser.add_argument('-h', '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='Show this help message and exit.'
    )
    parser.add_argument('length',
        metavar='LENGTH',
        type=int,
        help='The length of the password (min: 4).'
    )
    parser.add_argument("-u", "--upper",
        action="store_false",
        dest="upper",
        default=True,
        help="Disable ascii upper letters (enabled by default)"
    )
    parser.add_argument("-l", "--lower",
        action="store_false",
        dest="lower",
        default=True,
        help="Disable ascii lower letters (enabled by default)."
    )
    parser.add_argument("-d", "--digit",
        action="store_false",
        dest="digits",
        default=True,
        help="Disable digit characters (enabled by default)."
    )
    parser.add_argument("-p", "--punctuation",
        action="store_true",
        dest="punctuation",
        default=False,
        help="Enable punctuation symbols (disabled by default)."
    )

    args = parser.parse_args()

    samples = []
    weights = []

    if args.upper:
        samples.append(string.ascii_uppercase)
        weights.append(35)

    if args.lower:
        samples.append(string.ascii_lowercase)
        weights.append(35)

    if args.digits:
        samples.append(string.digits)
        weights.append(20)

    if args.punctuation:
        samples.append('!#$&()*+,-.:;=?@_')
        weights.append(10)
    
    weights = normalize_probabilities(weights)

    try:
        pass_length = args.length if args.length > 3 else 16
        password = generate_password(pass_length, samples, weights)
        print(password)
    except Exception as ex:
        message = 'Error: '
        message += ex.message if hasattr(ex, 'message') else str(ex)
        print(message, file=sys.stderr)
        sys.exit(-1)
