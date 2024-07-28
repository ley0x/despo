## Blind SQL Injection Exploitation Script


This script is designed to exploit blind SQL injection vulnerabilities in web applications.

### Features

*   Exploits blind SQL injection vulnerabilities
*   Exfiltrates data from a database
*   Customizable injection points and payloads

### Usage

1.  Clone the repository: `git clone https://github.com/ley0x/despo.git`
2.  Install the required dependencies: `pip install -r requirements.txt`
3.  Configure the script by modifying the following variables:
    *   `charset`: The character set to use for exfiltration
    *   `METHOD`: The HTTP method to use (GET, POST, etc.)
    *   `url`: The URL of the vulnerable web application
    *   `endpoint`: The endpoint to target
    *   `params`: The URL parameters to include
    *   `data`: The request body data
    *   `cookies`: The cookies to include
    *   `headers`: The headers to include
    *   `verbose`: Prints the log in the console
4.  Choose the injection point and payload
4.  Run the script: `python3 despo.py`

### Configuration

The script can be configured by modifying the following variables:

*   `charset`: The character set to use for exfiltration (default: "0123456789abcdefghijklmnopqrstuvwxyz")
*   `METHOD`: The HTTP method to use (default: "GET")
*   `url`: The URL of the vulnerable web application (default: "https://example.com")
*   `endpoint`: The endpoint to target (default: "/fake")
*   `params`: The URL parameters to include (default: {})
*   `data`: The request body data (default: {})
*   `cookies`: The cookies to include (default: {})
*   `headers`: The headers to include (default: { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" })

Check them easily by searching for `TODO` in the code.

License
-------

This script is released under the MIT License.

Contributing
------------

Contributions are welcome! If you have any ideas or improvements, please submit a pull request.

Acknowledgments
---------------

This script was inspired by the work of [Your Name] and the [Your Project] project.

Disclaimer
----------

This script is for educational purposes only. It should not be used for malicious purposes.
