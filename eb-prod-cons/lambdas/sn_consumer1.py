def lambda_handler(event, context):
    transactions = event["detail"]["transactions"]
    print('Consumer 1 received:', event)
    print("Transfering point from client to aliadito")
    for tx in transactions:
        pt = tx["payment_type"]
        total = tx["total"]
        p_to_aliadito = tx["points_to_aliadito"]
        p_to_client = tx["points_to_client"]
        if p_to_aliadito > 0:
            # print(f"Payment type: {pt}, Total: {total}, Points to Aliadito: {p_to_aliadito}, Points to client: {p_to_client}")
            print(f"Transfering {p_to_aliadito} points from client to aliadito. Total: {total}, Payment type: {pt}")