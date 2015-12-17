# ub-comp
This repositoy is part of a project for the course [Ubiquitous Computing ](https://www.rug.nl/ocasys/ucg/vak/show?code=INMUBC-09) of the University of Groningen. Keep in mind that nothing, such as documentation or even working code, is guaranteed

## Installation

### Spotify
To use the spotify API, you need to have libspotify and pyspotify. At the moment there is no fallback for if there is no libspotify and pyspotify installed.

Installation of libspotify can be done via [repositories](https://pyspotify.mopidy.com/en/latest/installation/#debian-ubuntu) or via [https://developer.spotify.com/technologies/libspotify/](manual installation). Please note that this library is official deprecated, however no replacement for desktop use have been provided. Therefore we still use it.

To install pyspotify, assuming pip has been installed, use the following command `pip install pyspotify`