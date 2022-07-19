#########################Ze most important function of all newbie functions
#########################GetMetadataFunction



def getmetadataforsoros():
    """Gets metadata for soros"""
    username = input("Who are you?. . ._ ")
    userage = input("ok "+ username + " how old are you?_ ")
    return (username,userage)

def weWEHAVEYOURMETADATA(playerdata):
    """prints real some real talk"""
    print("\nSee you next time", playerdata[0], "who is", playerdata[1], "years old...\nwe now have your 💩💩💩💩💩 Metadata and sell it to:\n\n💩 Facebook\n💩 Soros\n💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩")
    return "💩"


#The program assumes you know that the getdataforsoros function has to be computed and assigned to a variable, this besaid variable is then later used by the
#weWENOWHAVEYOURMETADATA function to print out players metadata 
##for testing try:
player=getmetadataforsoros()
print(weWEHAVEYOURMETADATA(player))
