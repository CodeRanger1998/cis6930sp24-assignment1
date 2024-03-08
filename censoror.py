import argparse
import glob
import os
import assignment1.nlp as nlp
import sys



def censor_text(text,stats,censor_names=True, censor_dates=True, censor_phones=True, censor_address=True):
    doc = nlp.getDocFromText(text=text)
    statString = ''
    if censor_names:
        # Implement logic to censor names
        text,namestat = nlp.redactNames(text=text,doc=doc)
        statString = statString + '\nNumber of Names redacted: '+str(namestat)
    
    if censor_dates:
        # Implement logic to censor dates
        text,datestat = nlp.redactDates(text=text,doc=doc)
        statString = statString + '\nNumber of Dates redacted: '+str(datestat)
    
    if censor_phones:
        # Implement logic to censor phone numbers
        text,phonestat = nlp.redactPhones(text=text)
        statString = statString + '\nNumber of Phones redacted: '+str(phonestat)
    
    if censor_address:
        # Implement logic to censor addresses
        text,addressStat = nlp.redactAddresses(text=text)
        statString = statString + '\nNumber of Addresses redacted: '+str(addressStat)
    
    return text,statString

def censor_files(input_pattern, output_dir,stats, censor_names=True, censor_dates=True, censor_phones=True, censor_address=True):
    files = glob.glob(input_pattern)
    statStringFinal = ''
    for file_path in files:
        with open(file_path, 'r') as f:
            text = f.read()
        
        censored_text,fileStatString = censor_text(text,stats, censor_names, censor_dates, censor_phones, censor_address)
        output_path = os.path.join(output_dir, os.path.basename(file_path) + '.censored')
        with open(output_path, 'w') as f:
            f.write(censored_text)
        if stats != None:
            statStringFinal = statStringFinal + '\nFile Name:' + os.path.basename(file_path)+fileStatString
    if stats == 'stderr':
        print(statStringFinal,file=sys.stderr)
    elif stats == 'stdout':
        print(statStringFinal,file=sys.stdout)
    else:
        stat_path = os.path.join(output_dir, 'stats.txt')
        with open(stat_path, 'w') as f:
            f.write(statStringFinal)
        


def main():
    parser = argparse.ArgumentParser(description='Censor sensitive information in text documents')
    parser.add_argument('--input', nargs='+', help='Input file pattern(s)', required=True)
    parser.add_argument('--output', help='Output directory', required=True)
    parser.add_argument('--names', action='store_true', help='Censor names')
    parser.add_argument('--dates', action='store_true', help='Censor dates')
    parser.add_argument('--phones', action='store_true', help='Censor phone numbers')
    parser.add_argument('--address', action='store_true', help='Censor addresses')
    parser.add_argument('--stats', help='censor statistics')
    args = parser.parse_args()
    for input_pattern in args.input:
        if not os.path.exists(args.output.replace("'","")):
            os.makedirs(args.output.replace("'",""))
        censor_files(input_pattern.replace("'",""), args.output.replace("'",""),args.stats, args.names, args.dates, args.phones, args.address)

if __name__ == "__main__":
    main()