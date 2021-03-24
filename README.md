# NF-Reader (Challenge-Backend-Developer)

This API receives a JSON with the text of a "Nota Fiscal"(NF) and returns:
* NF Number
* NF Value
* NF Verification Code

## Getting Started

To run this API you will need python 3.6.9 or latest and Flask 1.1.2 or latest

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

  For other Linux flavors, macOS and Windows, packages are available at

     https://www.python.org/getit/
  
For Flask installation and update use pip:

    $ pip install -U Flask



## Running the tests

To obtain the JSON with the NF text:

* Go To the [VISION API](https://cloud.google.com/vision) site
* Upload your NF image in the **"Try the API"** section
* Then click on **Show JSON** and copy the **"Response"** section
* Now you can send this JSON to the API in a **POST Request**


