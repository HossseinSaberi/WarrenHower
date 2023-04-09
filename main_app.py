from proj_setting import settings
import uvicorn
if __name__=='__main__':
    print(settings.host,settings.port,settings.reload)
    uvicorn.run('config:app',host=settings.host,port=int(settings.port),reload=settings.reload)