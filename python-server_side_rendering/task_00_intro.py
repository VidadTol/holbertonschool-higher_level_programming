#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    """ Check Imput Types"""
    try:
        if not isinstance(template, str):
            raise TypeError('Error: template must be a string')
        if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
            raise TypeError('Error: attendees must be a list of dictionnaries')
    
    except TypeError as e:
        print("TypeError: {}".format(e))
        return
    
    """ Handle Empty List"""
    try:
        if not template:
            raise ValueError("Error: template is empty")
      
        if not attendees:
            raise ValueError("Error: the participant list is empty")
    
    except ValueError as e:
        print("ValueError: {}".format(e))
        return
    
    """ treatment of each paticipant"""
    for i, attendee in enumerate(attendees):
        invitation = template

        """ Replacement of reserved spaces """
        if "name" in attendee:
                invitation = invitation.replace("{name}", attendee["name"])
        else:
                invitation = invitation.replace("{name}", "N/A")

        if "event_title" in attendee:
                invitation = invitation.replace("{event_title}", attendee["event_title"])
        else:
                invitation = invitation.replace("{event_title}", "N/A")

        if "event_date" in attendee:
                invitation = invitation.replace("{event_date}", str(attendee["event_date"])) 
        else:
                invitation = invitation.replace("{event_date}", "N/A")

        if "event_location" in attendee:
                invitation = invitation.replace("{event_location}", attendee["event_location"])
        else:
                invitation = invitation.replace("{event_location}", "N/A")

        """Creating output files """
        filename = f"output/invitation_{i + 1}.txt"
        if os.path.exists(filename):
            print("file '{}' already exists".format(filename))

        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error when writing file 'ouput/invitation_{i + 1}.txt': {e}")
