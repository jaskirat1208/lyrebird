for f in $(ls tests/*.txt); do
	echo "Processing $f"
	python simulation.py 50 < $f

done