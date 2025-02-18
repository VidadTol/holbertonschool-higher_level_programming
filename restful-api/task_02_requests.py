#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from the API and print them.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch posts from the API and save them to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    status_code = response.status_code
    posts = response.json()
    data = [
        {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        for post in posts]

    with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("Posts have been saved to post.csv")
