# Octave code to segment out the instruction formats.

files = cell(5,1);
files{1} = '../raw/instruction-formats-1.png';
files{2} = '../raw/instruction-formats-2.png';
files{3} = '../raw/instruction-formats-3.png';
files{4} = '../raw/instruction-formats-4.png';
files{5} = '../raw/instruction-formats-5.png';

for j=1:5,
	ifs = imread(files{j});

	# convert the image to b/w.
	bw = sum(ifs,3);
	c  = max(max(bw));
	bw = ceil(abs((bw-c))./c);

	# compute row and colums sums.
	rSums = sum(bw,2);
	cSums = sum(bw,1);

	# compute row and column median points.
	rMedians = [];
	cMedians = [];

	current = 0; # current sum.
	record  = 0; 
	n       = 0; # number of points in current cluster.

	for i=1:length(rSums)
		if rSums(i) == 0,
			current = current + i;
			n = n + 1;

			if n > 5,
				record = 1;
			end

		else
			if record == 1,
				current = current/n;
				rMedians = [rMedians, current];
				record = 0;
			end

			current = 0;
			n = 0;
		end
	end

	if record == 1,
		current = current/n;
		rMedians = [rMedians, current];
	end

	current = 0; 
	record  = 0; 
	n       = 0; 

	for i=1:length(cSums)
		if cSums(i) == 0,
			current = current + i;
			n = n + 1;

			if n > 10,
				record = 1;
			end

		else
			if record == 1,
				current = current/n;
				cMedians = [cMedians, current];
				record = 0;
			end

			current = 0;
			n = 0;
		end
	end

	if record == 1,
		current = current/n;
		cMedians = [cMedians, current];
	end

	k = 0;

	# crop the image sections and write to file.
	for a=[1:2:(length(cMedians)-1)]
		for b=[1:2:(length(rMedians)-1)]
			k = k + 1
			c1 = round(cMedians(a));
			c2 = round(cMedians(a+1));

			r1 = round(rMedians(b));
			r2 = round(rMedians(b+1));

			imwrite(ifs(r1:r2,c1:c2), sprintf('%d-%d-format.png', j, k));

		end
	end
end

fprintf('done!');