from __future__ import print_function
from cmath import log
import re
import struct
import sys
import urllib.request as urllib2


def fetch_meta(url):
    encoding = 'utf-8'  # default: iso-8859-1 for mp3 and utf-8 for ogg streams
    try:
        request = urllib2.Request(
            url, headers={'Icy-MetaData': 1}
        )  # request metadata

        response = urllib2.urlopen(request)
        metaint = int(response.headers['icy-metaint'])

        for _ in range(10):  # title may be empty initially, try several times
            response.read(metaint)  # skip to metadata
            metadata_length = struct.unpack('B', response.read(1))[
                0] * 16  # length byte

            metadata = response.read(metadata_length).rstrip(b'\0')
            print(metadata.decode(encoding))
            m = re.search(br"StreamTitle='([^']*)';", metadata)
            if m:
                title = m.group(1)
                if title:
                    break
        else:
            return {}

        return {
            'title': title.decode(encoding, 'replace')
        }
    except Exception as e:
        print('Failed to fetch metadata:', e)
        return {}
