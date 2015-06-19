// global namespace pop
var pop = pop || {};

// index into instructions based on opcode.
pop.index = {};

pop.InstructionFieldEnum = {
	"MNEMONIC" 	: 1,
	"NAME"		: 2,
	"OPCODE" 	: 3,
	"POP-INDEX" : 4
}

pop.InstructionKeys = {
	1 : "mnemonic",
	2 : "name",
	3 : "opcode",
	4 : "pop-index"
}

// build an index based on the key (pop.InstructionFieldEnum)
pop.buildIndex = function(key) {

	pop.index[key] = {};
	instKey = pop.InstructionKeys[key]

	for (var i = 0; i < instructions.length; i++) {
		inst = instructions[i];
		pop.index[key][inst[instKey]] = i;
	}

}

// returns the relevant insturction given a query string
// and the index field key (pop.InstructionFieldEnum)
pop.findInstruction = function(key, query) {
	instIndex = pop.index[key][query]
	if (instIndex == undefined) 
		return ""

	return JSON.stringify(instructions[instIndex])
}