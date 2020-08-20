# AioCentralBankRuApi

## How to install:
	git clone https://github.com/dark0ghost/AioCentralBankRuApi.git
# dep
**python>=3.7 aiohttp>=3.6**
  
## How to use bot:
```python
      import aiohttp
      import AioCentralBankRuApi
 
      async def start() -> None:
         session: aiohttp.ClientSession = aiohttp.ClientSession()
         cb: AioCentralBankRuApi = AioCentralBankRuApi
         coin: Dict[str,Dict[str,str]] = await  cb.build_list_coin()
         print(coin)
         print( coin["EUR"])
         await session.close()
	 ```
 
  
