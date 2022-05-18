from GUI.Legacy.api_keys import API_KEY, API_SECRET

from binance.client import Client


class API(Client):
    
    def __init__(self,API_KEY,API_SECRET):
        Client.__init__(self,API_KEY,API_SECRET)
    

    def estado_cuenta(self):
        '''Funciona
        '''
        return self.get_account_status()
    
    def puntas_mercado(self):
        '''Funciona
        '''
        return self.get_orderbook_tickers()

    def puntas_ticker(self,**kwargs):
        '''FUnciona
        print(test.puntas_ticker(symbol="BTCUSDT")) 
        '''
        return self.get_order_book(**kwargs)

    def time (self):
        return self.get_server_time()

    def cambio_crypto(self):
        '''Funciona
        '''
        return self.get_exchange_info()

    def crypto_info(self,**kwargs):
        '''FUNCIONA
        print(test.crypto_info(symbol="LTCUSDT"))'''
        return  self.get_symbol_info(**kwargs)
    
    def all_last_price(self):
        '''Funciona'''
        return self.get_all_tickers()
    
    def all_mejores_puntas(self):
        '''funciona'''
        
        return self.get_orderbook_tickers()

    def last_trades(self,**kwargs):

        return self.get_recent_trades(**kwargs)

    def ticker_price(self,**kwargs):
        return self.get_symbol_ticker(**kwargs)
    def ticket_24hstats():
        pass

if __name__== "__main__":

    test=API(API_KEY,API_SECRET)
    print(test.ticker_price(symbol="BTCUSDT"))
    print(test.last_trades(symbol="BTCUSDT"))