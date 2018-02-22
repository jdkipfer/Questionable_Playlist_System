# Questionable Playlist System
The questionable playlist system is an algorithm that I use to listen to new albums on Google Play Music.
At a certain point I realized it was probably easier to automate it instead of always doing it manually, so his is what that is.

[Here's an explanation of how it works](https://github.com/jdkipfer/Questionable_Playlist_System/blob/master/Explanation.md)

To use this, you'll need [Python](https://www.python.org/downloads/) and [gmusicapi](https://unofficial-google-music-api.readthedocs.io/en/latest/), an unnoficial API for Google Play Music

You will need to enter your username and password into the top of the program where this is indicated.
Once this is done, run the program. The program has to claim it is one of your devices, and the error message that this will produce gives a list of your possible device IDs. Add one of them to the location prompted next to the login information.

I find it helpful to have an actual playlist to keep track of what is in the system, but the program actually pulls from hardcoded names of artists and albums. The reason for this is that if the song information is pulled from playlists in Google Play Music itself, only songs uploaded, not store tracks will have the information needed to run the process.

Write the artist and album names for the 7FAST and 7SLOW playlists where indicated.

All albums used must be added to the user's library.

When ran, the day lists for 7FAST and 7SLOW should be created.
