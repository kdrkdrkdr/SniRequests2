from pydivert import WinDivert
from threading import Thread
from requests import Session
from time import sleep


def DivertRST():
    while True: 
        with WinDivert("tcp.SrcPort == 443 and tcp.PayloadLength == 0") as w:
            try:
                for packet in w:
                    packet.tcp.rst = False
                    w.send(packet)
            except:
                w.close()


def DivertDecorator(func):
    def wrapper(*args, **kwargs):
        t1 = Thread(target=DivertRST, )
        t2 = Thread(target=func, args=args, kwargs=kwargs, )

        t1.start()
        t2.start()

        
        return func(*args, **kwargs)

    return wrapper



        


class SniSession:
    def __init__(self):
        self.sni_session = Session()


    def request(self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None):
        return self.sni_session.request(method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None)


    @DivertDecorator
    def get(self, url, **kwargs):
        return self.sni_session.get(url, **kwargs)

    
    def options(self, url, **kwargs):
        return self.sni_session.options(url, **kwargs)


    def head(self, url, **kwargs):
        return self.sni_session.head(url, **kwargs)


    @DivertDecorator
    def post(self, url, data=None, json=None, **kwargs):
        return self.sni_session.post(url, data, json, **kwargs)


    @DivertDecorator
    def put(self, url, data=None, **kwargs):
        return self.sni_session.put(url, data, **kwargs)


    @DivertDecorator
    def patch(self, url, data=None, **kwargs):
        return self.sni_session.patch(url, data, **kwargs)


    @DivertDecorator
    def delete(self, url, **kwargs):
        return self.sni_session.delete(url, **kwargs)


    @DivertDecorator
    def send(self, request, **kwargs):
        return self.sni_session.send(request, **kwargs)

    
    def merge_environment_settings(self, url, proxies, stream, verify, cert):
        return self.sni_session.merge_environment_settings(url, proxies, stream, verify, cert)


    def get_adapter(self, url):
        return self.sni_session.get_adapter(url)


    def close(self):
        return self.sni_session.close()

    
    def mount(self, prefix, adpater):
        return self.sni_session.mount(prefix, adpater)

    
    def __getstate__(self):
        return self.__getstate__()


    def __setstate__(self, state):
        return self.__setstate__(state)



