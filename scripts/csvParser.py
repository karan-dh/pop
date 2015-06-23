#!/bin/python

# This script reads ../structured-data/pop-appendix-b.csv
# and generates a json array containing objects with the 
# following schema:
# {
# 	mnemonic  	: string,
# 	name 		: string,
# 	opcode		: string,
# 	pop-index	: string,
#   inst-format : string
# }

# NOTE: ONLY MNEMONIC AND NAME ARE CORRECTLY PARSED

import csv
import json

# read the csv file containing the tabular appendix data in csv.
pop = open("../structured-data/pop-appendix-b.csv")
instructions = csv.reader(pop)

jsonInstructions = []

instructionFormats = [
"E",
"I",
"IE",
"MII",
"RI_a",
"RI_b",
"RI_c",
"RIE_a",
"RIE_b",
"RIE_c",
"RIE_d",
"RIE_e",
"RIE_f",
"RIE_g",
"RIL_a",
"RIL_b",
"RIL_c",
"RIS",
"RR",
"RRD",
"RRE",
"RRF_a",
"RRF_b",
"RRF_c",
"RRF_d",
"RRF_e",
"RRS",
"RS_a",
"RS_b",
"RSI",
"RSL_a",
"RSL_b",
"RSY_a",
"RSY_b",
"RX_a",
"RX_b",
"RXE",
"RXF",
"RXY_a",
"RXY_b",
"S",
"SI",
"SIL",
"SIY",
"SMI",
"SS_a",
"SS_b",
"SS_c",
"SS_d",
"SS_e",
"SS_f",
"SSE",
"SSF",
"VRI_a",
"VRI_b",
"VRI_c",
"VRI_d",
"VRI_e",
"VRR_a",
"VRR_b",
"VRR_c",
"VRR_d",
"VRR_e",
"VVR_f",
"VRS_a",
"VRS_b",
"VRS_c",
"VRV",
"VRX"]


# construct a json array with objects of the schema specified above.
for csvInstruction in instructions:
	jsonInstruction = {}
	jsonInstruction["mnemonic"] = csvInstruction[0]
	jsonInstruction["name"] 	= csvInstruction[1]
	jsonInstruction["inst-format"] = csvInstruction[2]

	popIndex = -1;

	# search the remaining strings containing '-', they can either
	# be instruction format or pop index.
	for i in range(len(csvInstruction)-1,3,-1):
		inst = csvInstruction[i]
		if "-" in inst:
			jsonInstruction["pop-index"] = inst
			popIndex = i
			break

	# seach for the opcode which is either popIndex-1 or popIndex-2:popIndex-1
	# TODO: maybe need a better algorithm for parsing the opcode.
	jsonInstruction["opcode"] = csvInstruction[popIndex-1]

	jsonInstructions.append(jsonInstruction)

# done processing pop.
pop.close()

# write the json data to file.
out = open("../structured-data/pop-appendix-b.json", "w")
out.write(json.dumps(jsonInstructions))
out.close()

# use the following command to add new line delimiters.
# sed -i 's/},/},\n/g' instructions.js

print "done!"