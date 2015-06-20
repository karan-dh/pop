#!/bin/python

# This script reads ../structured-data/pop-appendix-b.csv
# and generates a json array containing objects with the 
# following schema:
# {
# 	mnemonic  	: string,
# 	name 		: string,
# 	opcode		: string,
# 	pop-index	: string,
# }

# NOTE: ONLY MNEMONIC AND NAME ARE CORRECTLY PARSED

import csv
import json

# read the csv file containing the tabular appendix data in csv.
pop = open("../structured-data/pop-appendix-b.csv")
instructions = csv.reader(pop)

jsonInstructions = []

# construct a json array with objects of the schema specified above.
for csvInstruction in instructions:
	jsonInstruction = {}
	jsonInstruction["mnemonic"] = csvInstruction[0]
	jsonInstruction["name"] 	= csvInstruction[1]
	jsonInstruction["opcode"] 	= csvInstruction[12]
	jsonInstruction["pop-index"] = csvInstruction[13]
	jsonInstructions.append(jsonInstruction)

# done processing pop.
pop.close()

# write the json data to file.
out = open("../structured-data/pop-appendix-b.json", "w")
out.write(json.dumps(jsonInstructions))
out.close()

# use the following command to add new line delimiters.
# sed -i 's/},/|,\n/g' instructions.js

print "done!"