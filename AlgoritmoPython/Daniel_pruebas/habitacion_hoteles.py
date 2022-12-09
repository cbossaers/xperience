import json
import os
import statistics

dictionary =[
	{ 
	"type": "hotel-offer",
	"id": "420A",
	"checkInDate": "2020-11-13",
	"checkOutDate": "2021-11-17",
	"roomQuantity": "3",
	"rateCode": "BNB",
	"rateFamilyEstimated": {
		"code": "relleno",
		"type": "relleno"
	}, 
	"category": "CategoriaEjemplo",
	"description": {
		"text": "relleno",
		"lang": "relleno"
	},
	"commission": {
		"percentage": "20.50",
		"amount": "40.50",
		"description": {
			"text": "relleno",
			"lang": "relleno"
		}
	},
	"boardType": "ROOM_ONLY",
	"room":{
		"type": "A32",
		"typeEstimated": {
		"category": "relleno",
		"beds": 2,
		"bedType": "relleno"
		},
		"description": {
		"text": "relleno",
		"lang": "relleno"
		}
	},
	"guests":{
		"adults": 3,
		"childAges": [7,8,9]
	},
	"price":{
		"currency": "EUR",
		"sellingTotal": "600.50",
		"total": "500.00",
		"base": "400.00",
		"taxes": [
			{
				"amount": "relleno",
				"currency": "relleno",
				"code": "relleno",
				"percentage": "relleno",
				"included": "relleno",
				"description": "relleno",
				"pricingFrequency": "relleno",
				"pricingMode": "relleno"
			}
		],
		"markups": [
			{
				"description": "relleno",
				"amount": "relleno"
			}
		],
		"variations": {
			"average":{
				"currency": "EUR",
				"sellingTotal": "550.25",
				"total": "450.00",
				"base": "400.00",
				"markups": [
					{
						"description": "relleno",
						"amount": "relleno"
					}
				]
			},
			"changes": [
				{
					"startDate": "2020-11-01",
					"endDate": "2020-11-12",
					"currency": "relleno",
					"sellingTotal": "700.00",
					"total": "600.00",
					"base": "500.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-11-20",
					"endDate": "2020-11-23",
					"currency": "relleno",
					"sellingTotal": "600.00",
					"total": "500.00",
					"base": "400.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-10-01",
					"endDate": "2020-10-12",
					"currency": "relleno",
					"sellingTotal": "500.00",
					"total": "400.00",
					"base": "300.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-10-20",
					"endDate": "2020-10-23",
					"currency": "relleno",
					"sellingTotal": "400.00",
					"total": "300.00",
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-09-01",
					"endDate": "2020-09-12",
					"currency": "relleno",
					"sellingTotal": "400.00",
					"total": "300.00",
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-09-30",
					"endDate": "2020-10-03",
					"currency": "relleno",
					"sellingTotal": "600.00",
					"total": "500.00",
					"base": "400.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-08-01",
					"endDate": "2020-08-12",
					"currency": "relleno",
					"sellingTotal": "300.00",
					"total": "200.00",
					"base": "100.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-08-20",
					"endDate": "2020-08-23",
					"currency": "relleno",
					"sellingTotal": "500.00",
					"total": "400.00",
					"base": "300.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-07-01",
					"endDate": "2020-07-12",
					"currency": "relleno",
					"sellingTotal": "700.00",
					"total": "600.00",
					"base": "500.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-07-20",
					"endDate": "2020-07-23",
					"currency": "relleno",
					"sellingTotal": "800.00",
					"total": "700.00",
					"base": "600.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-06-01",
					"endDate": "2020-06-12",
					"currency": "relleno",

					"total": "700.00",
					"base": "600.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-06-20",
					"endDate": "2020-06-23",
					"currency": "relleno",
					"sellingTotal": "800.00",
					"total": "700.00",
					"base": "600.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-04-01",
					"endDate": "2020-04-12",
					"currency": "relleno",
					
					
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-04-20",
					"endDate": "2020-04-23",
					"currency": "relleno",
					
					"total": "300.00",
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-03-01",
					"endDate": "2020-03-12",
					"currency": "relleno",
					"sellingTotal": "400.00",
					"total": "300.00",
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-03-20",
					"endDate": "2020-03-23",
					"currency": "relleno",
					"sellingTotal": "600.00",
					"total": "500.00",
					"base": "400.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-02-01",
					"endDate": "2020-02-12",
					"currency": "relleno",
					"sellingTotal": "800.00",
					"total": "700.00",
					"base": "600.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-02-20",
					"endDate": "2020-02-23",
					"currency": "relleno",



					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				
			]
		}
	},
	"polices":{
		"paymentType": "relleno",
		"guarantee": "relleno",
		"deposit": "relleno",
		"prepay": "relleno",
		"holdTime": "relleno",
		"cancellation": "relleno",
		"checkInOut": "relleno",
	},
	"self": "relleno"
	},
	{ 
	"type": "hotel-offer",
	"id": "420A",
	"checkInDate": "2020-11-13",
	"checkOutDate": "2021-11-17",
	"roomQuantity": "3",
	"rateCode": "BNB",
	"rateFamilyEstimated": {
		"code": "relleno",
		"type": "relleno"
	}, 
	"category": "CategoriaEjemplo",
	"description": {
		"text": "relleno",
		"lang": "relleno"
	},
	"commission": {
		"percentage": "20.50",
		"amount": "40.50",
		"description": {
			"text": "relleno",
			"lang": "relleno"
		}
	},
	"boardType": "ROOM_ONLY",
	"room":{
		"type": "A32",
		"typeEstimated": {
		"category": "relleno",
		"beds": 2,
		"bedType": "relleno"
		},
		"description": {
		"text": "relleno",
		"lang": "relleno"
		}
	},
	"guests":{
		"adults": 3,
		"childAges": [7,8,9]
	},
	"price":{
		"currency": "EUR",
		"sellingTotal": "600.50",
		"total": "500.00",
		"base": "400.00",
		"taxes": [
			{
				"amount": "relleno",
				"currency": "relleno",
				"code": "relleno",
				"percentage": "relleno",
				"included": "relleno",
				"description": "relleno",
				"pricingFrequency": "relleno",
				"pricingMode": "relleno"
			}
		],
		"markups": [
			{
				"description": "relleno",
				"amount": "relleno"
			}
		],
		"variations": {
			"average":{
				"currency": "EUR",
				"sellingTotal": "550.25",
				"total": "450.00",
				"base": "400.00",
				"markups": [
					{
						"description": "relleno",
						"amount": "relleno"
					}
				]
			},
			"changes": [
				{
					"startDate": "2020-11-01",
					"endDate": "2020-11-12",
					"currency": "relleno",
					"sellingTotal": "700.00",
					"total": "600.00",
					"base": "500.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-11-20",
					"endDate": "2020-11-23",
					"currency": "relleno",
					"sellingTotal": "600.00",
					"total": "500.00",
					"base": "400.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-10-01",
					"endDate": "2020-10-12",
					"currency": "relleno",
					"sellingTotal": "500.00",
					"total": "400.00",
					"base": "300.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-10-20",
					"endDate": "2020-10-23",
					"currency": "relleno",
					"sellingTotal": "400.00",
					"total": "300.00",
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-09-01",
					"endDate": "2020-09-12",
					"currency": "relleno",
					"sellingTotal": "400.00",
					"total": "300.00",
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-09-30",
					"endDate": "2020-10-03",
					"currency": "relleno",
					"sellingTotal": "600.00",
					"total": "500.00",
					"base": "400.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-08-01",
					"endDate": "2020-08-12",
					"currency": "relleno",
					"sellingTotal": "300.00",
					"total": "200.00",
					"base": "100.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-08-20",
					"endDate": "2020-08-23",
					"currency": "relleno",
					"sellingTotal": "500.00",
					"total": "400.00",
					"base": "300.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-07-01",
					"endDate": "2020-07-12",
					"currency": "relleno",
					"sellingTotal": "700.00",
					"total": "600.00",
					"base": "500.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-07-20",
					"endDate": "2020-07-23",
					"currency": "relleno",
					"sellingTotal": "800.00",
					"total": "700.00",
					"base": "600.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-06-01",
					"endDate": "2020-06-12",
					"currency": "relleno",
					"total": "700.00",
					"base": "600.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-06-20",
					"endDate": "2020-06-23",
					"currency": "relleno",
					"sellingTotal": "800.00",
					"total": "700.00",
					"base": "600.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-04-01",
					"endDate": "2020-04-12",
					"currency": "relleno",
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-04-20",
					"endDate": "2020-04-23",
					"currency": "relleno",
					"total": "300.00",
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-03-01",
					"endDate": "2020-03-12",
					"currency": "relleno",
					"sellingTotal": "400.00",
					"total": "300.00",
					"base": "200.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-03-20",
					"endDate": "2020-03-23",
					"currency": "relleno",
					"sellingTotal": "600.00",
					"total": "500.00",
					"base": "400.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-02-01",
					"endDate": "2020-02-12",
					"currency": "relleno",
					"sellingTotal": "800.00",
					"total": "700.00",
					"base": "600.00",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				{
					"startDate": "2020-02-20",
					"endDate": "2020-02-23",
					"currency": "relleno",
					"markups": [
						{
							"description": "relleno",
							"amount": "relleno"
						}
					]
				},
				
			]
		}
	},
	"polices":{
		"paymentType": "relleno",
		"guarantee": "relleno",
		"deposit": "relleno",
		"prepay": "relleno",
		"holdTime": "relleno",
		"cancellation": "relleno",
		"checkInOut": "relleno",
	},
	"self": "relleno"
	}
]
      
# Serializing json
def getListaHabitaciones():
	json_object = json.dumps(dictionary, indent = 4)
	listOfRooms = json.loads(json_object)
	price = 0
	average = 0
	changes = [
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		},
		{
			"quantity": 0,
			"count": 0
		}
	]

	roomMonthAverageList = []
	monthList = []
	roomStd = []
	for room in listOfRooms:
		if "sellingTotal" in room["price"]:
			price = float(room["price"]["sellingTotal"])
		elif "total" in room["price"]:
			price = float(room["price"]["total"])
		elif "base" in room["price"]:
			price = float(room["price"]["base"])
		if "variations" in room["price"]:
			if "average" in room["price"]["variations"]:
				average = float(room["price"]["sellingTotal"])
			if "changes" in room["price"]["variations"]:
				monthAverageList = []
				monthInOfferList = []
				changes[0]["quantity"] = 0
				changes[0]["count"] = 0
				changes[1]["quantity"] = 0
				changes[1]["count"] = 0
				changes[2]["quantity"] = 0
				changes[2]["count"] = 0
				changes[3]["quantity"] = 0
				changes[3]["count"] = 0
				changes[4]["quantity"] = 0
				changes[4]["count"] = 0
				changes[5]["quantity"] = 0
				changes[5]["count"] = 0
				changes[6]["quantity"] = 0
				changes[6]["count"] = 0
				changes[7]["quantity"] = 0
				changes[7]["count"] = 0
				changes[8]["quantity"] = 0
				changes[8]["count"] = 0
				changes[9]["quantity"] = 0
				changes[9]["count"] = 0
				changes[10]["quantity"] = 0
				changes[10]["count"] = 0
				changes[11]["quantity"] = 0
				changes[11]["count"] = 0
				for variation in room["price"]["variations"]["changes"]:
					if variation["startDate"][5:7] == "01" or variation["endDate"][5:7] == "01":
						print("hi")
						if "sellingTotal" in variation:
							changes[0]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[0]["count"] +=1
						elif "total" in variation:
							changes[0]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[0]["count"] +=1
						elif "base" in variation:
							changes[0]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[0]["count"] +=1
					elif variation["startDate"][5:7] == "02" or variation["endDate"][5:7] == "02":
						if "sellingTotal" in variation:
							changes[1]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[1]["count"] +=1
						elif "total" in variation:
							changes[1]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[1]["count"] +=1
						elif "base" in variation:
							changes[1]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[1]["count"] +=1
					elif variation["startDate"][5:7] == "03" or variation["endDate"][5:7] == "03":
						if "sellingTotal" in variation:
							changes[2]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[2]["count"] +=1
						elif "total" in variation:
							changes[2]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[2]["count"] +=1
						elif "base" in variation:
							changes[2]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[2]["count"] +=1
					elif variation["startDate"][5:7] == "04" or variation["endDate"][5:7] == "04":
						if "sellingTotal" in variation:
							changes[3]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[3]["count"] +=1
						elif "total" in variation:
							changes[3]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[3]["count"] +=1
						elif "base" in variation:
							changes[3]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[3]["count"] +=1
					elif variation["startDate"][5:7] == "05" or variation["endDate"][5:7] == "05":
						if "sellingTotal" in variation:
							changes[4]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[4]["count"] +=1
						elif "total" in variation:
							changes[4]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[4]["count"] +=1
						elif "base" in variation:
							changes[4]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[4]["count"] +=1
					elif variation["startDate"][5:7] == "06" or variation["endDate"][5:7] == "06":
						if "sellingTotal" in variation:
							changes[5]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[5]["count"] +=1
						elif "total" in variation:
							changes[5]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[5]["count"] +=1
						elif "base" in variation:
							changes[5]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[5]["count"] +=1
					elif variation["startDate"][5:7] == "07" or variation["endDate"][5:7] == "07":
						if "sellingTotal" in variation:
							changes[6]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[6]["count"] +=1
						elif "total" in variation:
							changes[6]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[6]["count"] +=1
						elif "base" in variation:
							changes[6]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[6]["count"] +=1
					elif variation["startDate"][5:7] == "08" or variation["endDate"][5:7] == "08":
						if "sellingTotal" in variation:
							changes[7]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[7]["count"] +=1
						elif "total" in variation:
							changes[7]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[7]["count"] +=1
						elif "base" in variation:
							changes[7]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[7]["count"] +=1
					elif variation["startDate"][5:7] == "09" or variation["endDate"][5:7] == "09":
						if "sellingTotal" in variation:
							changes[8]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[8]["count"] +=1
						elif "total" in variation:
							changes[8]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[8]["count"] +=1
						elif "base" in variation:
							changes[8]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[8]["count"] +=1
					elif variation["startDate"][5:7] == "10" or variation["endDate"][5:7] == "10":
						if "sellingTotal" in variation:
							changes[9]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[9]["count"] +=1
						elif "total" in variation:
							changes[9]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[9]["count"] +=1
						elif "base" in variation:
							changes[9]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[9]["count"] +=1
					elif variation["startDate"][5:7] == "11" or variation["endDate"][5:7] == "11":
						if "sellingTotal" in variation:
							changes[10]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[10]["count"] +=1
						elif "total" in variation:
							changes[10]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[10]["count"] +=1
						elif "base" in variation:
							changes[10]["quantity"] += float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[10]["count"] +=1
					elif variation["startDate"][5:7] == "12" or variation["endDate"][5:7] == "12":
						if "sellingTotal" in variation:
							changes[11]["quantity"] += float(variation["sellingTotal"])
							monthList.append(float(variation["sellingTotal"]))
							changes[11]["count"] +=1
						elif "total" in variation:
							changes[11]["quantity"] += float(variation["total"])
							monthList.append(float(variation["total"]))
							changes[11]["count"] +=1
						elif "base" in variation:
							changes[11]["quantity"] = float(variation["base"])
							monthList.append(float(variation["base"]))
							changes[11]["count"] +=1
				for change in changes:
					if change["quantity"] != 0:
						monthAverageList.append(change["quantity"]/change["count"])
					else:
						monthAverageList.append(0)
		roomMonthAverageList.append(monthAverageList)
		roomStd.append(statistics.pstdev(monthList))
		for monthAverageIsOffer in monthAverageList:
			if monthAverageIsOffer!=0 and monthAverageIsOffer <= (average - 2*statistics.pstdev(monthList)):
				monthInOfferList.append("Y")
			else:
				monthInOfferList.append("N")
	return price, average, roomStd, monthInOfferList, roomMonthAverageList			
		


print(getListaHabitaciones())

