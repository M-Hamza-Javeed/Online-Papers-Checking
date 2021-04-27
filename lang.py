import language_check
tool = language_check.LanguageTool('en-US')
i = 0

fin=["how to identify the, nalyze their structure, assign assign them to lexical categories, and access their meanings",
    "how to identify the, nalyze their structure, assign assign them to lexical categories, and access their meanings",
    "how to identify the, analyze their their structure,  assign them to lexical categories, and access their meanings",
    "how to identify the, analyze their structure, assign them to lexical categories, and access their meanings"]


correct=[]
errors=[]

for line in fin:
    matches = tool.check(line);
    i=i+len(matches)
    for mistake in matches:
        error = mistake.context[mistake.contextoffset:mistake.contextoffset+mistake.errorlength]
        replacer = mistake.replacements[0]
        line=(line.replace(error,replacer))
        errors.append(mistake.category)
    correct.append(line)
    
    
print({"correct":correct,"len":len(correct),"error":i,"errortypes":list(set(errors))})