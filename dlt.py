import argparse, deepl, os, sys

version = 0.2.1

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--translate", metavar = "", help = "Text to be translated.")
parser.add_argument("-il", "--inputlang", metavar = "", help = "Defines the language of the input (Default = 'EN'), only needed if the default (Detect language) is tweeking.")
parser.add_argument("-ol", "--outputlang", metavar = "", help = "Defines the language that the input should be returned in (Defualt = 'DE').")
parser.add_argument("-f", "--formality", metavar = "", help = "Defines the formality of the output: default, more, less, prefer_more, prefer_less.")
parser.add_argument("-sbc", "--show_billed_characters", metavar = "", help = "Toggles the 'billed_characters' extension of the output.'")
parser.add_argument("-pf", "--preserve_formatting", metavar = "", help = "Toggles the 'preserve_formatting' setting of the output.")
args = parser.parse_args()

auth_key = os.getenv("deeplapikey")
deepl_client = deepl.DeepLClient(auth_key)

inputlang = "EN"
outputlang = "DE"
formality = "default"
sbc = "true"
pf = "false"

if args.translate:
    cli()
else:
    main()

def cli():
    x = translate(args.translate, inputlang, outputlang, formality, sbc, pf)
    output(x)

def translate(text, inputlang, outputlang, formality, sbc, pf):
# text = array[string]
# source_lang = string
# target_lang = string
# formality = string:     
#    default (default)
#    more - for a more formal language
#    less - for a more informal language
#    prefer_more - for a more formal language if available, otherwise fallback to default formality
#    prefer_less - for a more informal language if available, otherwise fallback to default formality
#[REMOVED FROM INPUT] show_billed_characters = boolean:
#                       returns: "billed_characters":int
# preserve_formatting = boolean:
#    Punctuation at the beginning and end of the sentence
#    Upper/lower case at the beginning of the sentence

    result = deepl_client.translate_text(text = text,source_lang = inputlang ,target_lang = outputlang, formality = formality, preserve_formatting = pf)
    return result

def output(x):
    print(x)

def main():
    os.system("clear")



