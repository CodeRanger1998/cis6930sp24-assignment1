import argparse
import glob
import os
import assignment1.nlp as nlp  # Import custom NLP module
import sys

# Function to censor sensitive information in the text
def censor_text(text, stats, censor_names=True, censor_dates=True, censor_phones=True, censor_address=True):
    # Get document from the text using the custom NLP module
    doc = nlp.getDocFromText(text=text)
    statString = ''
    if censor_names:
        # Redact names from the text and get the redaction statistics
        text, namestat = nlp.redactNames(text=text, doc=doc)
        statString = statString + '\nNumber of Names redacted: ' + str(namestat)

    if censor_dates:
        # Redact dates from the text and get the redaction statistics
        text, datestat = nlp.redactDates(text=text, doc=doc)
        statString = statString + '\nNumber of Dates redacted: ' + str(datestat)

    if censor_phones:
        # Redact phone numbers from the text and get the redaction statistics
        text, phonestat = nlp.redactPhones(text=text)
        statString = statString + '\nNumber of Phones redacted: ' + str(phonestat)

    if censor_address:
        # Redact addresses from the text and get the redaction statistics
        text, addressStat = nlp.redactAddresses(text=text,doc=doc)
        statString = statString + '\nNumber of Addresses redacted: ' + str(addressStat)

    return text, statString

# Function to censor files based on specified patterns
def censor_files(input_pattern, output_dir, stats, censor_names=True, censor_dates=True, censor_phones=True, censor_address=True):
    # Get list of files based on input pattern
    files = glob.glob(input_pattern)
    statStringFinal = ''
    # Process each file
    for file_path in files:
        with open(file_path, 'r') as f:
            text = f.read()

        # Censor sensitive information in the text
        censored_text, fileStatString = censor_text(text, stats, censor_names, censor_dates, censor_phones, censor_address)
        # Write censored text to new file with .censored extension
        output_path = os.path.join(output_dir, os.path.basename(file_path) + '.censored')
        with open(output_path, 'w', encoding="utf-8") as f:
            f.write(censored_text)
        # Aggregate statistics for all files
        if stats is not None:
            statStringFinal = statStringFinal + '\nFile Name:' + os.path.basename(file_path) + fileStatString
    # Print or write statistics based on specified output
    if stats == 'stderr':
        print(statStringFinal, file=sys.stderr)
    elif stats == 'stdout':
        print(statStringFinal, file=sys.stdout)
    else:
        stat_path = os.path.join(output_dir, 'stats.txt')
        with open(stat_path, 'w') as f:
            f.write(statStringFinal)

# Main function to parse arguments and execute censoring process
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
        # Create output directory if it doesn't exist
        if not os.path.exists(args.output.replace("'", "")):
            os.makedirs(args.output.replace("'", ""))
        # Call censor_files function to process files
        censor_files(input_pattern.replace("'", ""), args.output.replace("'", ""), args.stats, args.names, args.dates,
                     args.phones, args.address)

if __name__ == "__main__":
    main()