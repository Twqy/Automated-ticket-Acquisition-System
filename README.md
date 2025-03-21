# Automated-ticket-Acquisition-System

Automated Ticket Acquisition System
A Python-based automation tool that secures tickets for high-demand university events, specifically developed for the UWCSA St. Patrick's Day celebration.

Project Overview
This system addresses the challenge of acquiring tickets for popular campus events that typically sell out within seconds of going live. The script:

Automatically locates and selects tickets using dynamic element detection
Handles multi-user registration for up to 7 attendees simultaneously
Completes all required waiver forms and privacy confirmations
Processes checkout and payment information seamlessly
Reduces ticket acquisition time from minutes to seconds
Features
Dynamic Element Detection: Identifies ticket elements by scanning through a range of potential IDs, ensuring reliability even when website structure changes
Multi-User Registration: Automatically fills required information for up to 7 different attendees
Form Automation: Completes waiver acceptances and terms of service agreements without manual intervention
Payment Processing: Handles iframe navigation to securely submit payment details
Privacy Management: Automatically dismisses cookie/privacy popups that would otherwise interrupt the flow
Technical Implementation
The system utilizes:

Selenium WebDriver: For browser automation and element interaction
XPath Selectors: For robust element identification across website updates
Dynamic Waits: To handle website loading times
iFrame Navigation: For secure payment processing
Requirements
Python 3.6+
Google Chrome browser
Python packages:
selenium
webdriver-manager
How It Works
Ticket Location: The script uses a search algorithm to find the ticket selection elements by testing a range of potential IDs
Ticket Selection: Once found, it selects the specified number of tickets
Registration: For each attendee, it completes name, email, and waiver acceptance
Checkout Process: Fills billing information and navigates to payment
Payment Processing: Switches to the payment processor iframe and submits card details
Configuration
The script can be customized by modifying the following variables:

TICKET_COUNT: Number of tickets to purchase
User details (name, email, postal code)
Payment information
Usage Notes
The script is designed to run at the moment tickets become available
Test with TICKET_COUNT = 1 before attempting multi-ticket purchases
Update attendee information prior to use
For educational and personal use only
Disclaimer
This project was created for educational purposes to demonstrate web automation techniques. Users should ensure they comply with website terms of service and ticket purchasing policies.
