request_spending={
    "Mehak":{
        "balance":3000.00,
        "transactions":[
            {"amount": -9000.00, "category":"Creatives"},
            {"amount": 7000.00,"category":"Sponsers"},
            {"amount": -2000.00,"category":"Prize-Money"}
        ]
    },
    "Arham":{
        "balance":5000.00,
        "transactions":[
            {"amount": 8000.00, "category":"Stalls"},
            {"amount": 7500.00,"category":"Seminars"}
        ]
    },
    "Unnati":{
        "balance":3500.00,
        "transactions":[
            {"amount": -5000.00, "category":"Attraction"},
            {"amount": 2500.00,"category":"Promo"},
            {"amount": -900.00,"category":"Lighting"},
            {"amount": -3000.00,"category":"Games"}
        ]
    },
    "Gaurang":{
        "balance":2000.00,
        "transactions":[
            {"amount": -1500.00, "category":"Website"},
            {"amount": -1000.00,"category":"C2C"},
            {"amount": -500.00,"category":"Posters"}
        ]
    }
}
def total_spending(request_spending,account_id,category):
    if account_id in request_spending:
        print(account_id)
        if category in request_spending:
            amount_spent=request_spending["transactions"]["amount"]
            print(amount_spent)
      
total_spending(request_spending,"Mehak","Sponsers")
    
