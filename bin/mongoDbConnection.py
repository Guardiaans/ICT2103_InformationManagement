import pymongo
from pymongo import MongoClient

# csvfile = "C:\\Users\\sheng\\OneDrive - Singapore Institute Of Technology\\Desktop\\SE - Y2_TRI_1\\ICT 2103\\personal expenses\\mongo\\user_detail.csv"

cluster = MongoClient("mongodb+srv://shengyu98:PiJF4JXI@cluster0.zwj7f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["expenseTracker"]
collection = db["expenseTracker"]

userData = [{
    "account_id": 1001,
    "date_registered": "30/10/2021",
    "name": "Ang Yi Min",
    "bank_name": "OCBC",
    "password": "password123",
    "balance": 16000,
    "email": "aym@gmail.com",
    "transactions": [{
            "transaction_date": "30/4/2021",
            "debit_amount": "0",
            "credit_amount": "0.26",
            "description_1": "6104952719489604 OTHR GOOGLE PAY MENT",
            "description_2": "FAST TRANSFER",
            "category": "Cashback"
        },
        {
            "transaction_date": "5/5/2021",
            "debit_amount": "0",
            "credit_amount": "0.18",
            "description_1": "7969476824228909 OTHR GOOGLE PAY MENT",
            "description_2": "FAST TRANSFER",
            "category": "Cashback"
        },
        {
            "transaction_date": "17/8/2021",
            "debit_amount": "0",
            "credit_amount": "0.13",
            "description_1": "8269726151243496 OTHR GOOGLE PAY MENT",
            "description_2": "FAST TRANSFER",
            "category": "Cashback"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": "0",
            "credit_amount": "0.31",
            "description_1": "6774669374291668 OTHR GOOGLE PAY MENT",
            "description_2": "FAST TRANSFER",
            "category": "Cashback"
        },
        {
            "transaction_date": "25/8/2021",
            "debit_amount": "0",
            "credit_amount": "0.93",
            "description_1": "CASH REBATE",
            "description_2": "CASH REBATE",
            "category": "Cashback"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": "0",
            "credit_amount": "0.46",
            "description_1": "8511069957456760 OTHR GOOGLE PAY MENT",
            "description_2": "FAST TRANSFER",
            "category": "Cashback"
        },
        {
            "transaction_date": "21/9/2021",
            "debit_amount": "0",
            "credit_amount": "0.34",
            "description_1": "CASH REBATE",
            "description_2": "CASH REBATE",
            "category": "Cashback"
        },
        {
            "transaction_date": "18/5/2021",
            "debit_amount": "65",
            "credit_amount": "0",
            "description_1": "xx-1234 ZEPPELIN & CO PTE LTD S 15/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Entertainment"
        },
        {
            "transaction_date": "8/6/2021",
            "debit_amount": "1.5",
            "credit_amount": "0",
            "description_1": "xx-1234 PAYPAL *STEAM GAMES 3 05/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Entertainment"
        },
        {
            "transaction_date": "28/6/2021",
            "debit_amount": "16",
            "credit_amount": "0",
            "description_1": "xx-1234 MUSE COMMUNICATION SG PTES 25/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Entertainment"
        },
        {
            "transaction_date": "15/8/2021",
            "debit_amount": "36",
            "credit_amount": "0",
            "description_1": "xx-1234 CHIHULY GARDEN EXHIBIT 13/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Entertainment"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": "7.57",
            "credit_amount": "0",
            "description_1": "xx-1234 PAYPAL *STEAM GAMES 0 17/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Entertainment"
        },
        {
            "transaction_date": "25/9/2021",
            "debit_amount": "26.36",
            "credit_amount": "0",
            "description_1": "xx-1234 YQUEUE MUSEINITIATIVE KSRS 22/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Entertainment"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "xx-1234 PEPPER LUNCH S 27/04/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "2/5/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 STARBUCKS@WEST COAST (WP)S 29/04/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "10/5/2021",
            "debit_amount": "5.62",
            "credit_amount": "0",
            "description_1": "xx-1234 KREAM BEER S 07/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": "28",
            "credit_amount": "0",
            "description_1": "xx-1234 IKEA RESTAURANT / SFM - JS 11/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "13/6/2021",
            "debit_amount": "6.6",
            "credit_amount": "0",
            "description_1": "xx-1234 MCDONALD'S (WCP) S 11/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "20/6/2021",
            "debit_amount": "126.76",
            "credit_amount": "0",
            "description_1": "xx-1234 NTUC FP - HILLION S 18/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "28/6/2021",
            "debit_amount": "37.18",
            "credit_amount": "0",
            "description_1": "xx-1234 AHTTI-MM S 24/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "2/7/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 MA MUM - NTF S 01/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "7/7/2021",
            "debit_amount": "36.02",
            "credit_amount": "0",
            "description_1": "xx-1234 MONSTER PLANET JEM S 06/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "9/7/2021",
            "debit_amount": "24.5",
            "credit_amount": "0",
            "description_1": "OTHR - 200501738ZMAXO7W029534084 to WAN CHAI CAPITAL via PayNow-UEN",
            "description_2": "FAST PAYMENT",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "10/7/2021",
            "debit_amount": "25",
            "credit_amount": "0",
            "description_1": "xx-1234 A&W - JURONG POINT S 09/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "13/7/2021",
            "debit_amount": "17.5",
            "credit_amount": "0",
            "description_1": "xx-1234 SARIKA GOURMET COFFEE-MM S 09/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": "1",
            "credit_amount": "0",
            "description_1": "xx-1234 7-ELEVEN 117-00 SILOSO S 12/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": "54.6",
            "credit_amount": "0",
            "description_1": "xx-1234 SHAKE SHACK-VIVO S 12/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "29/7/2021",
            "debit_amount": "19.4",
            "credit_amount": "0",
            "description_1": "xx-1234 COLD STORAGE NAC S 26/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "29/7/2021",
            "debit_amount": "33.65",
            "credit_amount": "0",
            "description_1": "xx-1234 PIZZA EXPRESS SS S 26/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "29/7/2021",
            "debit_amount": "8.8",
            "credit_amount": "0",
            "description_1": "xx-1234 TAKASHIMAYA (S) LTD S 26/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "29/7/2021",
            "debit_amount": "3.5",
            "credit_amount": "0",
            "description_1": "xx-1234 TAKASHIMAYA (S) LTD S 26/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "29/7/2021",
            "debit_amount": "18",
            "credit_amount": "0",
            "description_1": "xx-1234 TSUTA SPORE-313@SOMERSET S 26/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "3/8/2021",
            "debit_amount": "8.4",
            "credit_amount": "0",
            "description_1": "xx-1234 BURGER KING - WEST COAST S 30/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "9/8/2021",
            "debit_amount": "26.32",
            "credit_amount": "0",
            "description_1": "xx-1234 SUSHI-TEI @WEST COAST S 06/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "13/8/2021",
            "debit_amount": "5.9",
            "credit_amount": "0",
            "description_1": "xx-1234 KOUFU PTE LTD S 10/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "13/8/2021",
            "debit_amount": "6.2",
            "credit_amount": "0",
            "description_1": "xx-1234 KOUFU PTE LTD S 10/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "16/8/2021",
            "debit_amount": "31.24",
            "credit_amount": "0",
            "description_1": "xx-1234 AJI ICHI JAPANESE CASU S 13/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "17/8/2021",
            "debit_amount": "103.4",
            "credit_amount": "0",
            "description_1": "xx-1234 YAKINIKU LIKE-CLM MALL S 14/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "19/8/2021",
            "debit_amount": "91.8",
            "credit_amount": "0",
            "description_1": "xx-1234 SEO CHON KOREA REST -MM S 16/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": "13",
            "credit_amount": "0",
            "description_1": "xx-1234 IKEA RESTAURANT / SFM - JS 19/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "30/8/2021",
            "debit_amount": "100",
            "credit_amount": "0",
            "description_1": "xx-1234 KISEKI - ORCHARD CENTRAL S 27/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "10/9/2021",
            "debit_amount": "12.7",
            "credit_amount": "0",
            "description_1": "xx-1234 MCDONALD'S (WCP) S 08/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "23/9/2021",
            "debit_amount": "95.35",
            "credit_amount": "0",
            "description_1": "xx-1234 PASTA BAR S 22/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "26/9/2021",
            "debit_amount": "43.08",
            "credit_amount": "0",
            "description_1": "xx-1234 WTRAJUMMAS-FUNAN 6 23/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "1/10/2021",
            "debit_amount": "7.05",
            "credit_amount": "0",
            "description_1": "xx-1234 MCDONALD'S (WCP) S 29/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Food & Drinks"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": "0",
            "credit_amount": "2.8",
            "description_1": "OTHR - Chicken Wing from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": "2.26",
            "credit_amount": "0",
            "description_1": "OTHR - grab to Ron via PayNow-Mobile",
            "description_2": "FAST PAYMENT",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": "3.7",
            "credit_amount": "0",
            "description_1": "OTHR - liho to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": "16.35",
            "credit_amount": "0",
            "description_1": "OTHR - mala to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": "0",
            "credit_amount": "2.8",
            "description_1": "OTHR Send back9 from Amirah via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": "0",
            "credit_amount": "0.8",
            "description_1": "OTHR Send back9 from Ron via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "2/5/2021",
            "debit_amount": "0",
            "credit_amount": "500",
            "description_1": "OTHR ACK from Ackmah DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "5/5/2021",
            "debit_amount": "30.61",
            "credit_amount": "0",
            "description_1": "OTHR - oppa bbq to Kermit via PayNow-Mobile",
            "description_2": "FAST PAYMENT",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "8/5/2021",
            "debit_amount": "16",
            "credit_amount": "0",
            "description_1": "OTHR - GPay- to Ciel via PayNow-Mobile",
            "description_2": "FAST PAYMENT",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "8/5/2021",
            "debit_amount": "16.5",
            "credit_amount": "0",
            "description_1": "OTHR - GPay- to Joel via PayNow-Mobile",
            "description_2": "FAST PAYMENT",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "8/5/2021",
            "debit_amount": "2",
            "credit_amount": "0",
            "description_1": "OTHR - GPay- to Min via PayNow-Mobile",
            "description_2": "FAST PAYMENT",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "11/5/2021",
            "debit_amount": "0",
            "credit_amount": "14.25",
            "description_1": "OTHR - ikea from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "24/5/2021",
            "debit_amount": "1",
            "credit_amount": "0",
            "description_1": "OTHR - Toto qp to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "1/6/2021",
            "debit_amount": "250",
            "credit_amount": "0",
            "description_1": "OTHR - MB725GMG to ASIA WEALTH PLAT via PayNow-UEN",
            "description_2": "FAST PAYMENT",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "1/6/2021",
            "debit_amount": "0",
            "credit_amount": "500",
            "description_1": "OTHR ACK from Ackmah DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "18/6/2021",
            "debit_amount": "22.5",
            "credit_amount": "0",
            "description_1": "OTHR - GPay- to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "18/6/2021",
            "debit_amount": "0",
            "credit_amount": "23.41",
            "description_1": "OTHR - Lunch + Dinner at Kermit's from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": "0",
            "credit_amount": "11.71",
            "description_1": "OTHR Send back from Andy via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "20/6/2021",
            "debit_amount": "0",
            "credit_amount": "67.32",
            "description_1": "OTHR PayNow Transfer from Kermit via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "24/6/2021",
            "debit_amount": "0",
            "credit_amount": "18.59",
            "description_1": "OTHR - AHTTI from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "1/7/2021",
            "debit_amount": "0",
            "credit_amount": "500",
            "description_1": "OTHR ACK from Ackmah DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "5/7/2021",
            "debit_amount": "8",
            "credit_amount": "0",
            "description_1": "OTHR - coffee beans to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "6/7/2021",
            "debit_amount": "31.5",
            "credit_amount": "0",
            "description_1": "OTHR - isteak to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "6/7/2021",
            "debit_amount": "0",
            "credit_amount": "104.5",
            "description_1": "OTHR Send back 96749777 from Amirah via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "9/7/2021",
            "debit_amount": "0",
            "credit_amount": "13.5",
            "description_1": "OTHR - A&W from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "9/7/2021",
            "debit_amount": "0",
            "credit_amount": "10",
            "description_1": "OTHR - Suzuki from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "9/7/2021",
            "debit_amount": "0",
            "credit_amount": "13.2",
            "description_1": "OTHR - Wanchai Hong Kong Tea Roo from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "12/7/2021",
            "debit_amount": "0",
            "credit_amount": "17.6",
            "description_1": "OTHR - Shake Shack from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "12/7/2021",
            "debit_amount": "0",
            "credit_amount": "19",
            "description_1": "OTHR Send back from Amirah via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "14/7/2021",
            "debit_amount": "0",
            "credit_amount": "1.3",
            "description_1": "OTHR Send back from Amirah via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": "66.5",
            "credit_amount": "0",
            "description_1": "OTHR - yotel staycay to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "16/7/2021",
            "debit_amount": "8.1",
            "credit_amount": "0",
            "description_1": "OTHR - Galaxy buds case to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "16/7/2021",
            "debit_amount": "0",
            "credit_amount": "7",
            "description_1": "OTHR - Lunch from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "26/7/2021",
            "debit_amount": "0",
            "credit_amount": "9",
            "description_1": "OTHR - Dinner from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "26/7/2021",
            "debit_amount": "0",
            "credit_amount": "16.15",
            "description_1": "OTHR - Pizza Express from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "26/7/2021",
            "debit_amount": "0",
            "credit_amount": "17.4",
            "description_1": "OTHR - Soju+Bread from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "27/7/2021",
            "debit_amount": "11.85",
            "credit_amount": "0",
            "description_1": "OTHR - mui kee to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "30/7/2021",
            "debit_amount": "5",
            "credit_amount": "0",
            "description_1": "OTHR - skipping rope to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "1/8/2021",
            "debit_amount": "0",
            "credit_amount": "500",
            "description_1": "OTHR ACK from Ackmah DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "2/8/2021",
            "debit_amount": "3.54",
            "credit_amount": "0",
            "description_1": "OTHR - r&b to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "3/8/2021",
            "debit_amount": "0",
            "credit_amount": "13",
            "description_1": "OTHR - Addison Present from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "3/8/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "OTHR - PayNow Transfer to John via PayNow-Other",
            "description_2": "FAST PAYMENT",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "4/8/2021",
            "debit_amount": "0",
            "credit_amount": "12.95",
            "description_1": "OTHR - Pho from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "6/8/2021",
            "debit_amount": "0",
            "credit_amount": "11.55",
            "description_1": "OTHR - Other from Anya via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "10/8/2021",
            "debit_amount": "0",
            "credit_amount": "3.8",
            "description_1": "OTHR - 3 layer tea from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "11/8/2021",
            "debit_amount": "2,700.00",
            "credit_amount": "0",
            "description_1": "OTHR - Other to Futu Singapore P 885069673530",
            "description_2": "FAST PAYMENT",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "11/8/2021",
            "debit_amount": "0",
            "credit_amount": "2,200.00",
            "description_1": "OTHR 570f4 from Futu Singapore DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "12/8/2021",
            "debit_amount": "9.1",
            "credit_amount": "0",
            "description_1": "OTHR - Dinner to Anya via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "13/8/2021",
            "debit_amount": "0",
            "credit_amount": "14",
            "description_1": "OTHR - Aji Ichi from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "13/8/2021",
            "debit_amount": "0",
            "credit_amount": "18",
            "description_1": "OTHR - GBTB from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "13/8/2021",
            "debit_amount": "0",
            "credit_amount": "8",
            "description_1": "OTHR - Satay and Chicken Wings - from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "14/8/2021",
            "debit_amount": "0",
            "credit_amount": "16.7",
            "description_1": "OTHR PayNow Transfer from Keith via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "14/8/2021",
            "debit_amount": "0",
            "credit_amount": "22.3",
            "description_1": "OTHR Send back from CJ via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "14/8/2021",
            "debit_amount": "0",
            "credit_amount": "22.3",
            "description_1": "OTHR Send back from Tan Wei Xiang via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "14/8/2021",
            "debit_amount": "0",
            "credit_amount": "22.5",
            "description_1": "OTHR Send back from Zero via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "14/8/2021",
            "debit_amount": "0",
            "credit_amount": "9.7",
            "description_1": "OTHR Send back from Zero via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "16/8/2021",
            "debit_amount": "0",
            "credit_amount": "30.6",
            "description_1": "OTHR - Lunch kbbq from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "16/8/2021",
            "debit_amount": "100",
            "credit_amount": "0",
            "description_1": "OTHR - QR210317368BBDC8848B to BUKIT BATOK DRIV via PayNow-UEN",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "16/8/2021",
            "debit_amount": "5.38",
            "credit_amount": "0",
            "description_1": "OTHR - resistance band to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "16/8/2021",
            "debit_amount": "0",
            "credit_amount": "30.6",
            "description_1": "OTHR Send back from Amirah via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "17/8/2021",
            "debit_amount": "150",
            "credit_amount": "0",
            "description_1": "OTHR - QR210318164BBDCD9E4C to BUKIT BATOK DRIV via PayNow-UEN",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "17/8/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "OTHR - QR210318172BBDC26B07 to BUKIT BATOK DRIV via PayNow-UEN",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": "22.4",
            "credit_amount": "0",
            "description_1": "OTHR - Collin's to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "23/8/2021",
            "debit_amount": "2.7",
            "credit_amount": "0",
            "description_1": "OTHR - each a cup to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "23/8/2021",
            "debit_amount": "19.1",
            "credit_amount": "0",
            "description_1": "OTHR - zzang Korean food to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "26/8/2021",
            "debit_amount": "0",
            "credit_amount": "6",
            "description_1": "OTHR - Other from Anya via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": "1.5",
            "credit_amount": "0",
            "description_1": "OTHR - drink to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": "0",
            "credit_amount": "25",
            "description_1": "OTHR - Kiseki from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": "0",
            "credit_amount": "25",
            "description_1": "OTHR Send back from Amirah via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": "0",
            "credit_amount": "25",
            "description_1": "OTHR PayNow Transfer from Ken via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "30/8/2021",
            "debit_amount": "11.63",
            "credit_amount": "0",
            "description_1": "OTHR - mala and drink to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "30/8/2021",
            "debit_amount": "0",
            "credit_amount": "11.9",
            "description_1": "OTHR - saizeriya from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "2/9/2021",
            "debit_amount": "0",
            "credit_amount": "500",
            "description_1": "OTHR ACK from Ackmah DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": "26.4",
            "credit_amount": "0",
            "description_1": "OTHR - ajiya to Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": "0",
            "credit_amount": "1.3",
            "description_1": "OTHR - teh from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "8/9/2021",
            "debit_amount": "0",
            "credit_amount": "5.8",
            "description_1": "OTHR - Mcdonalds from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "9/9/2021",
            "debit_amount": "220",
            "credit_amount": "0",
            "description_1": "OTHR - PayNow Transfer to John via PayNow-Other",
            "description_2": "FAST PAYMENT",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "9/9/2021",
            "debit_amount": "0",
            "credit_amount": "150",
            "description_1": "OTHR PAX 75621438 John from John GPNT",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "16/9/2021",
            "debit_amount": "0",
            "credit_amount": "1.2",
            "description_1": "OTHR Drinks Leon from Leon via PayNow-DBSS",
            "description_2": "PAYMENT/TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "22/9/2021",
            "debit_amount": "0",
            "credit_amount": "26.84",
            "description_1": "OTHR - Ahjumma?s from Alex via PayNow-Mobile",
            "description_2": "FUND TRANSFER",
            "category": "Peer-to-peer"
        },
        {
            "transaction_date": "9/7/2021",
            "debit_amount": "104.8",
            "credit_amount": "0",
            "description_1": "xx-1234 UNIQLO SINGAPORE PTE. L S 06/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Shopping"
        },
        {
            "transaction_date": "17/8/2021",
            "debit_amount": "19.75",
            "credit_amount": "0",
            "description_1": "xx-1234 GUARDIAN-COMMONWEALTH S 14/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Shopping"
        },
        {
            "transaction_date": "6/5/2021",
            "debit_amount": "25",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab 8994520647faed07 S 04/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "6/5/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab aa8c0507939b7df1 S 04/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "6/5/2021",
            "debit_amount": "4.5",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-XUV9AP6GWE8D S 04/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "9/5/2021",
            "debit_amount": "3.3",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-XVBQJWHWWILA S 07/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab 85348cc5a0b564d0 S 10/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "13/5/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab a48b3f798132cddc S 11/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "13/5/2021",
            "debit_amount": "0.3",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-XVSBTOOWWGX9 S 11/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "14/5/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 EZ-LINK APP S 11/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "19/5/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab a6bc1b3a4683e9f5 S 17/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "19/5/2021",
            "debit_amount": "5.8",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-2WL6GTRWWFFS S 17/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "20/5/2021",
            "debit_amount": "11.3",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-2WP7F38WWHEN S 18/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "22/5/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab 81e7052aba88df73 S 20/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "24/5/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab 835a67d519cb585e S 22/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "26/5/2021",
            "debit_amount": "11.55",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-2XHQDWEWWI74 S 24/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "30/5/2021",
            "debit_amount": "15.2",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-222DPA5WWJDX S 28/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "3/6/2021",
            "debit_amount": "13.7",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-22INFTOWWEF3 S 01/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "8/6/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab a6be1065b48eed6f S 05/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "10/6/2021",
            "debit_amount": "14.99",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-23FIHR9GWEQD S 08/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": "20",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab 96b4b25d45b4db78 S 14/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "17/6/2021",
            "debit_amount": "19.7",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-24CDPO7GWHWT S 15/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "23/6/2021",
            "debit_amount": "12.1",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab ADR-2552EODGWJLP S 21/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "26/6/2021",
            "debit_amount": "20",
            "credit_amount": "0",
            "description_1": "xx-1234 EZ-LINK APP S 24/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "26/6/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab 848149ec26efa88f S 24/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": "23.5",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-25LE5LQGWF7K S 25/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": "14.4",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-26XVKU2WWG4F S 28/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "2/7/2021",
            "debit_amount": "16.1",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-26A4PMJGWGMV S 30/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "9/7/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab 94821081857ddaad S 06/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "14/7/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab 8634415b7bbeb032 S 11/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": "20",
            "credit_amount": "0",
            "description_1": "xx-1234 EZ-LINK APP S 13/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "16/7/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab 9a9a9e4ab8990ae0 S 13/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "16/7/2021",
            "debit_amount": "12.9",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-283ROM4GWI2K S 14/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "17/7/2021",
            "debit_amount": "15.1",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-287UAHGGWG4F S 15/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": "2.56",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 88680938 S 16/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "23/7/2021",
            "debit_amount": "14.45",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-29WMUCIGWH9D S 21/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "24/7/2021",
            "debit_amount": "15.2",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-294O3VNWWIW4 S 22/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "1/8/2021",
            "debit_amount": "1.52",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 90119459 S 26/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "2/8/2021",
            "debit_amount": "1.6",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 90207753 S 27/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "4/8/2021",
            "debit_amount": "14.8",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-2AIWCVQGWFDA S 02/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "5/8/2021",
            "debit_amount": "4.42",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 90628373 S 30/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "5/8/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab aa745ae83b772cb0 S 03/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "6/8/2021",
            "debit_amount": "28.9",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-2AQRX64GWHSM S 04/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "7/8/2021",
            "debit_amount": "10",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab a10d15803ad62a15 S 05/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "8/8/2021",
            "debit_amount": "5.41",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 91230866 S 02/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "10/8/2021",
            "debit_amount": "50",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab bad2f7b07eeb5346 S 07/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "15/8/2021",
            "debit_amount": "2.24",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 92211870 S 09/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "16/8/2021",
            "debit_amount": "2.44",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 92405600 S 10/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "19/8/2021",
            "debit_amount": "7.8",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 92755595 S 13/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": "1.84",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 92943754 S 14/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "21/8/2021",
            "debit_amount": "14.3",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-2CO8XVTGWHN5 S 19/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "22/8/2021",
            "debit_amount": "1.31",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 93232807 S 16/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "22/8/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab a85792aa95a2a271 S 19/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "29/8/2021",
            "debit_amount": "2.6",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 94345254 S 23/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "1/9/2021",
            "debit_amount": "22.8",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-2E5OP9KGWFPQ S 30/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "2/9/2021",
            "debit_amount": "2.48",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 95114971 S 27/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": "11.4",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-2EDQPNOGWHVA S 01/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "5/9/2021",
            "debit_amount": "1.84",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 95576131 S 30/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "9/9/2021",
            "debit_amount": "4.64",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 96304849 S 03/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "12/9/2021",
            "debit_amount": "3.71",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 96819661 S 06/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "13/9/2021",
            "debit_amount": "3.1",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 96947825 S 07/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "16/9/2021",
            "debit_amount": "3.1",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 97350122 S 09/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "16/9/2021",
            "debit_amount": "3.1",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 97486615 S 10/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "19/9/2021",
            "debit_amount": "3.6",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 98088700 S 13/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "20/9/2021",
            "debit_amount": "3.1",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 98198389 S 14/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "22/9/2021",
            "debit_amount": "15.3",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-2GRMHXJGWF7J S 20/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "23/9/2021",
            "debit_amount": "3.1",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 98564789 S 16/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "26/9/2021",
            "debit_amount": "3.71",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 99200743 S 20/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "26/9/2021",
            "debit_amount": "12.6",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-2HCF3JUWWFKV S 24/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "27/9/2021",
            "debit_amount": "3.43",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 99427306 S 21/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "28/9/2021",
            "debit_amount": "5.14",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 99536007 S 22/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "29/9/2021",
            "debit_amount": "14.8",
            "credit_amount": "0",
            "description_1": "xx-1234 Grab A-2HOLWP9GWGKV S 27/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "30/9/2021",
            "debit_amount": "3.1",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 99686059 S 23/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "1/10/2021",
            "debit_amount": "2.14",
            "credit_amount": "0",
            "description_1": "xx-1234 BUS/MRT 100053413 S 25/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Transport"
        },
        {
            "transaction_date": "25/6/2021",
            "debit_amount": "20",
            "credit_amount": "0",
            "description_1": "OCBC-HAW PAR VILLA MRT SINGAPORE VIA PAY ANYONE QR",
            "description_2": "CASH WITHDRAWAL ATM",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "1/7/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "OCBC-NG TENG FONG HOSP SINGAPORE VIA PAY ANYONE QR",
            "description_2": "CASH WITHDRAWAL ATM",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "16/7/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "OCBC-COMMONWEALTH MRT SINGAPORE VIA PAY ANYONE QR",
            "description_2": "CASH WITHDRAWAL ATM",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "28/7/2021",
            "debit_amount": "20",
            "credit_amount": "0",
            "description_1": "OCBC-WEST COAST PLAZA SINGAPORE VIA PAY ANYONE QR",
            "description_2": "CASH WITHDRAWAL ATM",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "13/8/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "OCBC-CLEMENTI BRANCH SINGAPORE VIA PAY ANYONE QR",
            "description_2": "CASH WITHDRAWAL ATM",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "23/8/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "OCBC-CLEMENTI MRT SINGAPORE VIA PAY ANYONE QR",
            "description_2": "CASH WITHDRAWAL ATM",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "OCBC-CLEMENTI MRT SINGAPORE VIA QR CODE",
            "description_2": "CASH WITHDRAWAL ATM",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "16/9/2021",
            "debit_amount": "20",
            "credit_amount": "0",
            "description_1": "OCBC-HAW PAR VILLA MRT SINGAPORE VIA QR CODE",
            "description_2": "CASH WITHDRAWAL ATM",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "20/9/2021",
            "debit_amount": "30",
            "credit_amount": "0",
            "description_1": "xx-1234 UOB Yio Chu Kang MRT 1st",
            "description_2": "CASH WITHDRAWAL SATM",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "28/5/2021",
            "debit_amount": "0.14",
            "credit_amount": "0",
            "description_1": "FOR: 4.99 SGD",
            "description_2": "CCY CONVERSION FEE",
            "category": "Conversion Fee"
        },
        {
            "transaction_date": "8/6/2021",
            "debit_amount": "0.04",
            "credit_amount": "0",
            "description_1": "FOR: 1.50 SGD",
            "description_2": "CCY CONVERSION FEE",
            "category": "Conversion Fee"
        },
        {
            "transaction_date": "28/6/2021",
            "debit_amount": "0.14",
            "credit_amount": "0",
            "description_1": "FOR: 4.99 SGD",
            "description_2": "CCY CONVERSION FEE",
            "category": "Conversion Fee"
        },
        {
            "transaction_date": "28/7/2021",
            "debit_amount": "0.14",
            "credit_amount": "0",
            "description_1": "FOR: 4.99 SGD",
            "description_2": "CCY CONVERSION FEE",
            "category": "Conversion Fee"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": "0.21",
            "credit_amount": "0",
            "description_1": "FOR: 7.57 SGD",
            "description_2": "CCY CONVERSION FEE",
            "category": "Conversion Fee"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": "0.14",
            "credit_amount": "0",
            "description_1": "FOR: 4.99 SGD",
            "description_2": "CCY CONVERSION FEE",
            "category": "Conversion Fee"
        },
        {
            "transaction_date": "28/9/2021",
            "debit_amount": "0.14",
            "credit_amount": "0",
            "description_1": "FOR: 4.99 SGD",
            "description_2": "CCY CONVERSION FEE",
            "category": "Conversion Fee"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": "0",
            "credit_amount": "0.7",
            "description_1": "Interest",
            "description_2": "INTEREST CREDIT",
            "category": "Interest"
        },
        {
            "transaction_date": "31/5/2021",
            "debit_amount": "0",
            "credit_amount": "0.72",
            "description_1": "Interest",
            "description_2": "INTEREST CREDIT",
            "category": "Interest"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": "0",
            "credit_amount": "0.68",
            "description_1": "Interest",
            "description_2": "INTEREST CREDIT",
            "category": "Interest"
        },
        {
            "transaction_date": "31/7/2021",
            "debit_amount": "0",
            "credit_amount": "0.7",
            "description_1": "Interest",
            "description_2": "INTEREST CREDIT",
            "category": "Interest"
        },
        {
            "transaction_date": "31/8/2021",
            "debit_amount": "0",
            "credit_amount": "0.72",
            "description_1": "Interest",
            "description_2": "INTEREST CREDIT",
            "category": "Interest"
        },
        {
            "transaction_date": "30/9/2021",
            "debit_amount": "0",
            "credit_amount": "0.66",
            "description_1": "Interest",
            "description_2": "INTEREST CREDIT",
            "category": "Interest"
        },
        {
            "transaction_date": "18/5/2021",
            "debit_amount": "0",
            "credit_amount": "36",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "20/5/2021",
            "debit_amount": "0",
            "credit_amount": "7",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "1/6/2021",
            "debit_amount": "0",
            "credit_amount": "29.25",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "1/6/2021",
            "debit_amount": "250",
            "credit_amount": "0",
            "description_1": "RoboInvest A/c RoboInvest A/c OTHR Arok",
            "description_2": "FAST TRANSFER",
            "category": "Investment"
        },
        {
            "transaction_date": "1/6/2021",
            "debit_amount": "250",
            "credit_amount": "0",
            "description_1": "RoboInvest A/c RoboInvest A/c OTHR Arok",
            "description_2": "FAST TRANSFER",
            "category": "Investment"
        },
        {
            "transaction_date": "9/6/2021",
            "debit_amount": "0",
            "credit_amount": "4.91",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "9/6/2021",
            "debit_amount": "0",
            "credit_amount": "13.28",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "13/7/2021",
            "debit_amount": "563.03",
            "credit_amount": "0",
            "description_1": "81595333001 0 600000 O CBC Securities Pte",
            "description_2": "GIRO",
            "category": "Investment"
        },
        {
            "transaction_date": "27/7/2021",
            "debit_amount": "0",
            "credit_amount": "1,588.17",
            "description_1": "81605821401 0 600000 O CBC Securities Pte",
            "description_2": "GIRO",
            "category": "Investment"
        },
        {
            "transaction_date": "30/7/2021",
            "debit_amount": "1,000.00",
            "credit_amount": "0",
            "description_1": "2021073003061776 via Internet Ba nkin",
            "description_2": "UT PURCHASE",
            "category": "Investment"
        },
        {
            "transaction_date": "2/8/2021",
            "debit_amount": "0",
            "credit_amount": "22.13",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "10/8/2021",
            "debit_amount": "0",
            "credit_amount": "5,000.00",
            "description_1": "Maturity",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "14/8/2021",
            "debit_amount": "5,000.00",
            "credit_amount": "0",
            "description_1": "OCBC-ONLINE BANKING ISSUE CODE:BS21116S",
            "description_2": "SGS APPLICATION",
            "category": "Investment"
        },
        {
            "transaction_date": "18/8/2021",
            "debit_amount": "0",
            "credit_amount": "19.2",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "18/8/2021",
            "debit_amount": "0",
            "credit_amount": "24.73",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "19/8/2021",
            "debit_amount": "0",
            "credit_amount": "7.5",
            "description_1": "ISSUE CODE:BS21116S",
            "description_2": "SGS DIS/PRE REFUND",
            "category": "Investment"
        },
        {
            "transaction_date": "25/8/2021",
            "debit_amount": "0",
            "credit_amount": "13.2",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "25/8/2021",
            "debit_amount": "0",
            "credit_amount": "2",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "25/8/2021",
            "debit_amount": "0",
            "credit_amount": "2",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": "0",
            "credit_amount": "1.83",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": "0",
            "credit_amount": "4.58",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": "0",
            "credit_amount": "0.15",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "7/9/2021",
            "debit_amount": "0",
            "credit_amount": "9.31",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "27/9/2021",
            "debit_amount": "0",
            "credit_amount": "3.51",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "27/9/2021",
            "debit_amount": "0",
            "credit_amount": "14.7",
            "description_1": "Dividend",
            "description_2": "CDP",
            "category": "Investment"
        },
        {
            "transaction_date": "28/5/2021",
            "debit_amount": "4.99",
            "credit_amount": "0",
            "description_1": "xx-1234 PAYPAL *SPOTIFY 3 25/05/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Subscription"
        },
        {
            "transaction_date": "28/6/2021",
            "debit_amount": "4.99",
            "credit_amount": "0",
            "description_1": "xx-1234 PAYPAL *SPOTIFY 3 25/06/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Subscription"
        },
        {
            "transaction_date": "28/7/2021",
            "debit_amount": "4.99",
            "credit_amount": "0",
            "description_1": "xx-1234 PAYPAL *SPOTIFY 3 25/07/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Subscription"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": "4.99",
            "credit_amount": "0",
            "description_1": "xx-1234 PAYPAL *SPOTIFY 3 25/08/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Subscription"
        },
        {
            "transaction_date": "28/9/2021",
            "debit_amount": "4.99",
            "credit_amount": "0",
            "description_1": "xx-1234 PAYPAL *SPOTIFY AB 3 25/09/21",
            "description_2": "DEBIT PURCHASE",
            "category": "Subscription"
        }
    ]
}, {
    "account_id": 1002,
    "date_registered": "30/10/2021",
    "name": "Bryan Ong",
    "bank_name": "DBS",
    "password": "password123",
    "balance": 2000,
    "email": "bo@gmail.com",
    "transactions": [{
            "transaction_date": "4/5/2021",
            "debit_amount": 0,
            "credit_amount": 600,
            "description_1": "I-BANK",
            "description_2": "Richard",
            "category": "Deposits"
        },
        {
            "transaction_date": "17/6/2021",
            "debit_amount": 0,
            "credit_amount": 550,
            "description_1": "I-BANK",
            "description_2": "Richard",
            "category": "Deposits"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 0,
            "credit_amount": 800,
            "description_1": "I-BANK",
            "description_2": "Richard",
            "category": "Deposits"
        },
        {
            "transaction_date": "12/8/2021",
            "debit_amount": 0,
            "credit_amount": 700,
            "description_1": "I-BANK",
            "description_2": "Richard",
            "category": "Deposits"
        },
        {
            "transaction_date": "13/9/2021",
            "debit_amount": 0,
            "credit_amount": 600,
            "description_1": "I-BANK",
            "description_2": "Richard",
            "category": "Deposits"
        },
        {
            "transaction_date": "4/5/2021",
            "debit_amount": 31.25,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 30APR",
            "description_2": "1123-2234-5544-7755 TRY184.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "16/5/2021",
            "debit_amount": 10.7,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 14MAY",
            "description_2": "1123-2234-5544-7755 TRY64.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "16/5/2021",
            "debit_amount": 5.59,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 14MAY",
            "description_2": "1123-2234-5544-7755 TRY33.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "16/5/2021",
            "debit_amount": 59.25,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 14MAY",
            "description_2": "1123-2234-5544-7755 TRY359.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "21/5/2021",
            "debit_amount": 16.45,
            "credit_amount": 0,
            "description_1": "PAYPAL *STEAM GAMES 35 31 18MAY",
            "description_2": "1123-2234-5544-7755",
            "category": "Entertainment"
        },
        {
            "transaction_date": "22/5/2021",
            "debit_amount": 1.16,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 20MAY",
            "description_2": "1123-2234-5544-7755 TRY6.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "22/5/2021",
            "debit_amount": 1.16,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 20MAY",
            "description_2": "1123-2234-5544-7755 TRY6.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 5.5,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 17JUN",
            "description_2": "1123-2234-5544-7755 TRY33.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "16/7/2021",
            "debit_amount": 61.68,
            "credit_amount": 0,
            "description_1": "PAYPAL *STEAM GAMES 35 31 13JUL",
            "description_2": "1123-2234-5544-7755",
            "category": "Entertainment"
        },
        {
            "transaction_date": "20/7/2021",
            "debit_amount": 5.62,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 18JUL",
            "description_2": "1123-2234-5544-7755 TRY33.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "3/8/2021",
            "debit_amount": 35.92,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 31JUL",
            "description_2": "1123-2234-5544-7755 TRY214.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "11/8/2021",
            "debit_amount": 15.41,
            "credit_amount": 0,
            "description_1": "PAYPAL *STEAM GAMES 35 31 08AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Entertainment"
        },
        {
            "transaction_date": "24/8/2021",
            "debit_amount": 5.76,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 21AUG",
            "description_2": "1123-2234-5544-7755 TRY33.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": 20.46,
            "credit_amount": 0,
            "description_1": "PAYPAL *STEAM GAMES 35 31 25AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Entertainment"
        },
        {
            "transaction_date": "16/9/2021",
            "debit_amount": 546.96,
            "credit_amount": 0,
            "description_1": "GOOGLE *ECOMI TECH LTD G. CO 14SEP",
            "description_2": "1123-2234-5544-7755 USD394.00",
            "category": "Entertainment"
        },
        {
            "transaction_date": "21/9/2021",
            "debit_amount": 15.21,
            "credit_amount": 0,
            "description_1": "PAYPAL *STEAM GAMES 35 31 17SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Entertainment"
        },
        {
            "transaction_date": "29/9/2021",
            "debit_amount": 5.54,
            "credit_amount": 0,
            "description_1": "GOOGLE *YOSTAR LIMITED G. CO 27SEP",
            "description_2": "1123-2234-5544-7755 TRY33.99",
            "category": "Entertainment"
        },
        {
            "transaction_date": "13/10/2021",
            "debit_amount": 61.68,
            "credit_amount": 0,
            "description_1": "PAYPAL *STEAM GAMES 35 31 11OCT",
            "description_2": "1123-2234-5544-7755",
            "category": "Entertainment"
        },
        {
            "transaction_date": "26/4/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Marcus",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "1/5/2021",
            "debit_amount": 6.2,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ben",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "1/5/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Brandon",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "2/5/2021",
            "debit_amount": 5.5,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Darren",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "4/5/2021",
            "debit_amount": 48,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ming",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "5/5/2021",
            "debit_amount": 16.1,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "ENAK ENAK HONGKONG TEAHOU",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "25/5/2021",
            "debit_amount": 6.9,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "15/6/2021",
            "debit_amount": 9.6,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 18,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 17,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Terry",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/6/2021",
            "debit_amount": 3.3,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Samuel",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": 6.3,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "ENAK ENAK HONGKONG TEAHOU",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": 3.8,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Darren",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "2/7/2021",
            "debit_amount": 7.01,
            "credit_amount": 0,
            "description_1": "PAYPAL *JUYUANZIHEW IN 40 29 30JUN",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/7/2021",
            "debit_amount": 9.6,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/7/2021",
            "debit_amount": 11.7,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "ENAK ENAK HONGKONG TEAHOU",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "14/7/2021",
            "debit_amount": 9.4,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "18/7/2021",
            "debit_amount": 8.9,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 6.4,
            "credit_amount": 0,
            "description_1": "CHEERS - TANAH MERAH SI NG 20JUL",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 9.9,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (EPM) SI NG 19JUL",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "30/7/2021",
            "debit_amount": 12,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "31/7/2021",
            "debit_amount": 100,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Brandon",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "19/8/2021",
            "debit_amount": 11.4,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "KOI",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": 3.1,
            "credit_amount": 0,
            "description_1": "CHEERS - KEMBANGAN MRT SI NG 18AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "21/8/2021",
            "debit_amount": 6.4,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (EPM) SI NG 18AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "23/8/2021",
            "debit_amount": 9.4,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "KOI THE SINGAPORE PTE LTD",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/8/2021",
            "debit_amount": 5.5,
            "credit_amount": 0,
            "description_1": "CHEERS - KEMBANGAN MRT SI NG 21AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "25/8/2021",
            "debit_amount": 2,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Darren",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "25/8/2021",
            "debit_amount": 5,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Sammy",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "26/8/2021",
            "debit_amount": 13,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Darren",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": 6000,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ryu",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": 3.3,
            "credit_amount": 0,
            "description_1": "CHEERS - TANAH MERAH SI NG 26AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "31/8/2021",
            "debit_amount": 5.5,
            "credit_amount": 0,
            "description_1": "CHEERS - KEMBANGAN MRT SI NG 28AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "1/9/2021",
            "debit_amount": 4.3,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/9/2021",
            "debit_amount": 3.3,
            "credit_amount": 0,
            "description_1": "CHEERS - TANAH MERAH SI NG 03SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "10/9/2021",
            "debit_amount": 3.5,
            "credit_amount": 0,
            "description_1": "7-ELEVEN-SIMEI MRT SI NG 08SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 3.5,
            "credit_amount": 0,
            "description_1": "7-ELEVEN-SIMEI MRT SI NG 09SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "13/9/2021",
            "debit_amount": 40,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Gab",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "14/9/2021",
            "debit_amount": 3.5,
            "credit_amount": 0,
            "description_1": "7-ELEVEN-SIMEI MRT SI NG 11SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "23/9/2021",
            "debit_amount": 19,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ben",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/9/2021",
            "debit_amount": 40,
            "credit_amount": 0,
            "description_1": "CHATERAISE SI NG 22SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/9/2021",
            "debit_amount": 1,
            "credit_amount": 0,
            "description_1": "CHEERS - KEMBANGAN MRT SI NG 22SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "25/9/2021",
            "debit_amount": 16.3,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Fanny",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "27/9/2021",
            "debit_amount": 94,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: gab",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "28/9/2021",
            "debit_amount": 3.3,
            "credit_amount": 0,
            "description_1": "CHEERS - TANAH MERAH SI NG 24SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "29/9/2021",
            "debit_amount": 4.1,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (EPM) SI NG 26SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "5/10/2021",
            "debit_amount": 22.3,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (BDML) SI NG 30SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/10/2021",
            "debit_amount": 35.6,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Derrick",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/10/2021",
            "debit_amount": 824,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Tom",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "8/10/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Nick",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "8/10/2021",
            "debit_amount": 135,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Nick",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "12/10/2021",
            "debit_amount": 42,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Sam",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "17/10/2021",
            "debit_amount": 16,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Gab",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "19/10/2021",
            "debit_amount": 61.09,
            "credit_amount": 0,
            "description_1": "SUSHI TEI - TBP SI NG 16OCT",
            "description_2": "1123-2234-5544-7755",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/10/2021",
            "debit_amount": 0,
            "credit_amount": 6.3,
            "description_1": "OTHR PayNow Transfer",
            "description_2": "Incoming PayNow Ref 7198855",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "27/4/2021",
            "debit_amount": 0,
            "credit_amount": 6.7,
            "description_1": "Incoming PayNow Ref 9341412",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "5/5/2021",
            "debit_amount": 0,
            "credit_amount": 6.3,
            "description_1": "Incoming PayNow Ref 9040404",
            "description_2": "From: Justin",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "6/5/2021",
            "debit_amount": 0,
            "credit_amount": 7,
            "description_1": "Incoming PayNow Ref 9559559",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "19/5/2021",
            "debit_amount": 0,
            "credit_amount": 6.5,
            "description_1": "Incoming PayNow Ref 5892380",
            "description_2": "From: Min",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "26/5/2021",
            "debit_amount": 0,
            "credit_amount": 5.6,
            "description_1": "Incoming PayNow Ref 8723256",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "4/6/2021",
            "debit_amount": 0,
            "credit_amount": 6.3,
            "description_1": "Incoming PayNow Ref 8171629",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 0,
            "credit_amount": 6.3,
            "description_1": "Incoming PayNow Ref 9913217",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "20/6/2021",
            "debit_amount": 0,
            "credit_amount": 4.8,
            "description_1": "Incoming PayNow Ref 8702466",
            "description_2": "From: Ben",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "20/6/2021",
            "debit_amount": 0,
            "credit_amount": 4.8,
            "description_1": "Incoming PayNow Ref 8702628",
            "description_2": "From: Joshua",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "21/6/2021",
            "debit_amount": 0,
            "credit_amount": 2.2,
            "description_1": "Incoming PayNow Ref 9955422",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 0,
            "credit_amount": 11.5,
            "description_1": "Incoming PayNow Ref 8069340",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 0,
            "credit_amount": 4.2,
            "description_1": "Incoming PayNow Ref 8071802",
            "description_2": "From: Sam",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 0,
            "credit_amount": 4.8,
            "description_1": "Incoming PayNow Ref 8075669",
            "description_2": "From: Ben",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "7/7/2021",
            "debit_amount": 0,
            "credit_amount": 4.5,
            "description_1": "Incoming PayNow Ref 7556599",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "7/7/2021",
            "debit_amount": 0,
            "credit_amount": 4.53,
            "description_1": "Incoming PayNow Ref 7559243",
            "description_2": "From: Ben",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "7/7/2021",
            "debit_amount": 0,
            "credit_amount": 1.7,
            "description_1": "Incoming PayNow Ref 8678924",
            "description_2": "From: Sam",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "8/7/2021",
            "debit_amount": 0,
            "credit_amount": 1.7,
            "description_1": "Incoming PayNow Ref 8710340",
            "description_2": "From: Terry",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "13/7/2021",
            "debit_amount": 0,
            "credit_amount": 7.25,
            "description_1": "Incoming PayNow Ref 9689367",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 0,
            "credit_amount": 3.8,
            "description_1": "Incoming PayNow Ref 6202313",
            "description_2": "From: Ben",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 0,
            "credit_amount": 3.8,
            "description_1": "Incoming PayNow Ref 6204388",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "16/7/2021",
            "debit_amount": 0,
            "credit_amount": 2.75,
            "description_1": "Incoming PayNow Ref 7904095",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "21/7/2021",
            "debit_amount": 0,
            "credit_amount": 6.8,
            "description_1": "Incoming PayNow Ref 7282603",
            "description_2": "From: Samuel",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "30/7/2021",
            "debit_amount": 0,
            "credit_amount": 5.8,
            "description_1": "Incoming PayNow Ref 6871078",
            "description_2": "From: Ben",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "4/8/2021",
            "debit_amount": 0,
            "credit_amount": 6.3,
            "description_1": "Incoming PayNow Ref 7951153",
            "description_2": "From: Ben",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "16/8/2021",
            "debit_amount": 0,
            "credit_amount": 2.75,
            "description_1": "Incoming PayNow Ref 6666300",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "21/8/2021",
            "debit_amount": 0,
            "credit_amount": 3,
            "description_1": "Incoming PayNow Ref 6527019",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "23/8/2021",
            "debit_amount": 0,
            "credit_amount": 3.5,
            "description_1": "Incoming PayNow Ref 8704099",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": 0,
            "credit_amount": 3.85,
            "description_1": "Incoming PayNow Ref 7532929",
            "description_2": "From: Tommy",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": 0,
            "credit_amount": 3.85,
            "description_1": "Incoming PayNow Ref 7533033",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 0,
            "credit_amount": 50,
            "description_1": "Incoming PayNow Ref 6274440",
            "description_2": "From: Sally",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "13/9/2021",
            "debit_amount": 0,
            "credit_amount": 122,
            "description_1": "Incoming PayNow Ref 8231656",
            "description_2": "From: PayLah! Bryan",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "23/9/2021",
            "debit_amount": 0,
            "credit_amount": 3.8,
            "description_1": "Incoming PayNow Ref 9089370",
            "description_2": "From: Darren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "25/9/2021",
            "debit_amount": 0,
            "credit_amount": 1.6,
            "description_1": "Incoming PayNow Ref 6283257",
            "description_2": "From: Ben",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "25/9/2021",
            "debit_amount": 0,
            "credit_amount": 24.5,
            "description_1": "Incoming PayNow Ref 6852033",
            "description_2": "From: Terry",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "26/9/2021",
            "debit_amount": 0,
            "credit_amount": 7.3,
            "description_1": "Incoming PayNow Ref 7552171",
            "description_2": "From: PayLah! Benny",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "30/9/2021",
            "debit_amount": 0,
            "credit_amount": 9.5,
            "description_1": "Incoming PayNow Ref 8264901",
            "description_2": "From: Justin",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "9/10/2021",
            "debit_amount": 0,
            "credit_amount": 2461.88,
            "description_1": "Incoming PayNow Ref 8205610",
            "description_2": "From: Terry",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "16/10/2021",
            "debit_amount": 0,
            "credit_amount": 30,
            "description_1": "Incoming PayNow Ref 2631141",
            "description_2": "From: Tom",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "20/6/2021",
            "debit_amount": 209,
            "credit_amount": 0,
            "description_1": "LAZADA SI NG 18JUN",
            "description_2": "1123-2234-5544-7755",
            "category": "Shopping"
        },
        {
            "transaction_date": "12/8/2021",
            "debit_amount": 58.41,
            "credit_amount": 0,
            "description_1": "OVOKEYS LO ND 10AUG",
            "description_2": "1123-2234-5544-7755 GBP29.99",
            "category": "Shopping"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": 14.22,
            "credit_amount": 0,
            "description_1": "LAZADA SINGAPORE SI NG 25AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Shopping"
        },
        {
            "transaction_date": "8/10/2021",
            "debit_amount": 31.39,
            "credit_amount": 0,
            "description_1": "LAZADA SI NG 06OCT",
            "description_2": "1123-2234-5544-7755",
            "category": "Shopping"
        },
        {
            "transaction_date": "15/10/2021",
            "debit_amount": 11.65,
            "credit_amount": 0,
            "description_1": "LAZADA SI NG 14OCT",
            "description_2": "1123-2234-5544-7755",
            "category": "Shopping"
        },
        {
            "transaction_date": "21/10/2021",
            "debit_amount": 100,
            "credit_amount": 0,
            "description_1": "OTHR PayNow Transfer",
            "description_2": "PayNow Transfer",
            "category": "Shopping"
        },
        {
            "transaction_date": "1/5/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB* 8A454FB0B0FBB5F3 SI NG 29APR",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "10/5/2021",
            "debit_amount": 11.1,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ben",
            "category": "Transport"
        },
        {
            "transaction_date": "15/5/2021",
            "debit_amount": 11.2,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Transport"
        },
        {
            "transaction_date": "28/5/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB* A5CD0E336F275812 SI NG 25MAY",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "22/6/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB* 8E72DF4CD352A17B SI NG 19JUN",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "26/6/2021",
            "debit_amount": 6.4,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Fanny",
            "category": "Transport"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB* 847CA67712AEE2CB SI NG 28JUN",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "3/7/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB* 9DC8374AFB1E312D SI NG 01JUL",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Transport"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 17.09,
            "credit_amount": 0,
            "description_1": "BUS/MRT 87610624 SI NG 07JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "20/7/2021",
            "debit_amount": 14.5,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Transport"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 18.09,
            "credit_amount": 0,
            "description_1": "BUS/MRT 88542984 SI NG 12JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "25/7/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB* 8D49E639A4E3305C SI NG 23JUL",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "27/7/2021",
            "debit_amount": 10.49,
            "credit_amount": 0,
            "description_1": "BUS/MRT 89341272 SI NG 17JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "31/7/2021",
            "debit_amount": 14.22,
            "credit_amount": 0,
            "description_1": "BUS/MRT 90025566 SI NG 22JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "4/8/2021",
            "debit_amount": 11,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Transport"
        },
        {
            "transaction_date": "5/8/2021",
            "debit_amount": 13.43,
            "credit_amount": 0,
            "description_1": "BUS/MRT 90699348 SI NG 27JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "6/8/2021",
            "debit_amount": 3.67,
            "credit_amount": 0,
            "description_1": "BUS/MRT 90963624 SI NG 01AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "8/8/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: John",
            "category": "Transport"
        },
        {
            "transaction_date": "15/8/2021",
            "debit_amount": 2.76,
            "credit_amount": 0,
            "description_1": "BUS/MRT 92277014 SI NG 06AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "19/8/2021",
            "debit_amount": 8,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Joshua",
            "category": "Transport"
        },
        {
            "transaction_date": "21/8/2021",
            "debit_amount": 5.2,
            "credit_amount": 0,
            "description_1": "BUS/MRT 93172022 SI NG 12AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB* 8488C6E28CA1D246 SI NG 26AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "1/9/2021",
            "debit_amount": 5.88,
            "credit_amount": 0,
            "description_1": "BUS/MRT 94982651 SI NG 23AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "6/9/2021",
            "debit_amount": 9,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Transport"
        },
        {
            "transaction_date": "7/9/2021",
            "debit_amount": 7.28,
            "credit_amount": 0,
            "description_1": "BUS/MRT 95856392 SI NG 28AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 7.45,
            "credit_amount": 0,
            "description_1": "BUS/MRT 96745731 SI NG 02SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "14/9/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB* 8708FB07B2A8C1CD SI NG 12SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "14/9/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB* AFA1648F238DD76B SI NG 12SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "17/9/2021",
            "debit_amount": 12.5,
            "credit_amount": 0,
            "description_1": "BUS/MRT 97809762 SI NG 08SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "23/9/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ben",
            "category": "Transport"
        },
        {
            "transaction_date": "23/9/2021",
            "debit_amount": 13.04,
            "credit_amount": 0,
            "description_1": "BUS/MRT 98818113 SI NG 14SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "26/9/2021",
            "debit_amount": 5.7,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Justin",
            "category": "Transport"
        },
        {
            "transaction_date": "28/9/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "GRAB SI NG 26SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Transport"
        },
        {
            "transaction_date": "5/10/2021",
            "debit_amount": 11.48,
            "credit_amount": 0,
            "description_1": "BUS/MRT 100585368 SI NG 25SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "9/10/2021",
            "debit_amount": 5.82,
            "credit_amount": 0,
            "description_1": "BUS/MRT 101319279 SI NG 30SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "14/10/2021",
            "debit_amount": 13.72,
            "credit_amount": 0,
            "description_1": "BUS/MRT 102057976 SI NG 05OCT",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "16/10/2021",
            "debit_amount": 9,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Dom",
            "category": "Transport"
        },
        {
            "transaction_date": "21/10/2021",
            "debit_amount": 14.45,
            "credit_amount": 0,
            "description_1": "BUS/MRT 103109332 SI NG 12OCT",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "22/10/2021",
            "debit_amount": 16.2,
            "credit_amount": 0,
            "description_1": "OTHR PayNow Transfer",
            "description_2": "PayNow Transfer",
            "category": "Transport"
        },
        {
            "transaction_date": "26/5/2021",
            "debit_amount": 80,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "PAYALEBAR MRT1",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "8/6/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "NTUC LK TIGA",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "8/7/2021",
            "debit_amount": 80,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "SIMEI MRT 3",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "29/8/2021",
            "debit_amount": 80,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "NTUC LK TIGA",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "KEMBANGAN MRT",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "26/9/2021",
            "debit_amount": 100,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "KEMBANGAN MRT",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 75.12,
            "credit_amount": 0,
            "description_1": "PAYPAL *MYPROTEIN 35 31 26APR",
            "description_2": "1123-2234-5544-7755",
            "category": "Health"
        },
        {
            "transaction_date": "29/4/2021",
            "debit_amount": 81,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "CHA HENG CHOY ACUPUNCTURE",
            "category": "Health"
        },
        {
            "transaction_date": "4/5/2021",
            "debit_amount": 72.76,
            "credit_amount": 0,
            "description_1": "EZYPAYSGD*ANYTIME FITN SI NG 01MAY",
            "description_2": "1123-2234-5544-7755",
            "category": "Health"
        },
        {
            "transaction_date": "7/5/2021",
            "debit_amount": 35.43,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "HEALTHWAY MEDICAL GROUP P",
            "category": "Health"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": 19.5,
            "credit_amount": 0,
            "description_1": "29102754",
            "description_2": "GUARDIAN HEALTH & BEAUTY",
            "category": "Health"
        },
        {
            "transaction_date": "2/7/2021",
            "debit_amount": 72.76,
            "credit_amount": 0,
            "description_1": "EZYPAYSGD*ANYTIME FITN SI NG 01JUL",
            "description_2": "1123-2234-5544-7755",
            "category": "Health"
        },
        {
            "transaction_date": "4/8/2021",
            "debit_amount": 164.25,
            "credit_amount": 0,
            "description_1": "Q&M DENTAL SURG-MP SI NG 01AUG",
            "description_2": "1123-2234-5544-7755",
            "category": "Health"
        },
        {
            "transaction_date": "2/9/2021",
            "debit_amount": 72.76,
            "credit_amount": 0,
            "description_1": "EZYPAYSGD*ANYTIME FITN SI NG 01SEP",
            "description_2": "1123-2234-5544-7755",
            "category": "Health"
        },
        {
            "transaction_date": "2/10/2021",
            "debit_amount": 72.76,
            "credit_amount": 0,
            "description_1": "EZYPAYSGD*ANYTIME FITN SI NG 01OCT",
            "description_2": "1123-2234-5544-7755",
            "category": "Health"
        },
        {
            "transaction_date": "19/10/2021",
            "debit_amount": 19.5,
            "credit_amount": 0,
            "description_1": "GUARDIAN-KEMBANGAN MRT SI NG 16OCT",
            "description_2": "1123-2234-5544-7755",
            "category": "Health"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": 0,
            "credit_amount": 0.16,
            "description_1": "",
            "description_2": "",
            "category": "Interest"
        },
        {
            "transaction_date": "31/5/2021",
            "debit_amount": 0,
            "credit_amount": 0.11,
            "description_1": "",
            "description_2": "",
            "category": "Interest"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": 0,
            "credit_amount": 0.06,
            "description_1": "",
            "description_2": "",
            "category": "Interest"
        },
        {
            "transaction_date": "31/7/2021",
            "debit_amount": 0,
            "credit_amount": 0.06,
            "description_1": "",
            "description_2": "",
            "category": "Interest"
        },
        {
            "transaction_date": "31/8/2021",
            "debit_amount": 0,
            "credit_amount": 0.08,
            "description_1": "",
            "description_2": "",
            "category": "Interest"
        },
        {
            "transaction_date": "30/9/2021",
            "debit_amount": 0,
            "credit_amount": 0.07,
            "description_1": "",
            "description_2": "",
            "category": "Interest"
        },
        {
            "transaction_date": "14/5/2021",
            "debit_amount": 1600,
            "credit_amount": 0,
            "description_1": "CIMB:10000100000057962:I-BANK",
            "description_2": "xfers deposit",
            "category": "Investment"
        },
        {
            "transaction_date": "20/5/2021",
            "debit_amount": 500,
            "credit_amount": 0,
            "description_1": "CIMB:10000100000057962:I-BANK",
            "description_2": "xfers deposit",
            "category": "Investment"
        },
        {
            "transaction_date": "21/7/2021",
            "debit_amount": 200,
            "credit_amount": 0,
            "description_1": "CIMB:10000100000057962:I-BANK",
            "description_2": "Xfers Pte Ltd",
            "category": "Investment"
        },
        {
            "transaction_date": "17/9/2021",
            "debit_amount": 0,
            "credit_amount": 988.34,
            "description_1": "WC1763699WC",
            "description_2": "20210917CIBBSGSGBRT1861865",
            "category": "Investment"
        },
        {
            "transaction_date": "26/9/2021",
            "debit_amount": 0,
            "credit_amount": 1252,
            "description_1": "WC1806032WC",
            "description_2": "20210926CIBBSGSGBRT1938839",
            "category": "Investment"
        },
        {
            "transaction_date": "2/10/2021",
            "debit_amount": 0,
            "credit_amount": 1917,
            "description_1": "WC1825304WC",
            "description_2": "20211002CIBBSGSGBRT1997800",
            "category": "Investment"
        },
        {
            "transaction_date": "6/10/2021",
            "debit_amount": 0,
            "credit_amount": 2399,
            "description_1": "WC1840872WC",
            "description_2": "20211006CIBBSGSGBRT2041221",
            "category": "Investment"
        },
        {
            "transaction_date": "7/10/2021",
            "debit_amount": 0,
            "credit_amount": 2430,
            "description_1": "WC1847652WC",
            "description_2": "20211007CIBBSGSGBRT2055757",
            "category": "Investment"
        },
        {
            "transaction_date": "4/5/2021",
            "debit_amount": 200,
            "credit_amount": 0,
            "description_1": "Manulife-Operations",
            "description_2": "INS 29042021",
            "category": "Insurance"
        },
        {
            "transaction_date": "4/6/2021",
            "debit_amount": 200,
            "credit_amount": 0,
            "description_1": "Manulife-Operations",
            "description_2": "INS 29052021",
            "category": "Insurance"
        },
        {
            "transaction_date": "5/7/2021",
            "debit_amount": 200,
            "credit_amount": 0,
            "description_1": "Manulife-Operations",
            "description_2": "INS 29062021",
            "category": "Insurance"
        },
        {
            "transaction_date": "4/8/2021",
            "debit_amount": 200,
            "credit_amount": 0,
            "description_1": "Manulife-Operations",
            "description_2": "INS 29072021",
            "category": "Insurance"
        },
        {
            "transaction_date": "6/9/2021",
            "debit_amount": 200,
            "credit_amount": 0,
            "description_1": "Manulife-Operations",
            "description_2": "INS 29082021",
            "category": "Insurance"
        },
        {
            "transaction_date": "4/10/2021",
            "debit_amount": 200,
            "credit_amount": 0,
            "description_1": "Manulife-Operations",
            "description_2": "INS 29092021",
            "category": "Insurance"
        }
    ]
}, {
    "account_id": 1003,
    "date_registered": "30/10/2021",
    "name": "Kwang Guan Cong",
    "bank_name": "DBS",
    "password": "password123",
    "balance": 3000,
    "email": "kgc@gmail.com",
    "transactions": [{
            "transaction_date": "28/5/2021",
            "debit_amount": 0,
            "credit_amount": 4.81,
            "description_1": "DBS VISA DEBIT CASHBACK F OR 24MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Cashback"
        },
        {
            "transaction_date": "25/6/2021",
            "debit_amount": 0,
            "credit_amount": 1.62,
            "description_1": "DBS VISA DEBIT CASHBACK F OR 21JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Cashback"
        },
        {
            "transaction_date": "13/7/2021",
            "debit_amount": 0,
            "credit_amount": 8,
            "description_1": "DBS 7.7 Extra Bonus Day 10JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Cashback"
        },
        {
            "transaction_date": "27/7/2021",
            "debit_amount": 0,
            "credit_amount": 5.31,
            "description_1": "DBS VISA DEBIT CASHBACK F OR 21JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Cashback"
        },
        {
            "transaction_date": "24/8/2021",
            "debit_amount": 0,
            "credit_amount": 5.81,
            "description_1": "DBS VISA DEBIT CASHBACK F OR 18AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Cashback"
        },
        {
            "transaction_date": "23/9/2021",
            "debit_amount": 0,
            "credit_amount": 1.3,
            "description_1": "DBS VISA DEBIT CASHBACK F OR 21SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Cashback"
        },
        {
            "transaction_date": "7/5/2021",
            "debit_amount": 0,
            "credit_amount": 580,
            "description_1": "CASH NETS",
            "description_2": "TAMPINES ONE B",
            "category": "Deposits"
        },
        {
            "transaction_date": "15/5/2021",
            "debit_amount": 0,
            "credit_amount": 450,
            "description_1": "CASH NETS",
            "description_2": "TAMP C BR 1",
            "category": "Deposits"
        },
        {
            "transaction_date": "28/5/2021",
            "debit_amount": 0,
            "credit_amount": 200,
            "description_1": "CASH NETS",
            "description_2": "TAMP C BR 1",
            "category": "Deposits"
        },
        {
            "transaction_date": "13/6/2021",
            "debit_amount": 0,
            "credit_amount": 380,
            "description_1": "CASH NETS",
            "description_2": "TAMPINES ONE B",
            "category": "Deposits"
        },
        {
            "transaction_date": "3/7/2021",
            "debit_amount": 0,
            "credit_amount": 170,
            "description_1": "CASH NETS",
            "description_2": "TAMPINES MRT 3",
            "category": "Deposits"
        },
        {
            "transaction_date": "14/8/2021",
            "debit_amount": 0,
            "credit_amount": 420,
            "description_1": "CASH NETS",
            "description_2": "TAMP C BR 1",
            "category": "Deposits"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": 0,
            "credit_amount": 44.33,
            "description_1": "1201111119 : I-BANK",
            "description_2": "",
            "category": "Deposits"
        },
        {
            "transaction_date": "1/9/2021",
            "debit_amount": 0,
            "credit_amount": 344.08,
            "description_1": "1201111119 : I-BANK",
            "description_2": "",
            "category": "Deposits"
        },
        {
            "transaction_date": "6/9/2021",
            "debit_amount": 0,
            "credit_amount": 530,
            "description_1": "CASH NETS",
            "description_2": "TAMP C BR 1",
            "category": "Deposits"
        },
        {
            "transaction_date": "3/10/2021",
            "debit_amount": 0,
            "credit_amount": 790,
            "description_1": "CASH NETS",
            "description_2": "TAMPINES ONE B",
            "category": "Deposits"
        },
        {
            "transaction_date": "16/5/2021",
            "debit_amount": 4.32,
            "credit_amount": 0,
            "description_1": "PAYPAL *STEAM GAMES  35 31 14MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Entertainment"
        },
        {
            "transaction_date": "19/5/2021",
            "debit_amount": 15.22,
            "credit_amount": 0,
            "description_1": "WARGAMING_ASIA  NI CO 17MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Entertainment"
        },
        {
            "transaction_date": "9/6/2021",
            "debit_amount": 28.5,
            "credit_amount": 0,
            "description_1": "WWW.GV.COM.SG  SI NG 05JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Entertainment"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": 5.61,
            "credit_amount": 0,
            "description_1": "WARGAMINGASIA  NI CO 25AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Entertainment"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": 15.22,
            "credit_amount": 0,
            "description_1": "WARGAMINGASIA  NI CO 25AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Entertainment"
        },
        {
            "transaction_date": "29/4/2021",
            "debit_amount": 5,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (PRC2)  SI NG 26APR",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": 10.5,
            "credit_amount": 0,
            "description_1": "IKEA-RESTAURANT  SI NG 28APR",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "1/5/2021",
            "debit_amount": 10.15,
            "credit_amount": 0,
            "description_1": "KFC TPH 514  SI NG 29APR",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "4/5/2021",
            "debit_amount": 11.4,
            "credit_amount": 0,
            "description_1": "ASTON SPECIALITIES  SI NG 01MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "9/5/2021",
            "debit_amount": 20.95,
            "credit_amount": 0,
            "description_1": "TAMAGO EN @ TPM  SI NG 07MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "18/5/2021",
            "debit_amount": 10.5,
            "credit_amount": 0,
            "description_1": "IKEA-RESTAURANT  SI NG 16MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "26/5/2021",
            "debit_amount": 6.5,
            "credit_amount": 0,
            "description_1": "BOOST JUICE TAMPINES  SI NG 24MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "26/5/2021",
            "debit_amount": 4.4,
            "credit_amount": 0,
            "description_1": "CHATERAISE  SI NG 24MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "12/6/2021",
            "debit_amount": 5.7,
            "credit_amount": 0,
            "description_1": "CHICHA SAN CHEN-TAMPIN SI NG 10JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "15/6/2021",
            "debit_amount": 12.6,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: MentaiYa in ya area",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 1.5,
            "credit_amount": 0,
            "description_1": "CHATERAISE  SI NG 13JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "18/6/2021",
            "debit_amount": 7.8,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: MentaiYa in ya area",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "23/6/2021",
            "debit_amount": 8.1,
            "credit_amount": 0,
            "description_1": "FR VIVO-TASTE  SI NG 20JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "23/6/2021",
            "debit_amount": 3.8,
            "credit_amount": 0,
            "description_1": "LIHO TAMP HUB  SI NG 21JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/6/2021",
            "debit_amount": 10.8,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TGV)  SI NG 21JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "25/6/2021",
            "debit_amount": 23.4,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: MentaiYa in ya area",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 2.2,
            "credit_amount": 0,
            "description_1": "CHATERAISE  SI NG 26JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 37.3,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (WCP)  SI NG 26JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 7.5,
            "credit_amount": 0,
            "description_1": "STUFF'D JEM  SI NG 26JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "2/7/2021",
            "debit_amount": 17.2,
            "credit_amount": 0,
            "description_1": "KATONG MEI WEI CHICKEN SI NG 30JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "6/7/2021",
            "debit_amount": 1.5,
            "credit_amount": 0,
            "description_1": "CHATERAISE  SI NG 03JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "8/7/2021",
            "debit_amount": 6.4,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TGV)  SI NG 05JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "13/7/2021",
            "debit_amount": 8.3,
            "credit_amount": 0,
            "description_1": "WOK HEY - BUGIS JUNCTI SI NG 11JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "13/7/2021",
            "debit_amount": 8.8,
            "credit_amount": 0,
            "description_1": "WOK HEY - BUGIS JUNCTI SI NG 11JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "14/7/2021",
            "debit_amount": 9.3,
            "credit_amount": 0,
            "description_1": "GENKI SUSHI-BUGIS +  SI NG 11JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "17/7/2021",
            "debit_amount": 6.4,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TGV)  SI NG 14JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "20/7/2021",
            "debit_amount": 29.64,
            "credit_amount": 0,
            "description_1": "BJR-MENYA MUSASHI@VV  SI NG 17JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "20/7/2021",
            "debit_amount": 9.8,
            "credit_amount": 0,
            "description_1": "WOK HEY PTE LTD  SI NG 18JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 26.95,
            "credit_amount": 0,
            "description_1": "THE SUSHI BAR - TAMPIN SI NG 20JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 9.8,
            "credit_amount": 0,
            "description_1": "WOK HEY PTE LTD  SI NG 19JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "28/7/2021",
            "debit_amount": 5,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TN3)  SI NG 25JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "31/7/2021",
            "debit_amount": 6.35,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (SHTM)  SI NG 29JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "3/8/2021",
            "debit_amount": 10.8,
            "credit_amount": 0,
            "description_1": "WOK HEY PTE LTD  SI NG 01AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/8/2021",
            "debit_amount": 7.8,
            "credit_amount": 0,
            "description_1": "WOK HEY PTE LTD  SI NG 06AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/8/2021",
            "debit_amount": 13.4,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TAM)  SI NG 19AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/8/2021",
            "debit_amount": 1,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TAM)  SI NG 20AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/8/2021",
            "debit_amount": 140.06,
            "credit_amount": 0,
            "description_1": "STICKIES BAR - ALJUNIE SI NG 20AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "31/8/2021",
            "debit_amount": 10.8,
            "credit_amount": 0,
            "description_1": "WOK HEY PTE LTD  SI NG 28AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "2/9/2021",
            "debit_amount": 20.4,
            "credit_amount": 0,
            "description_1": "IKEA-RESTAURANT  SI NG 31AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": 16.95,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TGV)  SI NG 31AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": 12.3,
            "credit_amount": 0,
            "description_1": "WOK HEY PTE LTD  SI NG 01SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/9/2021",
            "debit_amount": 18.45,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TGV)  SI NG 04SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "8/9/2021",
            "debit_amount": 11.45,
            "credit_amount": 0,
            "description_1": "KFC TPH 514  SI NG 06SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 5.8,
            "credit_amount": 0,
            "description_1": "LIHO TAMP HUB  SI NG 09SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 10.8,
            "credit_amount": 0,
            "description_1": "WOK HEY PTE LTD  SI NG 09SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "16/9/2021",
            "debit_amount": 11.2,
            "credit_amount": 0,
            "description_1": "BLANCO CT BEEF NOODLES SI NG 14SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "18/9/2021",
            "debit_amount": 18.95,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TGV)  SI NG 15SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "23/9/2021",
            "debit_amount": 9.8,
            "credit_amount": 0,
            "description_1": "WOK HEY PTE LTD  SI NG 21SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "25/9/2021",
            "debit_amount": 11,
            "credit_amount": 0,
            "description_1": "WINGSTOP - OUR TAMP HU SI NG 23SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "5/10/2021",
            "debit_amount": 2.9,
            "credit_amount": 0,
            "description_1": "WADORI TAMPINES 1  SI NG 03OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "6/10/2021",
            "debit_amount": 13.89,
            "credit_amount": 0,
            "description_1": "GENKI SUSHI-TAMPINES M SI NG 03OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "12/10/2021",
            "debit_amount": 5,
            "credit_amount": 0,
            "description_1": "MCDONALD'S (TAM)  SI NG 09OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "12/10/2021",
            "debit_amount": 44.6,
            "credit_amount": 0,
            "description_1": "THE SUSHI BAR - TAMPIN SI NG 09OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/6/2021",
            "debit_amount": 0,
            "credit_amount": 200,
            "description_1": "GST VOUCHER",
            "description_2": "GOVT PAYOUT",
            "category": "Government"
        },
        {
            "transaction_date": "27/7/2021",
            "debit_amount": 0,
            "credit_amount": 300,
            "description_1": "GST VOUCHER",
            "description_2": "GOVT PAYOUT",
            "category": "Government"
        },
        {
            "transaction_date": "13/10/2021",
            "debit_amount": 210,
            "credit_amount": 0,
            "description_1": "MYICA  SI NG 10OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Government"
        },
        {
            "transaction_date": "8/5/2021",
            "debit_amount": 9.7,
            "credit_amount": 0,
            "description_1": "SHENGSIONG@602ATAMPINE SI NG 06MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Groceries"
        },
        {
            "transaction_date": "20/6/2021",
            "debit_amount": 3.8,
            "credit_amount": 0,
            "description_1": "SHENGSIONG@602ATAMPINE SI NG 18JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Groceries"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 2.5,
            "credit_amount": 0,
            "description_1": "FAIRPRICE XTRA - JEM  SI NG 26JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Groceries"
        },
        {
            "transaction_date": "8/7/2021",
            "debit_amount": 0.55,
            "credit_amount": 0,
            "description_1": "PRIME FOOD & GROCER  SI NG 06JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Groceries"
        },
        {
            "transaction_date": "31/7/2021",
            "debit_amount": 4.85,
            "credit_amount": 0,
            "description_1": "SHENGSIONG@602ATAMPINE SI NG 29JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Groceries"
        },
        {
            "transaction_date": "4/8/2021",
            "debit_amount": 3.5,
            "credit_amount": 0,
            "description_1": "SHENGSIONG@602ATAMPINE SI NG 31JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Groceries"
        },
        {
            "transaction_date": "5/8/2021",
            "debit_amount": 11.45,
            "credit_amount": 0,
            "description_1": "SHENGSIONG@602ATAMPINE SI NG 03AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Groceries"
        },
        {
            "transaction_date": "26/4/2021",
            "debit_amount": 0,
            "credit_amount": 19.9,
            "description_1": "Incoming PayNow Ref 7468632",
            "description_2": "From: Holdor",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "26/4/2021",
            "debit_amount": 0,
            "credit_amount": 1.6,
            "description_1": "Incoming PayNow Ref 7468817",
            "description_2": "From: Holdor",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "26/4/2021",
            "debit_amount": 0,
            "credit_amount": 2.37,
            "description_1": "Incoming PayNow Ref 7469645",
            "description_2": "From: Holdor",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "26/4/2021",
            "debit_amount": 0,
            "credit_amount": 1.6,
            "description_1": "Incoming PayNow Ref 7490834",
            "description_2": "From: Holdor",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 0,
            "credit_amount": 1,
            "description_1": "Incoming PayNow Ref 5032062",
            "description_2": "From: Jim Kirk",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 0,
            "credit_amount": 1,
            "description_1": "Incoming PayNow Ref 5032336",
            "description_2": "From: Holdor",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 0,
            "credit_amount": 1,
            "description_1": "Incoming PayNow Ref 5255894",
            "description_2": "From: Holdor",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 0,
            "credit_amount": 1,
            "description_1": "Incoming PayNow Ref 9081503",
            "description_2": "From: Bran Stark",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 0,
            "credit_amount": 1,
            "description_1": "Incoming PayNow Ref 9082298",
            "description_2": "From: Aria Stark",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/4/2021",
            "debit_amount": 30,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Han Solo",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "4/5/2021",
            "debit_amount": 0,
            "credit_amount": 50,
            "description_1": "SEND BACK FROM PAYLAH! :",
            "description_2": "43258932",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "9/5/2021",
            "debit_amount": 15,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Luke Skywalker",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "9/5/2021",
            "debit_amount": 6.5,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Han Solo",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "10/5/2021",
            "debit_amount": 0,
            "credit_amount": 250,
            "description_1": "Incoming PayNow Ref 9111231",
            "description_2": "From: Daenerys Targaryen",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "11/5/2021",
            "debit_amount": 0,
            "credit_amount": 10,
            "description_1": "Incoming PayNow Ref 9712596",
            "description_2": "From: Jane Smith",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": 0,
            "credit_amount": 25,
            "description_1": "Incoming PayNow Ref 6683255",
            "description_2": "From: Jane Smith",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "4/6/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: WISE ASIA-PACIFIC  PTE. LTD.",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "8/6/2021",
            "debit_amount": 0,
            "credit_amount": 14.25,
            "description_1": "Incoming PayNow Ref 1779936",
            "description_2": "From: Bran Stark",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "10/6/2021",
            "debit_amount": 0,
            "credit_amount": 150,
            "description_1": "Incoming PayNow Ref 9070366",
            "description_2": "From: Daenerys Targaryen",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "13/6/2021",
            "debit_amount": 0,
            "credit_amount": 10,
            "description_1": "Incoming PayNow Ref 7905786",
            "description_2": "From: John Doe",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 0,
            "credit_amount": 75,
            "description_1": "Incoming PayNow Ref 8431431",
            "description_2": "From: John Doe",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 28,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Han Solo",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": 0,
            "credit_amount": 7.8,
            "description_1": "Incoming PayNow Ref 6155726",
            "description_2": "From: John Doe",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": 0,
            "credit_amount": 11.75,
            "description_1": "Incoming PayNow Ref 6313575",
            "description_2": "From: Holdor",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 0,
            "credit_amount": 16,
            "description_1": "Incoming PayNow Ref 7521892",
            "description_2": "From: Aria Stark",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 0,
            "credit_amount": 12.8,
            "description_1": "Incoming PayNow Ref 8283875",
            "description_2": "From: Jim Kirk",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "1/7/2021",
            "debit_amount": 0,
            "credit_amount": 12.8,
            "description_1": "Incoming PayNow Ref 6403948",
            "description_2": "From: Holdor",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "1/7/2021",
            "debit_amount": 54.75,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Luke Skywalker",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "1/7/2021",
            "debit_amount": 0,
            "credit_amount": 9,
            "description_1": "SEND BACK FROM PAYLAH! :",
            "description_2": "43258932",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "2/7/2021",
            "debit_amount": 0,
            "credit_amount": 24.3,
            "description_1": "Incoming PayNow Ref 6953787",
            "description_2": "From: Mary Lane",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "10/7/2021",
            "debit_amount": 0,
            "credit_amount": 13,
            "description_1": "Incoming PayNow Ref 5894417",
            "description_2": "From: John Doe",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "11/7/2021",
            "debit_amount": 0,
            "credit_amount": 8.3,
            "description_1": "Incoming PayNow Ref 1816988",
            "description_2": "From: Bran Stark",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "12/7/2021",
            "debit_amount": 0,
            "credit_amount": 12.15,
            "description_1": "Incoming PayNow Ref 2002520",
            "description_2": "From: Bran Stark",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "18/7/2021",
            "debit_amount": 0,
            "credit_amount": 15,
            "description_1": "Incoming PayNow Ref 5217991",
            "description_2": "From: Jim Kirk",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "19/7/2021",
            "debit_amount": 0,
            "credit_amount": 26,
            "description_1": "Incoming PayNow Ref 3930428",
            "description_2": "From: Bran Stark",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "26/7/2021",
            "debit_amount": 30,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: WISE ASIA-PACIFIC  PTE. LTD.",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": 0,
            "credit_amount": 31.54,
            "description_1": "Incoming PayNow Ref 5850707",
            "description_2": "From: Alicia",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": 0,
            "credit_amount": 31.54,
            "description_1": "Incoming PayNow Ref 5852787",
            "description_2": "From: Darth Vader",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": 0,
            "credit_amount": 20,
            "description_1": "Incoming PayNow Ref 5854040",
            "description_2": "From: Darth Vader",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "20/8/2021",
            "debit_amount": 0,
            "credit_amount": 31.5,
            "description_1": "Incoming PayNow Ref 5857409",
            "description_2": "From: Holdor",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "25/9/2021",
            "debit_amount": 110,
            "credit_amount": 0,
            "description_1": "UOB:4683722795:I-BANK",
            "description_2": "nil",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/9/2021",
            "debit_amount": 6.2,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Luke Skywalker",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "22/10/2021",
            "debit_amount": 0,
            "credit_amount": 20,
            "description_1": "Incoming PayNow Ref 7381703",
            "description_2": "From: Mary Lane",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/4/2021",
            "debit_amount": 4.68,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE GPAY  SI NG 26APR",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": 11.29,
            "credit_amount": 0,
            "description_1": "APPLE.COM/BILL  IT UN 28APR",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": 850,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE MP  SI NG 08MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "26/6/2021",
            "debit_amount": 175.11,
            "credit_amount": 0,
            "description_1": "SP * GLORIOUS PC GAMIN WW W. 24JUN",
            "description_2": "1234-4567-7890-3245 USD125.85",
            "category": "Shopping"
        },
        {
            "transaction_date": "7/7/2021",
            "debit_amount": 24.55,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE MP  SI NG 03JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "10/7/2021",
            "debit_amount": 103.51,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE MP  SI NG 07JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "11/7/2021",
            "debit_amount": 2.24,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE GPAY  SI NG 08JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "11/7/2021",
            "debit_amount": 13.47,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE MP  SI NG 08JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "28/7/2021",
            "debit_amount": 100,
            "credit_amount": 0,
            "description_1": "7-ELEVEN -BEDOK RESERV SI NG 25JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "28/7/2021",
            "debit_amount": 100,
            "credit_amount": 0,
            "description_1": "7-ELEVEN -BEDOK RESERV SI NG 25JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "17/8/2021",
            "debit_amount": 7.99,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE GPAY  SI NG 13AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "18/8/2021",
            "debit_amount": 4.38,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE GPAY  SI NG 14AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "18/8/2021",
            "debit_amount": 45,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE MP  SI NG 14AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "31/8/2021",
            "debit_amount": 338,
            "credit_amount": 0,
            "description_1": "LAZADA  SI NG 28AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "31/8/2021",
            "debit_amount": 12.51,
            "credit_amount": 0,
            "description_1": "LAZADA SINGAPORE  SI NG 28AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "4/9/2021",
            "debit_amount": 11.29,
            "credit_amount": 0,
            "description_1": "APPLE.COM/BILL  IT UN 02SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Shopping"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 3.36,
            "credit_amount": 0,
            "description_1": "BUS/MRT 76941660  SI NG 22APR",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "1/5/2021",
            "debit_amount": 2.72,
            "credit_amount": 0,
            "description_1": "BUS/MRT 77517479  SI NG 26APR",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "4/5/2021",
            "debit_amount": 8.3,
            "credit_amount": 0,
            "description_1": "GRAB* ADR-XUNFP7CWWJDX SI NG 02MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "5/5/2021",
            "debit_amount": 1.84,
            "credit_amount": 0,
            "description_1": "BUS/MRT 77913408  SI NG 28APR",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "6/5/2021",
            "debit_amount": 27,
            "credit_amount": 0,
            "description_1": "SHELL TAMPINES AVE 2  SI NG 04MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "6/5/2021",
            "debit_amount": 3.44,
            "credit_amount": 0,
            "description_1": "BUS/MRT 78474239  SI NG 01MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "7/5/2021",
            "debit_amount": 2.6,
            "credit_amount": 0,
            "description_1": "BUS/MRT 78643218  SI NG 02MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": 1.84,
            "credit_amount": 0,
            "description_1": "BUS/MRT 79521222  SI NG 07MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "13/5/2021",
            "debit_amount": 1.76,
            "credit_amount": 0,
            "description_1": "BUS/MRT 79655287  SI NG 08MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "18/5/2021",
            "debit_amount": 2.14,
            "credit_amount": 0,
            "description_1": "BUS/MRT 80283011  SI NG 12MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "20/5/2021",
            "debit_amount": 3.04,
            "credit_amount": 0,
            "description_1": "BUS/MRT 80760067  SI NG 15MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "21/5/2021",
            "debit_amount": 0.92,
            "credit_amount": 0,
            "description_1": "BUS/MRT 80895447  SI NG 16MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 1.02,
            "credit_amount": 0,
            "description_1": "BUS/MRT 83543169  SI NG 10JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 0.92,
            "credit_amount": 0,
            "description_1": "BUS/MRT 83552463  SI NG 10JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 1.02,
            "credit_amount": 0,
            "description_1": "BUS/MRT 83909702  SI NG 13JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "22/6/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "GRAB  AE89D3217B838D36 SI NG 20JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "24/6/2021",
            "debit_amount": 3.48,
            "credit_amount": 0,
            "description_1": "BUS/MRT 84611426  SI NG 19JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "26/6/2021",
            "debit_amount": 3.8,
            "credit_amount": 0,
            "description_1": "BUS/MRT 84730970  SI NG 20JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": 18,
            "credit_amount": 0,
            "description_1": "SHELL TAMPINES AVE 2  SI NG 26JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "2/7/2021",
            "debit_amount": 18,
            "credit_amount": 0,
            "description_1": "SHELL TAMPINES AVE 2  SI NG 30JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "8/7/2021",
            "debit_amount": 0.92,
            "credit_amount": 0,
            "description_1": "BUS/MRT 86600913  SI NG 03JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "13/7/2021",
            "debit_amount": 24.3,
            "credit_amount": 0,
            "description_1": "GRAB  A-27PJUN3GWGGV  SI NG 11JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "14/7/2021",
            "debit_amount": 2.76,
            "credit_amount": 0,
            "description_1": "BUS/MRT 87348691  SI NG 08JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "14/7/2021",
            "debit_amount": 1.84,
            "credit_amount": 0,
            "description_1": "BUS/MRT 87515462  SI NG 09JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 3.54,
            "credit_amount": 0,
            "description_1": "BUS/MRT 87674644  SI NG 10JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "16/7/2021",
            "debit_amount": 1.72,
            "credit_amount": 0,
            "description_1": "BUS/MRT 87866932  SI NG 11JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "17/7/2021",
            "debit_amount": 1.84,
            "credit_amount": 0,
            "description_1": "BUS/MRT 87968104  SI NG 12JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 3.12,
            "credit_amount": 0,
            "description_1": "BUS/MRT 88445696  SI NG 15JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "23/7/2021",
            "debit_amount": 3.8,
            "credit_amount": 0,
            "description_1": "BUS/MRT 88791202  SI NG 17JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "19/8/2021",
            "debit_amount": 0.92,
            "credit_amount": 0,
            "description_1": "BUS/MRT 92927553  SI NG 14AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "25/8/2021",
            "debit_amount": 3.16,
            "credit_amount": 0,
            "description_1": "BUS/MRT 93857691  SI NG 20AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "8/9/2021",
            "debit_amount": 10.44,
            "credit_amount": 0,
            "description_1": "BLUESG  SI NG 06SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "8/9/2021",
            "debit_amount": 3.75,
            "credit_amount": 0,
            "description_1": "BUS/MRT 96285208  SI NG 03SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 4.32,
            "credit_amount": 0,
            "description_1": "BUS/MRT 96801817  SI NG 06SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "12/9/2021",
            "debit_amount": 3.36,
            "credit_amount": 0,
            "description_1": "BUS/MRT 97065432  SI NG 07SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 8,
            "credit_amount": 0,
            "description_1": "BLUESG  SI NG 13SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "19/9/2021",
            "debit_amount": 3.4,
            "credit_amount": 0,
            "description_1": "BUS/MRT 98181472  SI NG 14SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "21/9/2021",
            "debit_amount": 1.68,
            "credit_amount": 0,
            "description_1": "BUS/MRT 98352599  SI NG 15SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "22/9/2021",
            "debit_amount": 9.36,
            "credit_amount": 0,
            "description_1": "BLUESG  SI NG 20SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "22/9/2021",
            "debit_amount": 3.36,
            "credit_amount": 0,
            "description_1": "BUS/MRT 98548136  SI NG 16SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "25/9/2021",
            "debit_amount": 3.36,
            "credit_amount": 0,
            "description_1": "BUS/MRT 99184219  SI NG 20SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "26/9/2021",
            "debit_amount": 3.4,
            "credit_amount": 0,
            "description_1": "BUS/MRT 99410794  SI NG 21SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "29/9/2021",
            "debit_amount": 3.4,
            "credit_amount": 0,
            "description_1": "BUS/MRT 99669011  SI NG 23SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "8/10/2021",
            "debit_amount": 0.92,
            "credit_amount": 0,
            "description_1": "BUS/MRT 101244291  SI NG 03OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "14/10/2021",
            "debit_amount": 0.92,
            "credit_amount": 0,
            "description_1": "BUS/MRT 102164072  SI NG 09OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "17/10/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "GRAB  B6BD72F8FB6C68FC SI NG 15OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "20/10/2021",
            "debit_amount": 1.48,
            "credit_amount": 0,
            "description_1": "BUS/MRT 102998351  SI NG 15OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Transport"
        },
        {
            "transaction_date": "19/5/2021",
            "debit_amount": 62.62,
            "credit_amount": 0,
            "description_1": "SP DIGITAL PTE LTD  SI NG 16MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "25/5/2021",
            "debit_amount": 17,
            "credit_amount": 0,
            "description_1": "MYREPUBLIC LIMITED  SI NG 22MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 210.25,
            "credit_amount": 0,
            "description_1": "SP DIGITAL PTE LTD  SI NG 13JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": 17,
            "credit_amount": 0,
            "description_1": "MYREPUBLIC LIMITED  SI NG 28JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "25/7/2021",
            "debit_amount": 22.55,
            "credit_amount": 0,
            "description_1": "SP DIGITAL PTE LTD  SI NG 22JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "29/7/2021",
            "debit_amount": 17,
            "credit_amount": 0,
            "description_1": "MYREPUBLIC LIMITED  SI NG 27JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "18/8/2021",
            "debit_amount": 195.14,
            "credit_amount": 0,
            "description_1": "SP DIGITAL PL-UTILITIE SI NG 14AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "29/8/2021",
            "debit_amount": 17.3,
            "credit_amount": 0,
            "description_1": "MYREPUBLIC LIMITED  SI NG 27AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "29/9/2021",
            "debit_amount": 17,
            "credit_amount": 0,
            "description_1": "MYREPUBLIC LIMITED  SI NG 27SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "1/10/2021",
            "debit_amount": 210.38,
            "credit_amount": 0,
            "description_1": "SP DIGITAL PL-UTILITIE SI NG 28SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Utilities"
        },
        {
            "transaction_date": "27/4/2021",
            "debit_amount": 19.3,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "2/5/2021",
            "debit_amount": 8.6,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "5/5/2021",
            "debit_amount": 8.2,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "11/5/2021",
            "debit_amount": 5,
            "credit_amount": 0,
            "description_1": "CASH NETS",
            "description_2": "P PARKING",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "16/5/2021",
            "debit_amount": 1.15,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "11/6/2021",
            "debit_amount": 9,
            "credit_amount": 0,
            "description_1": "CASH NETS",
            "description_2": "P PARKING",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "12/6/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 75,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "21/6/2021",
            "debit_amount": 18.75,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "26/6/2021",
            "debit_amount": 20,
            "credit_amount": 0,
            "description_1": "CASH NETS",
            "description_2": "P PARKING",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "26/6/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "CASH NETS",
            "description_2": "P PARKING",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": 5,
            "credit_amount": 0,
            "description_1": "CASH NETS",
            "description_2": "P PARKING",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "12/7/2021",
            "debit_amount": 27.3,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "12/7/2021",
            "debit_amount": 13.5,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "12/7/2021",
            "debit_amount": 7.5,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 0.5,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 75,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "20/7/2021",
            "debit_amount": 3.6,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "GuanCong",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 65,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": 685,
            "credit_amount": 0,
            "description_1": "1201111119 : I-BANK",
            "description_2": "USD @  1.3609420",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "9/10/2021",
            "debit_amount": 44.91,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "43258932",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "17/10/2021",
            "debit_amount": 63.15,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "GuanCong",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "22/10/2021",
            "debit_amount": 30.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "GuanCong",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 14.2,
            "credit_amount": 0,
            "description_1": "WATSON'S  SI NG 13JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Health"
        },
        {
            "transaction_date": "6/7/2021",
            "debit_amount": 22.3,
            "credit_amount": 0,
            "description_1": "WATSON'S  SI NG 03JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Health"
        },
        {
            "transaction_date": "11/7/2021",
            "debit_amount": 50.29,
            "credit_amount": 0,
            "description_1": "UNIVERSAL DENTAL CENTR SI NG 09JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Health"
        },
        {
            "transaction_date": "27/4/2021",
            "debit_amount": 0,
            "credit_amount": 0.37,
            "description_1": "Incoming PayNow Ref 8878105",
            "description_2": "From: GOOGLE PAYMENT SINGAPORE PTE.",
            "category": "Interest"
        },
        {
            "transaction_date": "16/5/2021",
            "debit_amount": 0,
            "credit_amount": 0.12,
            "description_1": "Incoming PayNow Ref 5006562",
            "description_2": "From: GOOGLE PAYMENT SINGAPORE PTE.",
            "category": "Interest"
        },
        {
            "transaction_date": "12/6/2021",
            "debit_amount": 0,
            "credit_amount": 0.11,
            "description_1": "Incoming PayNow Ref 2821222",
            "description_2": "From: GOOGLE PAYMENT SINGAPORE PTE.",
            "category": "Interest"
        },
        {
            "transaction_date": "12/7/2021",
            "debit_amount": 0,
            "credit_amount": 0.4,
            "description_1": "Incoming PayNow Ref 2007244",
            "description_2": "From: GOOGLE PAYMENT SINGAPORE PTE.",
            "category": "Interest"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": 0,
            "credit_amount": 1000,
            "description_1": "SG21082800600252450000",
            "description_2": "20210828SCBLSG22BRT0024969",
            "category": "Income"
        },
        {
            "transaction_date": "5/10/2021",
            "debit_amount": 0,
            "credit_amount": 5955,
            "description_1": "SG21100500600225890000",
            "description_2": "20211005SCBLSG22BRT0025272",
            "category": "Income"
        },
        {
            "transaction_date": "17/7/2021",
            "debit_amount": 0,
            "credit_amount": 13.47,
            "description_1": "SHOPEE SINGAPORE MP  SI NG 14JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Refunds"
        },
        {
            "transaction_date": "7/9/2021",
            "debit_amount": 0,
            "credit_amount": 10.67,
            "description_1": "APPLE.COM/BILL  IT UN 04SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Refunds"
        },
        {
            "transaction_date": "4/5/2021",
            "debit_amount": 79.82,
            "credit_amount": 0,
            "description_1": "STBILL  SI NG 29APR",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "11/5/2021",
            "debit_amount": 17.46,
            "credit_amount": 0,
            "description_1": "SPOTIFY  ST OC 09MAY",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "11/6/2021",
            "debit_amount": 17.46,
            "credit_amount": 0,
            "description_1": "SPOTIFY P156D847D3  ST OC 09JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 49.9,
            "credit_amount": 0,
            "description_1": "SINGTEL  SI NG 12JUN",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "11/7/2021",
            "debit_amount": 44.91,
            "credit_amount": 0,
            "description_1": "SINGTEL  SI NG 08JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "11/7/2021",
            "debit_amount": 17.46,
            "credit_amount": 0,
            "description_1": "SPOTIFY  ST OC 09JUL",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "11/8/2021",
            "debit_amount": 17.46,
            "credit_amount": 0,
            "description_1": "SPOTIFY  ST OC 09AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "12/8/2021",
            "debit_amount": 44.91,
            "credit_amount": 0,
            "description_1": "SINGTEL  SI NG 07AUG",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "9/9/2021",
            "debit_amount": 44.91,
            "credit_amount": 0,
            "description_1": "STBILL  SI NG 06SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 17.46,
            "credit_amount": 0,
            "description_1": "SPOTIFY  ST OC 09SEP",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        },
        {
            "transaction_date": "12/10/2021",
            "debit_amount": 17.46,
            "credit_amount": 0,
            "description_1": "SPOTIFY  ST OC 09OCT",
            "description_2": "1234-4567-7890-3245",
            "category": "Subscription"
        }
    ]
}, {
    "account_id": 1004,
    "date_registered": "30/10/2021",
    "name": "Chua Sheng Yu",
    "bank_name": "DBS",
    "password": "password123",
    "balance": 4000,
    "email": "csy@gmail.com",
    "transactions": [{
            "transaction_date": "27/6/2021",
            "debit_amount": 0,
            "credit_amount": 0.39,
            "description_1": "Incoming PayNow Ref 6994019",
            "description_2": "From: GOOGLE PAYMENT SINGAPORE PTE.",
            "category": "Cashback"
        },
        {
            "transaction_date": "5/9/2021",
            "debit_amount": 0,
            "credit_amount": 0.76,
            "description_1": "Incoming PayNow Ref 9376654",
            "description_2": "From: GOOGLE PAYMENT SINGAPORE PTE.",
            "category": "Cashback"
        },
        {
            "transaction_date": "16/10/2021",
            "debit_amount": 0,
            "credit_amount": 0.16,
            "description_1": "Incoming PayNow",
            "description_2": "From: GOOGLE PAYMENT SINGAPORE PTE.",
            "category": "Cashback"
        },
        {
            "transaction_date": "6/8/2021",
            "debit_amount": 0,
            "credit_amount": 500,
            "description_1": "",
            "description_2": "",
            "category": "Deposits"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": 28.5,
            "credit_amount": 0,
            "description_1": "CATHAY CINEPLEXES PTE SI NG 26JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Entertainment"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 15.5,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Benedict",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": 42.35,
            "credit_amount": 0,
            "description_1": "THETIRAMISUHERO SI NG 28APR",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/5/2021",
            "debit_amount": 7.1,
            "credit_amount": 0,
            "description_1": "",
            "description_2": "BURGER KING SINGAPORE",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "8/5/2021",
            "debit_amount": 34.64,
            "credit_amount": 0,
            "description_1": "LIFESTYLEMART SI NG 07MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "11/5/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 10MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": 1.3,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 11MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": 3.8,
            "credit_amount": 0,
            "description_1": "SPINELLI COFFEE SI NG 11MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "13/5/2021",
            "debit_amount": 1.3,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 12MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "15/5/2021",
            "debit_amount": 1.3,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 14MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "18/5/2021",
            "debit_amount": 2.9,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 17MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "19/5/2021",
            "debit_amount": 2.3,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 18MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "20/5/2021",
            "debit_amount": 2.6,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 19MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/5/2021",
            "debit_amount": 3.3,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 21MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "25/5/2021",
            "debit_amount": 3.4,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 24MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "26/5/2021",
            "debit_amount": 2.6,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 25MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "1/6/2021",
            "debit_amount": 3.4,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 31MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "8/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 07JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "15/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 14JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 15JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 17JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 1.3,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 17JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 0.6,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 17JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "19/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 18JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 21JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/6/2021",
            "debit_amount": 4.3,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 21JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "23/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 22JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/6/2021",
            "debit_amount": 29.69,
            "credit_amount": 0,
            "description_1": "GETZPAY*GREENDOT SI NG 21JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "25/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 23JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "26/6/2021",
            "debit_amount": 2.6,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 24JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 25JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "30/6/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 28JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "1/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 29JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "2/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 30JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "3/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 01JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 05JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "7/7/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "",
            "description_2": "CHANGI S AMENT",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "8/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 06JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "9/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 07JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "10/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 08JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "11/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 09JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "13/7/2021",
            "debit_amount": 13.95,
            "credit_amount": 0,
            "description_1": "COLD STORAGE CAUSEWAY SI NG 10JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "14/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 12JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 13JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "16/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 14JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "17/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 15JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "18/7/2021",
            "debit_amount": 3.4,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 16JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "18/7/2021",
            "debit_amount": 46.6,
            "credit_amount": 0,
            "description_1": "GREEN ON EARTH VEGETAR SI NG 16JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "18/7/2021",
            "debit_amount": 14,
            "credit_amount": 0,
            "description_1": "MR COCONUT-CHANGI CITY SI NG 16JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 19JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "23/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 21JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 22JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "25/7/2021",
            "debit_amount": 1.2,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 23JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "28/7/2021",
            "debit_amount": 3.3,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 26JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "29/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 27JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "30/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 28JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "31/7/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 29JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "31/7/2021",
            "debit_amount": 70.8,
            "credit_amount": 0,
            "description_1": "PIZZA HUT SINGAPORE SI NG 30JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "1/8/2021",
            "debit_amount": 1.2,
            "credit_amount": 0,
            "description_1": "CHILLIPADI SI NG 30JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "14/8/2021",
            "debit_amount": 19.9,
            "credit_amount": 0,
            "description_1": "GREEN ON EARTH VEGETAR SI NG 12AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "29/8/2021",
            "debit_amount": 44.8,
            "credit_amount": 0,
            "description_1": "GREEN ON EARTH VEGETAR SI NG 27AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "30/8/2021",
            "debit_amount": 11.9,
            "credit_amount": 0,
            "description_1": "",
            "description_2": "GREENDOT",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "24/9/2021",
            "debit_amount": 1,
            "credit_amount": 0,
            "description_1": "7-ELEVEN-MARISLING MRT SI NG 22SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "17/10/2021",
            "debit_amount": 14.9,
            "credit_amount": 0,
            "description_1": "GREEN ON EARTH VEGETAR SI NG 15OCT",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "19/10/2021",
            "debit_amount": 27.8,
            "credit_amount": 0,
            "description_1": "FLAVOURS BY SAUTE SI NG 16OCT",
            "description_2": "1234-3241-2200-2020",
            "category": "Food & Drink"
        },
        {
            "transaction_date": "22/6/2021",
            "debit_amount": 0,
            "credit_amount": 200,
            "description_1": "GST VOUCHER",
            "description_2": "GOVT PAYOUT",
            "category": "Government"
        },
        {
            "transaction_date": "27/7/2021",
            "debit_amount": 0,
            "credit_amount": 300,
            "description_1": "GST VOUCHER",
            "description_2": "GOVT PAYOUT",
            "category": "Government"
        },
        {
            "transaction_date": "30/5/2021",
            "debit_amount": 7.9,
            "credit_amount": 0,
            "description_1": "",
            "description_2": "GIANT SUPER",
            "category": "Groceries"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 0,
            "credit_amount": 9.35,
            "description_1": "Incoming PayNow Ref 5348320",
            "description_2": "From: Cassandra",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 0,
            "credit_amount": 3.82,
            "description_1": "Incoming PayNow Ref 5569471",
            "description_2": "From: Shervonne",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 0,
            "credit_amount": 3.82,
            "description_1": "Incoming PayNow Ref 9220144",
            "description_2": "From: Minah",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/4/2021",
            "debit_amount": 0,
            "credit_amount": 3.82,
            "description_1": "Incoming PayNow Ref 9220387",
            "description_2": "From: Olivia",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/4/2021",
            "debit_amount": 0,
            "credit_amount": 3.82,
            "description_1": "Incoming PayNow Ref 5688235",
            "description_2": "From: Bob",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/4/2021",
            "debit_amount": 0,
            "credit_amount": 7.5,
            "description_1": "Incoming PayNow Ref 5700074",
            "description_2": "From: Michael",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/4/2021",
            "debit_amount": 0,
            "credit_amount": 4.5,
            "description_1": "Incoming PayNow Ref 5703120",
            "description_2": "From: Angela",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/4/2021",
            "debit_amount": 0,
            "credit_amount": 18,
            "description_1": "Incoming PayNow Ref 6629030",
            "description_2": "From: Selena",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "1/5/2021",
            "debit_amount": 0,
            "credit_amount": 400,
            "description_1": "Incoming PayNow Ref 0060677",
            "description_2": "From: Marcus",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "7/5/2021",
            "debit_amount": 0,
            "credit_amount": 17,
            "description_1": "Incoming PayNow Ref 5862060",
            "description_2": "From: Alexia",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "7/5/2021",
            "debit_amount": 0,
            "credit_amount": 17,
            "description_1": "Incoming PayNow Ref 6075019",
            "description_2": "From: Selena",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "25/5/2021",
            "debit_amount": 0,
            "credit_amount": 10,
            "description_1": "Incoming PayNow Ref 8377259",
            "description_2": "From:Yi Qing",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "30/5/2021",
            "debit_amount": 0,
            "credit_amount": 400,
            "description_1": "Incoming PayNow Ref 3130055",
            "description_2": "From: Marcus",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "7/6/2021",
            "debit_amount": 0,
            "credit_amount": 10,
            "description_1": "Incoming PayNow Ref 6672190",
            "description_2": "From: Kade",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "10/6/2021",
            "debit_amount": 400,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Marcus",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "17/6/2021",
            "debit_amount": 0,
            "credit_amount": 1.2,
            "description_1": "Incoming PayNow Ref 6397782",
            "description_2": "From: jarren",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "21/6/2021",
            "debit_amount": 0,
            "credit_amount": 15,
            "description_1": "Incoming PayNow Ref 5244283",
            "description_2": "From: Diana",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": 0,
            "credit_amount": 27,
            "description_1": "Incoming PayNow Ref 5908941",
            "description_2": "From: Bob",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": 0,
            "credit_amount": 15,
            "description_1": "Incoming PayNow Ref 6427109",
            "description_2": "From: Bob",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "1/7/2021",
            "debit_amount": 0,
            "credit_amount": 400,
            "description_1": "Incoming PayNow Ref 6574728",
            "description_2": "From: Marcus",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "2/7/2021",
            "debit_amount": 0,
            "credit_amount": 18,
            "description_1": "Incoming PayNow Ref 7836720",
            "description_2": "From: Selena",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "10/7/2021",
            "debit_amount": 0,
            "credit_amount": 17,
            "description_1": "Incoming PayNow Ref 5835183",
            "description_2": "From: Selena",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "10/7/2021",
            "debit_amount": 0,
            "credit_amount": 17,
            "description_1": "Incoming PayNow Ref 6279503",
            "description_2": "From: Alexia",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "10/7/2021",
            "debit_amount": 0,
            "credit_amount": 4,
            "description_1": "Incoming PayNow Ref 6631282",
            "description_2": "From: Sally",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "26/7/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: 6 CHARMS SINGAPORE PTE. LTD.",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "27/7/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: 6 CHARMS SINGAPORE PTE. LTD.",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/7/2021",
            "debit_amount": 13.6,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: 6 CHARMS SINGAPORE PTE. LTD.",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "30/7/2021",
            "debit_amount": 0,
            "credit_amount": 35,
            "description_1": "Incoming PayNow Ref 7124008",
            "description_2": "From: Marcus",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "6/8/2021",
            "debit_amount": 0,
            "credit_amount": 500,
            "description_1": "Incoming PayNow Ref 6230748",
            "description_2": "From: Angela",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/8/2021",
            "debit_amount": 410,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ken",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": 0,
            "credit_amount": 10,
            "description_1": "Incoming PayNow Ref 6040724",
            "description_2": "From: Alexia",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "27/8/2021",
            "debit_amount": 0,
            "credit_amount": 25.3,
            "description_1": "Incoming PayNow Ref 6060485",
            "description_2": "From: Alexia",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": 0,
            "credit_amount": 7.5,
            "description_1": "Incoming PayNow Ref 9141827",
            "description_2": "From: Ah Junz",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "28/8/2021",
            "debit_amount": 2,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Celine",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "29/8/2021",
            "debit_amount": 0,
            "credit_amount": 400,
            "description_1": "Incoming PayNow Ref 2876598",
            "description_2": "From: Marcus",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "31/8/2021",
            "debit_amount": 25,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ken",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "1/9/2021",
            "debit_amount": 18,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Emma",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "2/9/2021",
            "debit_amount": 0,
            "credit_amount": 0.1,
            "description_1": "Incoming PayNow Ref 6168794",
            "description_2": "From: Michael",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "2/9/2021",
            "debit_amount": 0,
            "credit_amount": 45,
            "description_1": "Incoming PayNow Ref 6283362",
            "description_2": "From: Bob",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "4/9/2021",
            "debit_amount": 1.7,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ken",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "4/9/2021",
            "debit_amount": 20,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Ken",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "6/9/2021",
            "debit_amount": 0,
            "credit_amount": 306.5,
            "description_1": "Incoming PayNow Ref 5699202",
            "description_2": "From: Bob",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 0,
            "credit_amount": 12,
            "description_1": "Incoming PayNow Ref 6494429",
            "description_2": "From: Angela",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 0,
            "credit_amount": 1.25,
            "description_1": "Incoming PayNow Ref 0030247",
            "description_2": "From: Cassandra",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 0,
            "credit_amount": 1.25,
            "description_1": "Incoming PayNow Ref 2526853",
            "description_2": "From: Minah",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 0,
            "credit_amount": 1.25,
            "description_1": "Incoming PayNow Ref 6157167",
            "description_2": "From: Michael",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 0,
            "credit_amount": 1.25,
            "description_1": "Incoming PayNow Ref 6164293",
            "description_2": "From: Bob",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 0,
            "credit_amount": 1.25,
            "description_1": "Incoming PayNow Ref 6275736",
            "description_2": "From: Kelly",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 0,
            "credit_amount": 1.25,
            "description_1": "Incoming PayNow Ref 6287618",
            "description_2": "From: Shervonne",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 0,
            "credit_amount": 1.5,
            "description_1": "Incoming PayNow Ref 6292505",
            "description_2": "From: Angela",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "21/9/2021",
            "debit_amount": 0,
            "credit_amount": 5.55,
            "description_1": "Incoming PayNow Ref 7310219",
            "description_2": "From: Curry",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "21/9/2021",
            "debit_amount": 0,
            "credit_amount": 4.5,
            "description_1": "Incoming PayNow Ref 7376133",
            "description_2": "From: Peter",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "30/9/2021",
            "debit_amount": 0,
            "credit_amount": 400,
            "description_1": "Incoming PayNow Ref 6696208",
            "description_2": "From: James",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "30/9/2021",
            "debit_amount": 0,
            "credit_amount": 130,
            "description_1": "Incoming PayNow Ref 7637026",
            "description_2": "From: Peter",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "30/9/2021",
            "debit_amount": 0,
            "credit_amount": 160,
            "description_1": "Incoming PayNow Ref 8447744",
            "description_2": "From: Peter",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "30/9/2021",
            "debit_amount": 360,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: Harden",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "16/10/2021",
            "debit_amount": 0,
            "credit_amount": 27.8,
            "description_1": "Incoming PayNow",
            "description_2": "From: John",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "21/10/2021",
            "debit_amount": 0,
            "credit_amount": 16.6,
            "description_1": "Incoming PayNow",
            "description_2": "From: Johny",
            "category": "Peer-to-Peer"
        },
        {
            "transaction_date": "25/5/2021",
            "debit_amount": 68.98,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE GPAY SI NG 21MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "26/5/2021",
            "debit_amount": 66.54,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE GPAY SI NG 23MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "3/6/2021",
            "debit_amount": 0,
            "credit_amount": 68.98,
            "description_1": "SHOPEE SINGAPORE GPAY SI NG 31MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "11/6/2021",
            "debit_amount": 44.82,
            "credit_amount": 0,
            "description_1": "IHERB IHERB.COM IH ER 10JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "20/6/2021",
            "debit_amount": 2.59,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE GPAY SI NG 17JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "22/6/2021",
            "debit_amount": 52.88,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE GPAY SI NG 18JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "3/7/2021",
            "debit_amount": 32.9,
            "credit_amount": 0,
            "description_1": "SHOPEE SINGAPORE GPAY SI NG 30JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 41.45,
            "credit_amount": 0,
            "description_1": "TAOBAO.COM SI NG 20JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "23/7/2021",
            "debit_amount": 7.36,
            "credit_amount": 0,
            "description_1": "TAOBAO.COM SI NG 21JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "18/8/2021",
            "debit_amount": 146.31,
            "credit_amount": 0,
            "description_1": "CHALLENGER-PLAZASINGAP SI NG 15AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "29/8/2021",
            "debit_amount": 20,
            "credit_amount": 0,
            "description_1": "PAYPAL *SFA 68 05 27AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "1/9/2021",
            "debit_amount": 64.7,
            "credit_amount": 0,
            "description_1": "UNIQLO PLAZA SINGAPURA SI NG 30AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "14/9/2021",
            "debit_amount": 70.98,
            "credit_amount": 0,
            "description_1": "IHERB IHERB.COM IH ER 11SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Shopping"
        },
        {
            "transaction_date": "1/5/2021",
            "debit_amount": 27.1,
            "credit_amount": 0,
            "description_1": "GRAB* ADR-XUETJ8NGWHM6 SI NG 30APR",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "5/5/2021",
            "debit_amount": 12.8,
            "credit_amount": 0,
            "description_1": "GRAB* ADR-XUVBMAFWWIPH SI NG 04MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "7/5/2021",
            "debit_amount": 28.5,
            "credit_amount": 0,
            "description_1": "GRAB* ADR-XV7JU72GWILA SI NG 06MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "11/5/2021",
            "debit_amount": 16.2,
            "credit_amount": 0,
            "description_1": "GRAB* ADR-XVGVJLTWWHST SI NG 08MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": 8,
            "credit_amount": 0,
            "description_1": "BLUESG SI NG 10MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "16/6/2021",
            "debit_amount": 8,
            "credit_amount": 0,
            "description_1": "BLUESG SI NG 14JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "22/6/2021",
            "debit_amount": 43.5,
            "credit_amount": 0,
            "description_1": "GRAB* ADR-25XMOGIGWHWT SI NG 20JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": 30.6,
            "credit_amount": 0,
            "description_1": "GRAB* A-25MNQWSWWEMQ SI NG 25JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "14/7/2021",
            "debit_amount": 8,
            "credit_amount": 0,
            "description_1": "BLUESG SI NG 12JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 17.09,
            "credit_amount": 0,
            "description_1": "BUS/MRT 87610624 SI NG 07JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 18.09,
            "credit_amount": 0,
            "description_1": "BUS/MRT 88542984 SI NG 12JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "27/7/2021",
            "debit_amount": 10.49,
            "credit_amount": 0,
            "description_1": "BUS/MRT 89341272 SI NG 17JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "31/7/2021",
            "debit_amount": 14.22,
            "credit_amount": 0,
            "description_1": "BUS/MRT 90025566 SI NG 22JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "5/8/2021",
            "debit_amount": 13.43,
            "credit_amount": 0,
            "description_1": "BUS/MRT 90699348 SI NG 27JUL",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "6/8/2021",
            "debit_amount": 3.67,
            "credit_amount": 0,
            "description_1": "BUS/MRT 90963624 SI NG 01AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "15/8/2021",
            "debit_amount": 2.76,
            "credit_amount": 0,
            "description_1": "BUS/MRT 92277014 SI NG 06AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "18/8/2021",
            "debit_amount": 8,
            "credit_amount": 0,
            "description_1": "BLUESG SI NG 16AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "21/8/2021",
            "debit_amount": 5.2,
            "credit_amount": 0,
            "description_1": "BUS/MRT 93172022 SI NG 12AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "22/8/2021",
            "debit_amount": 15.1,
            "credit_amount": 0,
            "description_1": "GRAB* A-2CTBJP8GWFL9 SI NG 20AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "25/8/2021",
            "debit_amount": 18.5,
            "credit_amount": 0,
            "description_1": "GRAB* A-2DCS4EWWWG7K SI NG 24AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "1/9/2021",
            "debit_amount": 5.88,
            "credit_amount": 0,
            "description_1": "BUS/MRT 94982651 SI NG 23AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": 100,
            "credit_amount": 0,
            "description_1": "TRIBECAR SI NG 01SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "4/9/2021",
            "debit_amount": 100,
            "credit_amount": 0,
            "description_1": "TRIBECAR SI NG 02SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "7/9/2021",
            "debit_amount": 7.28,
            "credit_amount": 0,
            "description_1": "BUS/MRT 95856392 SI NG 28AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "7/9/2021",
            "debit_amount": 1.02,
            "credit_amount": 0,
            "description_1": "PARKING.SG BILL_AAB29D SI NG 04SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "8/9/2021",
            "debit_amount": 27.72,
            "credit_amount": 0,
            "description_1": "BLUESG SI NG 06SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "10/9/2021",
            "debit_amount": 10,
            "credit_amount": 0,
            "description_1": "",
            "description_2": "TRANSIT LINK PTE LTD",
            "category": "Transport"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 7.45,
            "credit_amount": 0,
            "description_1": "BUS/MRT 96745731 SI NG 02SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 8,
            "credit_amount": 0,
            "description_1": "BLUESG SI NG 13SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "17/9/2021",
            "debit_amount": 12.5,
            "credit_amount": 0,
            "description_1": "BUS/MRT 97809762 SI NG 08SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "23/9/2021",
            "debit_amount": 13.04,
            "credit_amount": 0,
            "description_1": "BUS/MRT 98818113 SI NG 14SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "29/9/2021",
            "debit_amount": 15.25,
            "credit_amount": 0,
            "description_1": "BUS/MRT 99782300 SI NG 21SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "5/10/2021",
            "debit_amount": 11.48,
            "credit_amount": 0,
            "description_1": "BUS/MRT 100585368 SI NG 25SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "9/10/2021",
            "debit_amount": 5.82,
            "credit_amount": 0,
            "description_1": "BUS/MRT 101319279 SI NG 30SEP",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "13/10/2021",
            "debit_amount": 8,
            "credit_amount": 0,
            "description_1": "BLUESG SI NG 11OCT",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "14/10/2021",
            "debit_amount": 13.72,
            "credit_amount": 0,
            "description_1": "BUS/MRT 102057976 SI NG 05OCT",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "21/10/2021",
            "debit_amount": 14.45,
            "credit_amount": 0,
            "description_1": "BUS/MRT 103109332 SI NG 12OCT",
            "description_2": "1234-3241-2200-2020",
            "category": "Transport"
        },
        {
            "transaction_date": "29/5/2021",
            "debit_amount": 19.9,
            "credit_amount": 0,
            "description_1": "SINGTEL MOBILE SINGAPO SI NG 26MAY",
            "description_2": "1234-3241-2200-2020",
            "category": "Utilities"
        },
        {
            "transaction_date": "29/6/2021",
            "debit_amount": 19.9,
            "credit_amount": 0,
            "description_1": "SINGTEL PREPAID HI!ACC SI NG 25JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Utilities"
        },
        {
            "transaction_date": "1/5/2021",
            "debit_amount": 28,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "2/5/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "",
            "description_2": "ZHENGHUA BR",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "11/5/2021",
            "debit_amount": 5.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "12/5/2021",
            "debit_amount": 8.3,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "14/5/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "17/5/2021",
            "debit_amount": 5.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "18/5/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "19/5/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "20/5/2021",
            "debit_amount": 5.3,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "20/5/2021",
            "debit_amount": 29.9,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "21/5/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "24/5/2021",
            "debit_amount": 5.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "24/5/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "",
            "description_2": "DBS ASIA HUB 2",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "31/5/2021",
            "debit_amount": 13.6,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "9/6/2021",
            "debit_amount": 89.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "15/6/2021",
            "debit_amount": 12.7,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "17/6/2021",
            "debit_amount": 7,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "18/6/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "20/6/2021",
            "debit_amount": 50,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "24/6/2021",
            "debit_amount": 3.3,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "25/6/2021",
            "debit_amount": 5.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": 7.6,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "27/6/2021",
            "debit_amount": 15.9,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "4/7/2021",
            "debit_amount": 14,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "5/7/2021",
            "debit_amount": 5.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "6/7/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "8/7/2021",
            "debit_amount": 2.4,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "12/7/2021",
            "debit_amount": 23.16,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "12/7/2021",
            "debit_amount": 3.4,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "13/7/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 6.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "21/7/2021",
            "debit_amount": 4.4,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "22/7/2021",
            "debit_amount": 5.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "23/7/2021",
            "debit_amount": 5.3,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "23/7/2021",
            "debit_amount": 32.11,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "8/8/2021",
            "debit_amount": 27.33,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "23/8/2021",
            "debit_amount": 2.5,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "23/8/2021",
            "debit_amount": 12.4,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "24/8/2021",
            "debit_amount": 15.69,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "3/9/2021",
            "debit_amount": 20,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "11/9/2021",
            "debit_amount": 16.04,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 12.5,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "24/9/2021",
            "debit_amount": 26,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "4/10/2021",
            "debit_amount": 5.8,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "11/10/2021",
            "debit_amount": 26.1,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "Lucas",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "16/10/2021",
            "debit_amount": 21,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "16/10/2021",
            "debit_amount": 13.9,
            "credit_amount": 0,
            "description_1": "TOP-UP TO PAYLAH! :",
            "description_2": "",
            "category": "Withdrawal"
        },
        {
            "transaction_date": "27/4/2021",
            "debit_amount": 2.5,
            "credit_amount": 0,
            "description_1": "ActiveSG DD 20210427RN001689",
            "description_2": "",
            "category": "Health"
        },
        {
            "transaction_date": "30/4/2021",
            "debit_amount": 2.5,
            "credit_amount": 0,
            "description_1": "ActiveSG DD 20210430RN001335",
            "description_2": "IIRGPCSG300421A0037081",
            "category": "Health"
        },
        {
            "transaction_date": "3/5/2021",
            "debit_amount": 193,
            "credit_amount": 0,
            "description_1": "",
            "description_2": "SKINLAB THE MED SPA",
            "category": "Health"
        },
        {
            "transaction_date": "6/8/2021",
            "debit_amount": 27.81,
            "credit_amount": 0,
            "description_1": "PayNow Transfer",
            "description_2": "To: ADVANCED DENTAL CLINIC BUKIT PA",
            "category": "Health"
        },
        {
            "transaction_date": "1/9/2021",
            "debit_amount": 45.5,
            "credit_amount": 0,
            "description_1": "SL AESTHETIC CLINIC-PS SI NG 30AUG",
            "description_2": "1234-3241-2200-2020",
            "category": "Health"
        },
        {
            "transaction_date": "5/6/2021",
            "debit_amount": 0,
            "credit_amount": 914.24,
            "description_1": "PERSOLKELLY Singapor",
            "description_2": "Payroll09200 Payroll09200",
            "category": "Income"
        },
        {
            "transaction_date": "6/7/2021",
            "debit_amount": 0,
            "credit_amount": 1200,
            "description_1": "PERSOLKELLY Singapor",
            "description_2": "Payroll09200 Payroll09200",
            "category": "Income"
        },
        {
            "transaction_date": "5/8/2021",
            "debit_amount": 0,
            "credit_amount": 1227.69,
            "description_1": "PERSOLKELLY Singapor",
            "description_2": "Payroll09200 Payroll09200",
            "category": "Income"
        },
        {
            "transaction_date": "17/5/2021",
            "debit_amount": 127.46,
            "credit_amount": 0,
            "description_1": "AIA",
            "description_2": "L123",
            "category": "Insurance"
        },
        {
            "transaction_date": "15/6/2021",
            "debit_amount": 127.46,
            "credit_amount": 0,
            "description_1": "AIA",
            "description_2": "L123",
            "category": "Insurance"
        },
        {
            "transaction_date": "15/7/2021",
            "debit_amount": 127.46,
            "credit_amount": 0,
            "description_1": "AIA",
            "description_2": "L123",
            "category": "Insurance"
        },
        {
            "transaction_date": "16/8/2021",
            "debit_amount": 127.46,
            "credit_amount": 0,
            "description_1": "AIA",
            "description_2": "L123",
            "category": "Insurance"
        },
        {
            "transaction_date": "15/9/2021",
            "debit_amount": 127.46,
            "credit_amount": 0,
            "description_1": "AIA",
            "description_2": "",
            "category": "Insurance"
        },
        {
            "transaction_date": "15/10/2021",
            "debit_amount": 127.46,
            "credit_amount": 0,
            "description_1": "AIA",
            "description_2": "L123",
            "category": "Insurance"
        },
        {
            "transaction_date": "22/6/2021",
            "debit_amount": 26.71,
            "credit_amount": 0,
            "description_1": "UDEMY UD EM 20JUN",
            "description_2": "1234-3241-2200-2020",
            "category": "Education"
        },
        {
            "transaction_date": "10/5/2021",
            "debit_amount": 150,
            "credit_amount": 0,
            "description_1": "TO MSA: 123-45678-2",
            "description_2": "",
            "category": "Savings"
        },
        {
            "transaction_date": "10/6/2021",
            "debit_amount": 150,
            "credit_amount": 0,
            "description_1": "TO MSA: 123-45678-2",
            "description_2": "",
            "category": "Savings"
        },
        {
            "transaction_date": "10/7/2021",
            "debit_amount": 150,
            "credit_amount": 0,
            "description_1": "TO MSA: 123-45678-2",
            "description_2": "",
            "category": "Savings"
        },
        {
            "transaction_date": "10/8/2021",
            "debit_amount": 150,
            "credit_amount": 0,
            "description_1": "TO MSA: 123-45678-2",
            "description_2": "",
            "category": "Savings"
        },
        {
            "transaction_date": "10/9/2021",
            "debit_amount": 150,
            "credit_amount": 0,
            "description_1": "TO MSA: 123-45678-2",
            "description_2": "",
            "category": "Savings"
        },
        {
            "transaction_date": "10/10/2021",
            "debit_amount": 150,
            "credit_amount": 0,
            "description_1": "TO MSA: 123-45678-2",
            "description_2": "",
            "category": "Savings"
        }
    ]
}]

collection.delete_many({})
# post = {"name" : "tim", "score": 5}
collection.insert_many(userData) # -- insert bulk json
# pprint.pprint(collection.find_one())

