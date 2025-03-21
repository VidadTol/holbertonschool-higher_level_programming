#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    """ Check Imput Types"""
    try:
        if not isinstance(template, str):
            raise TypeError('Error: template must be a string')
        if not isinstance(attendees, list) or not all(
                isinstance(attendee, dict) for attendee in attendees):
            raise TypeError('Error: attendees must be a list of dictionaries')

    except TypeError as e:
        print("TypeError: {}".format(e))
        return

    """ Handle Empty List"""
    try:
        if not template:
            raise ValueError("template is empty")

        if not attendees:
            raise ValueError("Error: the participant list is empty")

    except ValueError as e:
        print("ValueError: {}".format(e))
        return

    """ treatment of each paticipant"""
    for i, attendee in enumerate(attendees):
        invitation = template

        """ Replace placeholders with corresponding values, if empty N/A"""
        invitation = invitation.replace(
            "{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace(
            "{event_title}", attendee.get("event_title", "N/A"))
        invitation = invitation.replace(
            "{event_date}", attendee.get("event_date", "N/A"))
        invitation = invitation.replace(
            "{event_location}", attendee.get("event_location", "N/A"))

        """Creating output files """
        filename = f"output/invitation_{i + 1}.txt"

        """ Check if file already exists"""
        if os.path.exists(filename):
            print(f"Error: the file '{filename}' already exists")

        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error when writing file '{filename}': {e}")
