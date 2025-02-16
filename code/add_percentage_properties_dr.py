import pandas as pd
import csv
import argparse

def compute_percentage(row, tot):

	output_string = str()
	output_string = str(round(int((row['count'])) / int(tot) * 100, 2)) + "%"

	#if we don't want any decimals, just replace the previous line with the following
	# output_string = str(int(int((row['count'])) / int(tot) * 100)) + "%"

	#if we want all decimals, just replace the previous line with the following
	# output_string = str(int((row['count'])) / int(tot) * 100) + "%"

	return output_string


def add_percentage_to_tsv(input_tsv, clas_tsv, clas):

	clas_df = pd.read_table(clas_tsv)
	#$OUTPUTPATH/output/classes.tsv

	input_df = pd.read_table(input_tsv)
	#../patterns/$CLASS/$CLASS-properties.tsv
	print(input_df['count'])

	input_df['percentage'] = input_df.apply(lambda row: compute_percentage(row, clas_df.loc[clas_df["class"] == clas, "count"].iloc[0]), axis=1)

	print(input_df)

	input_df.to_csv(input_tsv, sep='\t', quoting=csv.QUOTE_NONE, escapechar='\t', index=False)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	# Parameters
	parser.add_argument('--input_tsv', type=str, required=True)
	parser.add_argument('--clas_tsv', type=str, required=True)
	parser.add_argument('--clas', type=str, required=True)

	args = parser.parse_args()
    
	add_percentage_to_tsv(args.input_tsv, args.clas_tsv, args.clas)

#add_percentage_to_tsv("/Users/vale/Documents/PhD/Music_WIKIDATA/new_code_swj/Q482994-properties_90_17.tsv", "/Users/vale/Documents/PhD/Music_WIKIDATA/new_code_swj/classes_95_7.tsv", "Q482994")