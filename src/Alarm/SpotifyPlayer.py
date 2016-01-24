import spotify
import time
import threading
import ConfigParser

"""
Class that plays music using spotify.

There should only be one instance of this class
"""
class SpotifyPlayer(object):

    def __init__(self):
    	self.username, self.password = self.read_userpass()

        self.session = spotify.Session()
        self.session.login(self.username, self.password, remember_me=True)

        print 'creating new spotifyplayer'

        # Process events in the background
        loop = spotify.EventLoop(self.session)
        loop.start()

        # Connect an audio sink
        audio = spotify.AlsaSink(self.session)

        # Events for coordination
        self.logged_in = threading.Event()
        self.end_of_track = threading.Event()

        # Register event listeners
        self.session.on(
            spotify.SessionEvent.CONNECTION_STATE_UPDATED, self.on_connection_state_updated)
        self.session.on(spotify.SessionEvent.END_OF_TRACK, self.on_end_of_track)

        # Wait for actual log on
        self.logged_in.wait()

    def read_userpass(self):
        config = ConfigParser.ConfigParser()
        config.read('spotify.config')
        return config.get('SpotifyLogin', 'username'), config.get('SpotifyLogin', 'password')

    # Functions needed for coordination of events
    def on_connection_state_updated(self, session):
        if self.session.connection.state is spotify.ConnectionState.LOGGED_IN:
            self.logged_in.set()

    def on_end_of_track(self):
        self.end_of_track.set()

    def stopPlaying(self):
        self.session.player.unload()

    # Play a track
    def play_track(self, track_uri):
        track = self.session.get_track(track_uri).load()
        self.session.player.unload()
        self.session.player.load(track)
        self.session.player.play()

    def isPlaying(self):
	return self.session.player.state == 'playing'