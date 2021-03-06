from Crypto.PublicKey import RSA
from Crypto.Util import number
from base64 import b64decode,b64encode

pkey_data = """MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAI8EUQvSHgJQF5zuWR0jfGC0aOAgveEo2ma73v7FryV/FORDZOpdEEjvWz4kpmNwBanUl73uLiHFaHco81FVwIK9z/KdnglawjTrV1Gg4XVPvWE1PqVRDFkAVRZX/y9jY7MsuN0b10Ozk8h+sLv0nQDEGFy7DdhWvzjDJb6j2j13AgMBAAECgYAtbx2gN7w41+Dohf/hdeiJgEbhDQXFhgj8IisRnROrQdgNPCvPGImX4hKGh3YkmO3zqgoa2JPnPqOVV3kVGbzyUgZnpcb5wR3YLzfmkeU+QkFKCD+A59jRc2TJOIV8FL8v+KS4NW2RN+nru63OEN6tJg9LkH4fUMN/SRK9WRIeAQJBAM+7O2PTOkj6LhInHvUChlLFzUWzspPnHOVjaxkONa1/OGbJtU5GdCyj2AOa15DOzMurlJCQLk22GKAF8n5vmbcCQQCwP5VJcxJAwaqEl3YUb+yuxVumokvRb+Ec+3LqKje0FOqeVT/5kCODpw3GRKTpCM4NnhfL8IKN/kFg0xcz1XpBAkA6pGuGqcmpcl7xJvQZTKYo1cg2Jh2CnVrN8vv37cf/e4urkMPLHh6Lv5Eqq1qxeX/c+0oMaXd43rAi9KrZQJ4PAkAYbqgGR5JnMbGuscRnruBTlf5Pij4SaXz+ZIkYlwOjziZ8DntQ4D9cF8NcEdX+i/7selb4KX4fqvhrMLgNsnFBAkEAr5MuiHM+QFurgHDYlddURe9Ux/m27oMlhbxpxqBRokzWRSR1QnSyzafgh3hjQloYfdStccLRM4oxz8j4m/HPiQ=="""

enc_data = "B1+wZuqs39+WKis75tdbRPks3C3LHbuXPXLHRWpTfrYCWD6eXme5azw7amHaKW6PLb3amxsqF7zcVE80kou0cbWE6QWjzIRSTAqGf0xggB8zoxBU87yNbdbVhSvABR7qxEFVD4ARkEl8LsX5Vw2EqgBqenHGBXj/HBJf9ul/U54="

pkey = RSA.importKey(b64decode(pkey_data))
enc = number.bytes_to_long(b64decode(enc_data))

text = number.long_to_bytes(pkey.decrypt(enc))

print(text)