from requests import Session

class Gofile:
    def __init__(self):
        self.sesssion = Session()
        self.sesssion.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }

    def createAccount(self):
        res = self.sesssion.get("https://api.gofile.io/createAccount")
        return res.json()["data"]["token"]

    def getServer(self):
        res = self.sesssion.get("https://api.gofile.io/getServer")
        return res.json()["data"]["server"]

    def uploadFile(self, file):
        server = gof.getServer()
        res = self.sesssion.post(
            f"https://{server}.gofile.io/uploadFile",
            files = {'file': open(file,'rb')}
        )
        return res.json()["data"]["code"]
    
    def readFile(self, code):
        token = self.createAccount()
        res = self.sesssion.get(f"https://api.gofile.io/getContent?contentId={code}&token={token}&websiteToken=7fd94ds12fds4")
        link = res.json()["data"]["contents"][res.json()["data"]["childs"][0]]["link"]

        self.sesssion.cookies.update({'accountToken': token})

        res = self.sesssion.get(link)
        return res.text

if __name__ == "__main__":
    gof = Gofile()
    code = gof.uploadFile("licence.txt")
    print(gof.readFile(code))