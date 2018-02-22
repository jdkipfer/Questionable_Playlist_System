'''
Created on Jan 18, 2018

@author: Joel
'''

from gmusicapi import Mobileclient
from gmusicapi.utils import utils
api = Mobileclient()

print("This line will be printed.")
logged_in = api.login('User Name', 'Password', 'Device Id', 'ICU Locale')
#[artist name, album name, song id, isthumbsup, tracks to ignore]
slow=[['Artist 1', 'Album 1', 0,False,[]],
      ['Artist 2', 'Album 2', 0,False,[]],
      ['Artist 3', 'Album 3', 0,False,[]]]
fast=[['Artist 4', 'Album 4', 0,False,[]],
      ['Artist 5', 'Album 5', 0,False,[]],
      ['Artist 6', 'Album 6', 0,False,[]]]
#auth=Mobileclient.is_authenticated()
if (logged_in)==True:
    print("Log In Successful")
songsTooBig =api.get_all_songs(incremental=False, include_deleted=None, updated_after=None)
#print(len(songs))
print("Song data recieved")
fastId=api.create_playlist('dayFASTList', description=None, public=False)
slowId=api.create_playlist('daySLOWList', description=None, public=False)
songs=[]
for song in songsTooBig:
    #print(song['rating'])
    yes=False
    try:
        if song['playCount']<7:
            yes=True
        else:
            yes=False
    except:
        song['playCount']=0
        yes=True
    if yes:
        try:
            #if (song['rating']=='1'):
            #    print (song['title'])
            
            if song['rating']=='5' or song['rating']=='0':
                
                songs.append(song)
        except:
            song['title']=song['title'].encode("utf-8")
            song['artist']=song['artist'].encode("utf-8")
            song['album']=song['album'].encode("utf-8")
            song['title']=song['title'].decode("utf-8")
            song['artist']=song['artist'].decode("utf-8")
            song['album']=song['album'].decode("utf-8")
            song['rating']='0'
            songs.append(song)

for i in range(0,7):
    print(i)
    for f in fast:
        f[2]=0
        f[3]=False
    for s in slow:
        s[2]=0
        s[3]=False
    for song in songs:
        for f in fast:
            if f[3]==False:
                try:
                    if (f[2]==0 or (f[3]==False and song['rating']=='5')):
                        #if (((song['artist']==f[0] and song['album']==f[1]) or song['album']=='The ArchAndroid') and song['playCount']==i):
                        if ((song['album']==f[1]) and song['playCount']==i):
                            bad=False
                            for title in f[4]:
                                if title==song['title']:
                                    bad=True
                            if bad==False:        
                                f[2]=song['id']
                                if song['rating']=='5':
                                    f[3]=True
                                print (song['artist'])
                    
                except:
                    if (song['artist']==f[0] and song['album']==f[1] and song['playCount']==i and f[2]==0):
                        f[2]=song['id']
                        print('happen')
                    pass
        for f in slow:       
            if f[3]==False:
                try:
                    if (f[2]==0 or (f[3]==False and song['rating']=='5')):
                        if (song['artist']==f[0] and song['album']==f[1] and song['playCount']==i):
                            bad=False
                            for title in f[4]:
                                if title==song['title']:
                                    bad=True
                            if bad==False:        
                                f[2]=song['id']
                                if song['rating']=='5':
                                    f[3]=True
                                print (song['artist'])
                except:
                    if (song['artist']==f[0] and song['album']==f[1] and song['playCount']==i and f[2]==0):
                        f[2]=song['id']
                        print('happen')
                    pass
    for f in fast:
        if f[2]!=0:
            api.add_songs_to_playlist(fastId, f[2])
    for f in slow:
        if f[2]!=0:
            api.add_songs_to_playlist(slowId, f[2])
          

print("This line will be printed.")

if __name__ == '__main__':
    pass
