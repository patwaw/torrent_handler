'''
	torrent_handler.py

	Frontend for Transmission Remote daemon.

'''

# TODO: Argument parsing
# TODO: More automation with torrents
# TODO: MIME type torrent add

import transmissionrpc

class Torrent(object):
    def __init__(self, host='localhost', port=9091):
        self.host = host        
        self.port = port        
        self.client = transmissionrpc.Client(self.host, self.port)

    def info_all(self):
        '''
        Function prints every torrent information.
        '''
        for torrent in self.client.get_torrents():
            print torrent.id
            print torrent.name
            print torrent.format_eta
            print "\n"

    def info_one(self, torrent_id):
        '''
        Function prints information about single torrent
        '''
        self.torrent_id = torrent_id
        self.result = self.client.get_torrent(self.torrent_id)
        print self.result.id
        print self.result.name

    def add_torrent(self, url):
        '''
        Function add torrent from url to client
        '''
        self.url = url
        return self.client.add_torrent(self.url)

    def remove_torrent(self, torrent_id, data_remove=False):
        '''
        Function remove torrent from client
        '''
        self.torrent_id = torrent_id
        self.data_remove = data_remove
        return self.client.remove_torrent(self.torrent_id, self.data_remove)

	

if __name__ == '__main__':
    pass