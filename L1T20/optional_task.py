# Create a dictionary containing some abbreviations and their meanings
abbreviations = {
    "ASDL": "Asymmetric Digital Subscriber Line",
    "CDMA": "Code Division Multiple Access",
    "GSM": "Global System for Mobile Communications",
    "LTE": "Long-Term Evolution"
}

# Add 2 more abbreviations and their meanings to the dictionary
abbreviations["5G"] = "Fifth Generation"
abbreviations["WiFi"] = "Wireless Fidelity"

# Ask the user to enter an abbreviation
abbr = input("Enter an abbreviation: ")

# Check if the abbreviation is in the dictionary
if abbr in abbreviations:
    print(abbr + ": " + abbreviations[abbr])
else:
    print("Abbreviation not found")
