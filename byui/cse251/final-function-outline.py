def breadth_fs_pedigree(family_id, tree:Tree):
    # KEEP this function even if you don't implement it
    # TODO - implement breadth first retrieval
    # TODO - Printing out people and families that are retrieved from the server will help debugging

    # Create an initial list for processing
    family_id_list = [family_id]
    while len(family_id_list):
        # Create a list for the next cycle
        next_family_id_list = []
        
        # Fetch data for all the families
        family_requests = []
        for family_id in family_id_list:
            family_requests.append() # Add new thread to list

        # Process API calls
        families_json = []
        for thread in family_requests:
            thread.start()
        for thread in family_requests:
            thread.join()
            # Dump resulting json into new list.
            families_json.append()
            # Add families to Tree
            if not tree.does_family_exist():
                tree.add_family()
        
        # Get data on family members
        families_member_requests = []
        # List of parents to check for next cycle
        parents = []
        # Iterate through the list of families
        for family in families_json:
            # Process for the father
            parents.append()
            families_member_requests.append() # Add new thread to list
            # Process for the mother
            parents.append()
            families_member_requests.append() # Add new thread to list
            # Process for the children
            for child in family["children"]:
                families_member_requests.append() # Add new thread to list
        
        # Handle request threads
        for thread in families_member_requests:
            thread.start()
        people_json = []
        for thread in families_member_requests:
            thread.join()
            # Send response data to a list
            people_json.append()

        # Add people into the tree data structure
        for person in people_json:
            # Add people to tree structure
            if not tree.does_person_exist():
                tree.add_person()
            # Check for more families to add for next cycle
            if person["id"] in parents: # Check if person is a known parent
                next_family_id_list.append()
        # Overwrite the list with our new list
        family_id_list = next_family_id_list
