import requests

session = requests.session()
# session.headers['content-yype'] = 'application/x-www-form-urlencoded'
header = {
    'content-yype': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'x-zse-83': '3_2.0',

}
session.headers.update(header)
result = session.post('https://www.zhihu.com/api/v3/oauth/sign_in',
                      data='a_3mcCe8FwxmkLF0sTYh2cHmD93Vgq398LF0c79hXq2pkLPGfCNmxg9qkLP9DbSBtq39k4U0geO9FbfGPgx1j9QGoGpmkLF0z8H0c79huq2pkLkM19pGiC3MgUNV-9e0zLS8kvcm2vwYgh3q8LP924_BFhoV-qoVp9VGS79hEqNm2LkBXwxmS79hXq2tUUS8KuV8FrU0g82L6BNmfUVYXg9hHhV9oqoMZu3qk47qSHFpeL20mH20rQuyPh2pkLP9BLfBJJHmkCOOcBF0zM28nbHBbL2fFCO018xqriuBbHYxcLOqM_S8oHXqUCSY20O0M8YyFvu92LkYkCpGZbSBDggqkLPfgG3ZsUO1iugZJvOfXqYhzqNMcCeMST2t67Y0GH20oA90SH2pr_e0zRVmUbcMgcS_eBF0z_NM-ccM2wNOXqYhzuVKeCpGEwxO3BF0zRF0gDUqr02YrXNqzgY827XyNqFp6XY8M828oQLBFqYfXqYhygSVe9LBDrOf:')
print(result.text)
