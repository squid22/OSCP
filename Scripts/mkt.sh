# This will create directories and swithch to that location.
# Example:
# mkt BoxName
#
# The results 
# BoxName/content
# Boxname/exploits
# BoxName/scans
# BoxName/scripts
# BoxName/tmp

mkt () {
        mkdir -p $1/{scans,content,exploits,scripts,tmp} && cd $1
}
