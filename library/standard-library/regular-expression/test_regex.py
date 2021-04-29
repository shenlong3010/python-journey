import re

"""
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub		Replaces one or many matches with a string

[]	A set of characters	"[a-m]"	
\   Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"	
()	Capture and group	 
"""
def test1():
	txt = "The rain in Spain"
	#Check if the string starts with "The" and ends with "Spain":
	x = re.search("^The.*Spain$", txt)
	print("YES! We have a match!") if x else print("No match")

# Using re.search()
s = "Now I know my ABC"
re.search("I", s)
re.search('[A-Z][A-Z][A-Z]',s)

text = 'The flight AAZ-1406 has landed at 4am, \
		flight CVV-1223 at 6am, \
		flight WWE-3342 at 8am, \
		flight QAD-9987 at 10am and \
		flight RRU-4437 at 1pm.'
re.findall(r'\b[0-9]{4}\s', text)