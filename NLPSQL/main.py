import wordIdentifier as wI
import codeGenerator as cG

def processQuery():
    query=input("Enter the Query :")
    print(query)
    query=query.lower()
	
    #wordIdentifier tokenizes sentences and tags words and segregates into numerals,keywords etc.,
    tokens,keywords,tagged,numerals=wI.wordIdentifier(query)
    cond = 0
    trans_list = ['transaction_id', 'cust_id', 'Qty', 'Rate', 'Tax', 'total_amt', 'Store_type']
    cust_list = ['customer_Id', 'Gender', 'DOB', 'city_code']

    for i in tokens:
        if (i in trans_list or i in cust_list):
            cond = 1
        elif (i in trans_list or i in cust_list):
            
        else:
            cond = 2

    sqlQuery = cG.queryGenerator(tagged, keywords, numerals, tokens, cond)

    return sqlQuery
	
processQuery()


