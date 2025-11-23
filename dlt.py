import argparse, deepl, os, sys, configparser
from pathlib import Path

version = "0.3.2"

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--translate", metavar = "", help = "Text to be translated.")
parser.add_argument("-doc", "--document", metavar = "", help = "Document to be translated.")
parser.add_argument("-il", "--inputlang", metavar = "", help = "Defines the language of the input, only needed if the default (Detect language) is tweeking.")
parser.add_argument("-ol", "--outputlang", metavar = "", help = "Defines the language that the input should be returned in.")
parser.add_argument("-f", "--formality", metavar = "", help = "Defines the formality of the output: default, more, less, prefer_more, prefer_less.")
parser.add_argument("-sbc", "--show_billed_characters", metavar = "", help = "Toggles the 'billed_characters' extension of the output.")
parser.add_argument("-pf", "--preserve_formatting", metavar = "", help = "Toggles the 'preserve_formatting' setting of the output.")
parser.add_argument("-v", "--verbose", metavar = "", help = "Toggles the 'verbose' setting of the application.")
parser.add_argument("-c", "--config", action = "store_true", help = "Prints the contense of the programs configuration and exits.")
parser.add_argument("-V", "--version", action = "version", version=version, help = "Prints the application version and exits.")
parser.add_argument("-sa", "--set_api", metavar = "", help = "Sets your DeepL API key.")
parser.add_argument("-H", "--history", metavar = "", help = "Toggles the translation history / caching of the application.")
parser.add_argument("-C", "--colours", metavar = "", help = "Toggles the colours of the application.")
args = parser.parse_args()

loaded_settings = {
        "inputlang": "EN",
        "outputlang": "DE",
        "formality": "default",
        "sbc": "true",
        "pf": "false",
        "verbose": "false",
        "APIkey": "PLACEHOLDER"
        }

cfgpath = Path.home() / ".config" / "dlt" / "config.ini"
cfgparser = configparser.ConfigParser()

def checkConfig():
    if cfgpath.exists():
        return
    else:
        makeConfig()

def makeConfig():
    Path(cfgpath).parent.mkdir(parents = True, exist_ok = True)
    Path(cfgpath).touch(exist_ok = True)
    writeDefaultConfig()

def writeDefaultConfig():
    cfgparser["CONFIG"] = {
            "APIkey": "Not set",
            "verbose": "false",
            "sbc": "true"
            }
    cfgparser["TEXT CONFIG"] = {
            "inputlang": "EN",
            "outputlang": "DE",
            "formality": "default",
            "pf": "false"
            }

    with cfgpath.open("w") as cfg:
        cfgparser.write(cfg)

def updateConfig(section, key, value):
    cfgparser[section][key] = value

    with path.open("w") as cfg:
        cfgparser.write(cfg)

def printConfig():
    cfgparser.read(cfgpath)
    
    for section in cfgparser.sections():
        print(f"[{section}]")
        for key, value in cfgparser[section].items():
            print(f"{key} = {value}")
        print()

def loadConfig():
    cfgparser.read(cfgpath)

    for section in cfg.sections():
        for key, value in cfg[section].items():
            if key in loaded_settings:
                settings[key] = value

def cli():
    checkConfig()

    if args.config:
        printConfig()

    if args.set_api:
        updateConfig("CONFIG", APIkey, args.set_api)
    
    if args.inputlang:
        updateConfig("TEXT CONFIG", inputlang, args.inputlang)

    if args.outputlang:
        updateConfig("TEXT CONFIG", outputlang, args.outputlang)

    if args.formality:
        updateConfig("TEXT CONFIG", formality, args.formality)

    if args.show_billed_characters:
        updateConfig("CONFIG", sbc, args.show_billed_characters)

    if args.preserve_formatting:
        updateConfig("TEXT CONFIG", pf, args.preserve_formatting)

    if args.verbose:
        updateConfig("TEXT CONFIG", verbose, args.verbose)

    if args.translate:
        loadConfig()
        x = translate(args.translate, loaded_setting["inputlang"], loaded_setting["outputlang"], loaded_setting["formality"], loaded_setting["sbc"],loaded_setting["pf"])
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
    auth_key = loaded_settigns[APIkey]
    deepl_client = deepl.DeepLClient(auth_key)
    result = deepl_client.translate_text(text = text,source_lang = inputlang ,target_lang = outputlang, formality = formality, preserve_formatting = pf)
    return result

def output(x):
    print(x)

def main():
    checkConfig()
    os.system("clear")
    sys.exit()

if __name__ == "__main__":
    if any(vars(args).values()):
        cli()
    else:
        main()
