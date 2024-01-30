while True:
    champion_name = input("Enter the champion's name: ")
    role = input("Enter the role: ")

    # Read the links from the text file
    with open('output.txt', 'r') as f:
        champion_links = [line.strip() for line in f]

    # Filter the links to find the counters for the specified champion and role
    counter_links = [link for link in champion_links if champion_name.lower() in link and role.lower() in link and 'counters' in link]

    # If no counters are found, print an error and ask for input again
    if not counter_links:
        print(f"No counters found for {champion_name} ({role}). Please try again.")
        continue

    # Extract the counter champions from the links
    counter_champions = [link.split('=')[-1] for link in counter_links if link.split('=')[-1].lower() != champion_name.lower()]

    # Print the counter champions
    print(f'Here are the counter champions for {champion_name} ({role}):') 
    for counter in counter_champions:
        print(counter)
    break