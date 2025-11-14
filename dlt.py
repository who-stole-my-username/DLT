import argparse, deepl, os, sys

version = 0.1

parser = argparse.ArgumentParser()
parser.add_argument("translate")
args = parser.parse_args()

auth_key = os.getenv("deeplapikey")
deepl_client = deepl.DeepLClient(auth_key)

inputlang = "EN"
outputlang = "DE"
formality = "default"
sbc = "true"
pf = "false"



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
# show_billed_characters = boolean:
#    returns: "billed_characters":int
# preserve_formatting = boolean:
#    Punctuation at the beginning and end of the sentence
#    Upper/lower case at the beginning of the sentence

    result = deepl_client.translate_text(text = text,source_lang = inputlang ,target_lang = outputlang, formality = formality, preserve_formatting = pf)
    return result

def output(x):
    print(x)

def main():
    os.system("clear")



x = (translate(args.translate, inputlang, outputlang, formality, sbc, pf))
print(x)
print(x.billed_characters)
