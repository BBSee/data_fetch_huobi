from huobi.FetchClient import FetchClient


# 定义操作交易对
symbol = 'btcusdt'
# 定义周期值 单位为min
period = 60
# 开始时间
fc = FetchClient(exchange='huobi', symbol=symbol, period=period)
fc.start_fetch()
