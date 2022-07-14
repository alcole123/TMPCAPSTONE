import requests
import json
import sys
import os
import argparse

my_parser = argparse.ArgumentParser(prog='pyblog', description='Program used to read and make blog posts')
my_parser.add_argument('command', type=str)
my_parser.add_argument('-f', '--file', help="Name of the file to create blog post from")
my_parser.add_argument('text_input', nargs='?', type=str, default="-", help="Name of the file to create blog post from")

args = my_parser.parse_args()

default_url = "http://127.0.0.1/blog/index.php/wp-json/wp/v2/posts"

headers = {
  'Accept': 'application/json',
  #'Content-Type': 'application/json',
  'Authorization': 'Basic d29yZHByZXNzLWFkbWluOjhCVG4gWDRrQyBxbklYIHNueVIgQmxwWiBpSzVN'
}

#filename = "latinfile"
def post():

    rest_method = "POST"
    url = default_url
    payload={'Content': 'Test Content',
    'title': 'Python Test Post',
    'excerpt': 'Posted using Python',
    'status': 'publish'}

    response = requests.request(rest_method, url, headers=headers, data=payload)

    print(response.text)

def upload():
    input_file = args.file or args.text_input
    for input_file in sys.stdin:
       
        lines = input_file
        title = lines.split('\n', 1)[0]              
        excerpt = lines.split('\n', 2)[2]

    else:
        with open(input_file) as file:
            lines = file.read()
            title = lines.split('\n', 1)[0]
            excerpt = lines.split('\n', 2)[2]

   
    rest_method = "POST"
    url = default_url
    payload={'Content': 'File Content',
    'title': title,
    'excerpt': excerpt,
    'status': 'publish'}

    response = requests.request(rest_method, url, headers=headers, data=payload)

    print(response.text)

def read():

    rest_method = "GET"
    url = default_url +"?per_page=1"
   
    response = requests.request(rest_method, url, headers=headers)

    print(response.text)

if args.command == "read":
    read()

if args.command == "upload":
    upload()