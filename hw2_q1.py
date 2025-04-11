MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
    with open(input_file, "r") as f:
        text = f.read()
        text = text.upper()

        paragraphs = text.split('\n\n')
    morse_paragraphs = []
    
    for paragraph in paragraphs:
        words = paragraph.split()
        morse_words = []
        
        for word in words:
            morse_chars = [MORSE_CODE.get(char, '') for char in word if char in MORSE_CODE]
            morse_word = ''.join(morse_chars)
            if morse_word:
                morse_words.append(morse_word)
        
        morse_paragraphs.append('\n'.join(morse_words))
    
    result = '\n\n'.join(morse_paragraphs)
    
    with open(output_file, "w") as f:
        f.write(result)



if __name__ == '__main__':
    english_to_morse() 
