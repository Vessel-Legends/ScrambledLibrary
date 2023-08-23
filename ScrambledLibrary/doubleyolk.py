from googletrans import Translator
import time, threading, threading, sys, os, itertools
translator = Translator()
def scramble(word: str, output_to_file: bool):
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write("\rScrambling... " + c)
            sys.stdout.flush()
            time.sleep(0.1)
        os.system("cls")
    '''
    ## Scramble a word using the DoubleYolk scramble method.
    ---
    word: The word you want to scramble.
    output_to_file: Weither to output the result to a file, or just print it to the console.
    ---
    Returns: A string with the output (if output_to_file is False), or a file with the original sentence and the scrambled one (if output_to_file is True).
    '''
    t = threading.Thread(target=animate)
    t.start()
    masstrans = translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(translator.translate(word, dest="af").text, dest="ht").text, dest="ha").text, dest="haw").text, dest="iw").text, dest="hi").text, dest="hmn").text, dest="hu").text, dest="is").text, dest="ig").text, dest="id").text, dest="ga").text, dest="it").text, dest="ja").text, dest="jw").text, dest="en").text
    done = True
    if output_to_file == True:
        with open("scrambled-doubelyolk.txt", 'w', encoding='utf-8') as f:
            f.write(f"Original sentence:\n{word}\n\nScrambled sentence:\n{str(masstrans)}")
            f.close()
    else:
        print(f"Original sentence:\n{word}\n\nScrambled sentence:\n{str(masstrans)}")
        time.sleep(10)
    return str(masstrans)