from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route('/text_detector', methods=['POST'])
def detect_text():

    data = request.get_json()
    image_text = data['textAnnotations'][0]['description']

    nf_number = get_nf(image_text)
    nf_value = get_nf_value(image_text)
    nf_verif_code = get_ver_code(image_text)

    response = {
        'nfNumber' : nf_number,
        'value' : nf_value,
        'verificationCode' : nf_verif_code
    }
    
    return jsonify(response), 200

def get_nf(text):
    nf = ''

    content = text.replace(' ', '').replace('\n', '')
    x = content.lower().find('nota')

    for i in range(x, len(content)):
        if content[i] in '0123456789':
            nf += content[i]
            if not content[i+1] in '0123456789':
                break
        else:
            continue
    return nf

def get_nf_value(text):
    nf_value = ''

    content = text.replace(' ', '').replace('\n', '')
    x = content.lower().find('valortotal')

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
    magic_word = 'verificação'
    verif_code_len = 9

    content = text.replace('\n', '')
    x = content.lower().find(magic_word)
    
    for i in range(x + len(magic_word), len(content)):
        if content[i].isalpha():
            nf_verif_code = content[i: i+verif_code_len]
            break
            
          
    return nf_verif_code

    

if __name__ == '__main__':
    if os.environ.get('GAE_ENV') != 'standard':
        app.run(host='127.0.0.1', port=8080, debug=True)