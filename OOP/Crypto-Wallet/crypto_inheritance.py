from crypto_wallet import CryptoWallet


class BitcoinWallet(CryptoWallet):
    def __init__(self, owner_name, balance=0):
        super().__init__(owner_name, balance)
        self.currency = 'Bitcoin'

    def __str__(self):
        return f"Owner: {self.owner_name}, Balance: {self.balance} BTC"


class EthereumWallet(CryptoWallet):
    def __init__(self, owner_name, balance=0):
        super().__init__(owner_name, balance)
        self.currency = 'Ethereum'

    def __str__(self):
        return f"Owner: {self.owner_name}, Balance: {self.balance} ETH"
