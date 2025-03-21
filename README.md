# Automated-ticket-Acquisition-System

This project automates the process of acquiring tickets for events using Selenium WebDriver. It interacts with the event ticketing website to select tickets, fill out attendee details, and complete the checkout process.

## Features

- Automatically selects the desired number of tickets.
- Fills out attendee information and waivers.
- Completes the billing and payment process.
- Handles dynamic element IDs for ticket selection.

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python**: Version 3.7 or higher.
2. **Google Chrome**: Latest version.
3. **ChromeDriver**: Managed automatically by `webdriver-manager`.

Install the required Python packages using:

```bash
pip install selenium webdriver-manager
