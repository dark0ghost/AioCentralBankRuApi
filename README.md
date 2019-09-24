# AioCentralBankRuApi

## How to install:
	git clone https://github.com/dark0ghost/async_py_bot.git
  
  
## How to use bot:
      import aiohttp
      import AioCentralBankRuApi
 
      async def start() -> None:
         session: aiohttp.ClientSession = aiohttp.ClientSession()
         cb: AioCentralBankRuApi = AioCentralBankRuApi
         coin: Dict[str,Dict[str,str]] = await  cb.build_list_coin()
         print(coin)
         print( coin["EUR"])
         await session.close()
 
  
