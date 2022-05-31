# -*- coding: utf-8 -*-
import dingtalk.api
import json


def getToken():
	req=dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
	access_token=""
	req.appkey="dingipn99fcmrkc8gkxp"
	req.appsecret="-Idw05ZBjf3-ZxbHhZKBRljjwgKfgnohw4_5UOSeBxotPDTt9xFuymeoqxl0_6MA"

	try:
		resp= req.getResponse(access_token)
		access_token = resp["access_token"]
		# access_token = data["access_token"]
		print("access_token:",access_token)
	except Exception as e:
		print(e)
	return access_token


req=dingtalk.api.OapiKacDatavDeptVideoconfListRequest("https://oapi.dingtalk.com/topapi/kac/datav/dept/videoconf/list")

data_id = "20220528"
print("日期：",data_id)

req.request={"size":5,
			"cursor":0,
			"data_id":data_id}
access_token = "4f1fe92d265b35ad959c9abfcc46c2cf"

try:
	resp= req.getResponse(access_token)
	print("resp:",resp)
	# //data = json.load(resp)
	# print(data)
	data = resp["result"]["data"];

	for k in data:
		print("部门：",k['dept_name']," ")
		print("参与人数：", k['join_count'], " ")
		print("会议次数：", k['start_count'], " ")
		print("平均时长：", k['start_avg_len_min'], " ")
		print("总时长：", k['start_len_min'], " ")
		print("\n")
except Exception as e :
	print(e)