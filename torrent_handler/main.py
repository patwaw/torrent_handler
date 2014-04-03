'''
	torrent_handler.py

	Frontend for Transmission Remote daemon.

'''

# TODO: Argument parsing
# TODO: More automation with torrents
# TODO: MIME type torrent add

import sys
import argparse
import transmissionrpc

class Torrent(object):
    def __init__(self, host='localhost', port=9091):
        self.host = host        
        self.port = port        
        try:
            self.client = transmissionrpc.Client(self.host, self.port)
        except:
            print "Connection refused. Exiting"
            sys.exit(1)

    def list(self):
        '''
        Function prints every torrent information.
        '''
        for torrent in self.client.get_torrents():
            print torrent.id, torrent.status
            print torrent.name
            print torrent.format_eta
            print "\n"

    def info(self, torrent_id):
        '''
        Function prints information about single torrent
        '''
        self.torrent_id = torrent_id
        self.result = self.client.get_torrent(self.torrent_id)
        print self.result.id, self.result.status
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
        self.data_remove = data_remove
        return self.client.remove_torrent(self.torrent_id, self.data_remove)

	

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="torrent_handler")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", type=str)
    group.add_argument("-r", "--remove", type=int)
    group.add_argument("-i", "--info", type=int)
    group.add_argument("-l", "--list", action='store_true')
    parser.add_argument('-p', '--port', type=str, help="Specify Transmission Remote port. default=9091")
    parser.add_argument('-c', '--connect', type=str, help="Specify Transmission Remote hostname/ip. default=localhost")
    args = parser.parse_args()
    port = args.port
    host = args.connect
    client = Torrent(host, port)
    if args.add != None:
        client.add_torrent(args.add)
    elif args.remove != None:
        client.remove_torrent(args.remove)
    elif args.list != None:
        client.list()
    elif args.info != None:
        client.info(args.info)
    else:
        sys.exit(0)