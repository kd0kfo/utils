
# Example Automake entry for version source generation
#
# This generates a source file, version.c, that will contain code for 
# version strings for software under git version control.
# For variable names, include version.h in source files that reference 
# the version strings.
version.c: 
	git rev-parse HEAD | awk ' BEGIN {print "#include \"version.h\""} {print "const char * build_git_sha = \"" $$0"\";"} END {}' > version.c
	date | awk 'BEGIN {} {print "const char * build_git_time = \""$$0"\";"} END {} ' >> version.c

.PHONY: version.c