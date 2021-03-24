from flask import Flask, jsonify, request
import os

app = Flask(__name__)

#principal function that gets the complete text of the image
@app.route('/text-detector', methods=['POST'])
def detect_text():
    #image text is received as a json
    data = request.get_json()
    try:
        #text ubication in the json
        image_text = data['textAnnotations'][0]['description']
    except:
    #response if there is an error with the JSON on the request
    #For example if you write 'descruption' instead of 'description'
        error_response = {
            'message' : 'There is something wrong with your JSON'
        }
        return jsonify(error_response), 400 


    nf_number = get_nf(image_text)
    nf_value = get_nf_value(image_text)
    nf_verif_code = get_ver_code(image_text)

    response = {
        'nfNumber' : nf_number,
        'value' : nf_value,
        'verificationCode' : nf_verif_code
    }

    #returns a json with the info requested
    return jsonify(response), 200

def get_nf(text):
    nf = ''
    #the first time that 'nota' is mentioned in the NF is in the number
    word_to_find = 'nota'
    #I clean spaces and newline jumps 
    content = text.replace(' ', '').replace('\n', '')
    #lower the string to secure our search of 'word_to_find'
    x = content.lower().find(word_to_find)

    #nfNumber contains only digits everytime, so we need to filter that
    for i in range(x, len(content)):
        if content[i].isdigit():
            nf += content[i]
            if not content[i+1].isdigit():
                break
        else:
            continue
    return nf

def get_nf_value(text):
    nf_value = ''

    word_to_find = 'valortotal'

    content = text.replace(' ', '').replace('\n', '')
    x = content.lower().find(word_to_find)

    #nfValue contains a '.' or ',' to separate decimals, 
    #that is why I include these symbols to the filter
    for i in range(x, len(content)):
        if content[i] in '.,0123456789':
            nf_value += content[i]
            if not content[i+1] in '.,0123456789':
                break
        else:
            continue
        
            
    return nf_value

def get_ver_code(text):
    nf_verif_code = ''
    word_to_find = 'verificação'
    #verification code size is always 9
    verif_code_len = 9

    content = text.replace('\n', '')
    x = content.lower().find(word_to_find)
    
    #verification code contains numbers and letters
    #and it comes after a long digit with variable size.
    #that is why I filter it and get only the needed code
    for i in range(x + len(word_to_find), len(content)):
        if content[i].isalpha():
            nf_verif_code = content[i: i+verif_code_len]
            break
            
          
    return nf_verif_code

    

if __name__ == '__main__':
    if os.environ.get('GAE_ENV') != 'standard':
        app.run(host='127.0.0.1', port=8080, debug=True)