from fastapi import FastAPI, Response
from fastapi.params import Form
from starlette.responses import PlainTextResponse, FileResponse

app = FastAPI()

downloads_base_files = '''czAssetManager.dll\n
czBinds.dll\n
czBrowser.dll\n
czBypass.dll\n
czCompass.dll\n
czGameVars.dll\n
czFPSWheel.dll\n
czJumpHud2.dll\n
czRpgScript.dll\n
czChat.dll\n
czJumpAnalyzer.dll\n
czHops.dll\n
czRPG.dll\n
czMeasure.dll\n
fonts/arial.ttf\n
fonts/CollegiateBlackFLF.ttf\n
fonts/CollegiateOutlineFLF.ttf\n
fonts/CollegiateInsideFLF.ttf\n
fonts/CollegiateFLF.ttf\n
czScriptMenu.dll\n
czGravGun.dll\n
czCollisions.dll\n
czMain.dll\n
czElebot2.dll\n
czAutoFPS.dll\n
czSegment.dll\n
czStrafer.dll\n
'''


@app.get("/downloads/mssloader.asi")
async def download_mssloader():
    try:
        file_path = "./mssloader.asi"
        return FileResponse(file_path, media_type='application/octet-stream')
    except Exception as e:
        return {"error": str(e)}


@app.post("/downloads/base", response_class=PlainTextResponse)
def download_base_files():
    return downloads_base_files


@app.post("/downloads/filecheck", response_class=PlainTextResponse)
def file_check(response: Response):
    response.set_cookie(key="connect.sid",
                        value="s%3AAODmv49iGPqLN1i1UUd8FH_YAACH6Dbz.83lDsUYdMtLzC1vfhZZgX6QLiXLHxVl3rpMp627O6Ec")
    return '''5a715a6d49a20cbd20dbb890d4c15cb2:mssloader.asi'''


@app.post("/downloads/auth", response_class=PlainTextResponse)
def authentication(response: Response, hwid: str = Form(...), name: str = Form(...)):
    # Check if hwid is in validhwids.txt
    with open("userlog.txt", "a") as f:
        f.write(f"{hwid},{name}\n")
    with open("bannednames.txt", "r") as f:
        banned_users = [line.strip().split(",")[1] for line in f]
    if name in banned_users:
        response_body = "0000"  # Return the hwid if it's valid
    else:
        # Add hwid and name to userlog.txt
        response_body = "4780d12e82fa3284dd0f02c1908affd1443e35c102d97a7caf01da413000d3d318ad5cbcc657306bff82f0b82897be5fb618314f4505c6da2eedfbd1606d24267e38dedb208e04c930955296fca0bc23268010fe8a1b5b9667296b12b2af616de4f1cb0ec7b87a700b43fcc3d96cad813ef7c07f8ca219baebcb30ec0e2a72f2cfaf284438356b511def344fded132c3cabbf34a1e0fcdadc8687b9517224314e99faf876a17ba470fea64ed3b05a547efe6a04c5b8e988d6208ff2863f3408e356467b7d3bd80ba5c790345f417fe71de756e41f4f9db5e04852265f48bde44705ed10e99e0342b2000ea1af74c3b608674cedad446c2ebf56b39f2cd6a488404e6cbbc0de1f688a3f8a7cc32fa61165724b5225fe0c546a4c2eece6619b36ffb43c332a329ddcac699a2857eb9767318fc757b1c541a1b35039ca806e29ae5082b2adacc4fee65d59900f038f255a831ebe46cc3cb58d466db844073ae9e5cacbc1e4b96bb684f963790863086777e158c4af2249b54acc46a4b5673b50dc4b6bdcbfc1f813b61c04f45c387a465a861ca76a2a3bd2f598ff5f71d63d4bb5846882724f033e78fa8efcf003a88f3befaa8691c869a685bb82308bcf3c4f1c7a522d84f1a8795c9afa6464189debe6c2469482fcb2bf66b0bb6eb5fb2b90ddce25345fe0c63728c9a4aedb84aeb7fce6f775fea3dc37258d3bbad25782c8c2347c3d24ed75c6984d6a53766073c8c8278378b2586976eacd275ccd7b4fe4849434b009052324c315b0f5ae03d779367a2c896aa0cd8be3193c18c483b1b0abf11898f36ea4cf4a85825f8496be49f5d0ff2cbab69f4588129e0fa8f03bd38fd22069c26ed6fd14f2eb8ceec4077366bcb044b28349f64cbf905cb0d10dd2af2650a175ed0f18045ea22090012010d72af237ff134fc48fb0491c55d687b8d17fd6d812f100b34c2b4850e62b0ea7432b693073d5213cc17b9c3fbd7a503ad783a52e33f9044b2e3ba7d966b159d1f436263e36e142651ad75f88220be47d0c8987b7c2d8cc549fb7e1469693228074c96bf58f5975ef55e25c2721fde2a97a3c108a0dbcd3f0f89c731e67471862f0f3388d954800eead154b39e1e86a06c6a5e3c446db169bc0ed178f4a3fb3431201687b842d6f8dcefceead64e97fdd13d9065471321da59bc0ef69a013aa77aa6c9c2f4ff7fa0461e66ec0418fdb128a1902a2b451b14197469bf8d223326c4efd22a0bed495bd173bcdc7b085f4da0548b26895b9190e6bf71bec53cb21d0736098b60bc587ebdaaef7fd0e3d6d6992bf2ee74c8b6a89e5db89bbc3a0eda7cd5999e87aebd68ce10ce38b964a6f3be4cd6299ed07ed0b88f39eff13821088bdb43a78fa7bf67230ae135a6337e871b539c8274f69cefcc350e5893ca35dbb7e6913d1e86f48e2512d5761e5ebec66674542aa8d50d6e216f740e63334b00aaba6d9a8b2fa5b78f570e75aeb88cade6b1b83ba0c123290dc9eeb947b2d9c9c2391162334a3035136cc2696c597918d5a2323486cfc105b173cae21ad5fbfeae0262c46965960c587600c42cbb26c5cec280852ec08c08f001272a3f1771e19b0b4de5b16639047f77026661c7a1d148252288636c783e93028ad93bcc8f85992f7baaec6ef78006df9b42de21c03c1b34ac84c814b02decf40765939d20a0d1c2ff6cd5f9b80da68118b1f088b0f79314d4e13975a8a24bca154d93690d6eda8c80a4062d5aef4469c6752e4f1dc55aa8da0e20921ca0b98c45e568ac383d64582d059b1ca9c7935b163f35ed484461463b86be3f3c9ec6f040cd624417d9336d39dd9839aea65a8d38fbcc00a442c3dd"

    return response_body


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=80
    )
