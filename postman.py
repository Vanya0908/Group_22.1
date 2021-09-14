{
	"info": {
		"_postman_id": "cd1ff23d-2a83-4bb4-88bf-b2450f949665",
		"name": "H.W.",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "1.1",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://162.55.220.72:5005/get_method?name=Ivan&age=28",
					"protocol": "http",
					"host": [
						"162",
						"55",
						"220",
						"72"
					],
					"port": "5005",
					"path": [
						"get_method"
					],
					"query": [
						{
							"key": "name",
							"value": "Ivan"
						},
						{
							"key": "age",
							"value": "28"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "1.2",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": [
						{
							"key": "name",
							"value": "Ivan",
							"type": "text"
						},
						{
							"key": "age",
							"value": "28",
							"type": "text"
						},
						{
							"key": "salary",
							"value": "2000",
							"type": "text"
						}
					]
				},
				"url": {
					"raw": "http://162.55.220.72:5005/user_info_3",
					"protocol": "http",
					"host": [
						"162",
						"55",
						"220",
						"72"
					],
					"port": "5005",
					"path": [
						"user_info_3"
					]
				}
			},
			"response": []
		},
		{
			"name": "1.3",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://162.55.220.72:5005/object_info_1?name=Ivan&age=28&weight=74",
					"protocol": "http",
					"host": [
						"162",
						"55",
						"220",
						"72"
					],
					"port": "5005",
					"path": [
						"object_info_1"
					],
					"query": [
						{
							"key": "name",
							"value": "Ivan"
						},
						{
							"key": "age",
							"value": "28"
						},
						{
							"key": "weight",
							"value": "74"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "1.4",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://162.55.220.72:5005/object_info_2?name=Ivan&age=28&salary=3000",
					"protocol": "http",
					"host": [
						"162",
						"55",
						"220",
						"72"
					],
					"port": "5005",
					"path": [
						"object_info_2"
					],
					"query": [
						{
							"key": "name",
							"value": "Ivan"
						},
						{
							"key": "age",
							"value": "28"
						},
						{
							"key": "salary",
							"value": "3000"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "1.5",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://162.55.220.72:5005/object_info_3?name=Ivan&age=28&salary=5000",
					"protocol": "http",
					"host": [
						"162",
						"55",
						"220",
						"72"
					],
					"port": "5005",
					"path": [
						"object_info_3"
					],
					"query": [
						{
							"key": "name",
							"value": "Ivan"
						},
						{
							"key": "age",
							"value": "28"
						},
						{
							"key": "salary",
							"value": "5000"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "1.6",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://162.55.220.72:5005/object_info_4?name=Ivan&age=28&salary=6000",
					"protocol": "http",
					"host": [
						"162",
						"55",
						"220",
						"72"
					],
					"port": "5005",
					"path": [
						"object_info_4"
					],
					"query": [
						{
							"key": "name",
							"value": "Ivan"
						},
						{
							"key": "age",
							"value": "28"
						},
						{
							"key": "salary",
							"value": "6000"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "1.7",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": [
						{
							"key": "name",
							"value": "Ivan",
							"type": "text"
						},
						{
							"key": "age",
							"value": "28",
							"type": "text"
						},
						{
							"key": "salary",
							"value": "7000",
							"type": "text"
						}
					]
				},
				"url": {
					"raw": "http://162.55.220.72:5005/user_info_2",
					"protocol": "http",
					"host": [
						"162",
						"55",
						"220",
						"72"
					],
					"port": "5005",
					"path": [
						"user_info_2"
					]
				}
			},
			"response": []
		}
	]
}