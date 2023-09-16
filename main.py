from fastapi import FastAPI, Query, HTTPException
import get_cur

app = FastAPI()

RATES = {
    "AED": "AED",  # United Arab Emirates Dirham
    "AFN": "AFN",  # Afghan Afghani
    "ALL": "ALL",  # Albanian Lek
    "AMD": "AMD",  # Armenian Dram
    "ANG": "ANG",  # Netherlands Antillean Guilder
    "AOA": "AOA",  # Angolan Kwanza
    "ARS": "ARS",  # Argentine Peso
    "AUD": "AUD",  # Australian Dollar
    "AWG": "AWG",  # Aruban Florin
    "AZN": "AZN",  # Azerbaijani Manat
    "BAM": "BAM",  # Bosnia-Herzegovina Convertible Mark
    "BBD": "BBD",  # Barbadian Dollar
    "BDT": "BDT",  # Bangladeshi Taka
    "BGN": "BGN",  # Bulgarian Lev
    "BHD": "BHD",  # Bahraini Dinar
    "BIF": "BIF",  # Burundian Franc
    "BMD": "BMD",  # Bermudan Dollar
    "BND": "BND",  # Brunei Dollar
    "BOB": "BOB",  # Bolivian Boliviano
    "BRL": "BRL",  # Brazilian Real
    "BSD": "BSD",  # Bahamian Dollar
    "BTC": "BTC",  # Bitcoin
    "BTN": "BTN",  # Bhutanese Ngultrum
    "BWP": "BWP",  # Botswanan Pula
    "BYN": "BYN",  # Belarusian Ruble
    "BYR": "BYR",  # Belarusian Ruble (pre-2016)
    "BZD": "BZD",  # Belize Dollar
    "CAD": "CAD",  # Canadian Dollar
    "CDF": "CDF",  # Congolese Franc
    "CHF": "CHF",  # Swiss Franc
    "CLF": "CLF",  # Chilean Unit of Account (UF)
    "CLP": "CLP",  # Chilean Peso
    "CNH": "CNH",  # Chinese Yuan (Offshore)
    "CNY": "CNY",  # Chinese Yuan
    "COP": "COP",  # Colombian Peso
    "CRC": "CRC",  # Costa Rican Colón
    "CUC": "CUC",  # Cuban Convertible Peso
    "CUP": "CUP",  # Cuban Peso
    "CVE": "CVE",  # Cape Verdean Escudo
    "CZK": "CZK",  # Czech Republic Koruna
    "DJF": "DJF",  # Djiboutian Franc
    "DKK": "DKK",  # Danish Krone
    "DOP": "DOP",  # Dominican Peso
    "DZD": "DZD",  # Algerian Dinar
    "EEK": "EEK",  # Estonian Kroon
    "EGP": "EGP",  # Egyptian Pound
    "ERN": "ERN",  # Eritrean Nakfa
    "ETB": "ETB",  # Ethiopian Birr
    "EUR": "EUR",  # Euro
    "FJD": "FJD",  # Fijian Dollar
    "FKP": "FKP",  # Falkland Islands Pound
    "GBP": "GBP",  # British Pound Sterling
    "GEL": "GEL",  # Georgian Lari
    "GGP": "GGP",  # Guernsey Pound
    "GHS": "GHS",  # Ghanaian Cedi
    "GIP": "GIP",  # Gibraltar Pound
    "GMD": "GMD",  # Gambian Dalasi
    "GNF": "GNF",  # Guinean Franc
    "GTQ": "GTQ",  # Guatemalan Quetzal
    "GYD": "GYD",  # Guyanaese Dollar
    "HKD": "HKD",  # Hong Kong Dollar
    "HNL": "HNL",  # Honduran Lempira
    "HRK": "HRK",  # Croatian Kuna
    "HTG": "HTG",  # Haitian Gourde
    "HUF": "HUF",  # Hungarian Forint
    "IDR": "IDR",  # Indonesian Rupiah
    "ILS": "ILS",  # Israeli New Sheqel
    "IMP": "IMP",  # Manx pound
    "INR": "INR",  # Indian Rupee
    "IQD": "IQD",  # Iraqi Dinar
    "IRR": "IRR",  # Iranian Rial
    "ISK": "ISK",  # Icelandic Króna
    "JEP": "JEP",  # Jersey Pound
    "JMD": "JMD",  # Jamaican Dollar
    "JOD": "JOD",  # Jordanian Dinar
    "JPY": "JPY",  # Japanese Yen
    "KES": "KES",  # Kenyan Shilling
    "KGS": "KGS",  # Kyrgystani Som
    "KHR": "KHR",  # Cambodian Riel
    "KMF": "KMF",  # Comorian Franc
    "KPW": "KPW",  # North Korean Won
    "KRW": "KRW",  # South Korean Won
    "KWD": "KWD",  # Kuwaiti Dinar
    "KYD": "KYD",  # Cayman Islands Dollar
    "KZT": "KZT",  # Kazakhstani Tenge
    "LAK": "LAK",  # Laotian Kip
    "LBP": "LBP",  # Lebanese Pound
    "LKR": "LKR",  # Sri Lankan Rupee
    "LRD": "LRD",  # Liberian Dollar
    "LSL": "LSL",  # Lesotho Loti
    "LTL": "LTL",  # Lithuanian Litas
    "LVL": "LVL",  # Latvian Lats
    "LYD": "LYD",  # Libyan Dinar
    "MAD": "MAD",  # Moroccan Dirham
    "MDL": "MDL",  # Moldovan Leu
    "MGA": "MGA",  # Malagasy Ariary
    "MKD": "MKD",  # Macedonian Denar
    "MMK": "MMK",  # Myanmar Kyat
    "MNT": "MNT",  # Mongolian Tugrik
    "MOP": "MOP",  # Macanese Pataca
    "MRO": "MRO",  # Mauritanian Ouguiya (pre-2018)
    "MRU": "MRU",  # Mauritanian Ouguiya
    "MUR": "MUR",  # Mauritian Rupee
    "MVR": "MVR",  # Maldivian Rufiyaa
    "MWK": "MWK",  # Malawian Kwacha
    "MXN": "MXN",  # Mexican Peso
    "MYR": "MYR",  # Malaysian Ringgit
    "MZN": "MZN",  # Mozambican Metical
    "NAD": "NAD",  # Namibian Dollar
    "NGN": "NGN",  # Nigerian Naira
    "NIO": "NIO",  # Nicaraguan Córdoba
    "NOK": "NOK",  # Norwegian Krone
    "NPR": "NPR",  # Nepalese Rupee
    "NZD": "NZD",  # New Zealand Dollar
    "OMR": "OMR",  # Omani Rial
    "PAB": "PAB",  # Panamanian Balboa
    "PEN": "PEN",  # Peruvian Sol
    "PGK": "PGK",  # Papua New Guinean Kina
    "PHP": "PHP",  # Philippine Peso
    "PKR": "PKR",  # Pakistani Rupee
    "PLN": "PLN",  # Polish Zloty
    "PYG": "PYG",  # Paraguayan Guarani
    "QAR": "QAR",  # Qatari Rial
    "RON": "RON",  # Romanian Leu
    "RSD": "RSD",  # Serbian Dinar
    "RUB": "RUB",  # Russian Ruble
    "RWF": "RWF",  # Rwandan Franc
    "SAR": "SAR",  # Saudi Riyal
    "SBD": "SBD",  # Solomon Islands Dollar
    "SCR": "SCR",  # Seychellois Rupee
    "SDG": "SDG",  # Sudanese Pound
    "SEK": "SEK",  # Swedish Krona
    "SGD": "SGD",  # Singapore Dollar
    "SHP": "SHP",  # Saint Helena Pound
    "SLL": "SLL",  # Sierra Leonean Leone
    "SOS": "SOS",  # Somali Shilling
    "SRD": "SRD",  # Surinamese Dollar
    "SSP": "SSP",  # South Sudanese Pound
    "STD": "STD",  # São Tomé and Príncipe Dobra (pre-2018)
    "STN": "STN",  # São Tomé and Príncipe Dobra
    "SVC": "SVC",  # Salvadoran Colón
    "SYP": "SYP",  # Syrian Pound
    "SZL": "SZL",  # Swazi Lilangeni
    "THB": "THB",  # Thai Baht
    "TJS": "TJS",  # Tajikistani Somoni
    "TMT": "TMT",  # Turkmenistani Manat
    "TND": "TND",  # Tunisian Dinar
    "TOP": "TOP",  # Tongan Pa'anga
    "TRY": "TRY",  # Turkish Lira
    "TTD": "TTD",  # Trinidad and Tobago Dollar
    "TWD": "TWD",  # New Taiwan Dollar
    "TZS": "TZS",  # Tanzanian Shilling
    "UAH": "UAH",  # Ukrainian Hryvnia
    "UGX": "UGX",  # Ugandan Shilling
    "USD": "USD",  # United States Dollar
    "UYU": "UYU",  # Uruguayan Peso
    "UZS": "UZS",  # Uzbekistan Som
    "VEF": "VEF",  # Venezuelan Bolívar Fuerte (Old)
    "VES": "VES",  # Venezuelan Bolívar Soberano
    "VND": "VND",  # Vietnamese Dong
    "VUV": "VUV",  # Vanuatu Vatu
    "WST": "WST",  # Samoan Tala
    "XAF": "XAF",  # CFA Franc BEAC
    "XAG": "XAG",  # Silver (troy ounce)
    "XAU": "XAU",  # Gold (troy ounce)
    "XCD": "XCD",  # East Caribbean Dollar
    "XDR": "XDR",  # Special Drawing Rights
    "XOF": "XOF",  # CFA Franc BCEAO
    "XPD": "XPD",  # Palladium Ounce
    "XPF": "XPF",  # CFP Franc
    "XPT": "XPT",  # Platinum Ounce
    "YER": "YER",  # Yemeni Rial
    "ZAR": "ZAR",  # South African Rand
    "ZMK": "ZMK",  # Zambian Kwacha (pre-2013)
    "ZMW": "ZMW",  # Zambian Kwacha
    "ZWL": "ZWL"   # Zimbabwean Dollar
}

@app.get("/api/rates")
def get_conversion_rate(from_currency: str = Query(..., alias="from"), to_currency: str = Query(..., alias="to"), value: float = 1.0):
    if from_currency ==  to_currency:
        raise HTTPException(status_code=400, detail=f"C'mon, you do not really need to convert {from_currency} to {from_currency}")
    if from_currency not in RATES:
        raise HTTPException(status_code=400, detail=f"Currency '{from_currency}' not supported")
    if to_currency not in RATES:
        raise HTTPException(status_code=400, detail=f"Currency '{to_currency}' not supported")
    
    if from_currency != 'USD':
        conversion_rate_temp = get_cur.get_the_currency(to_cur=from_currency)
        value = value / conversion_rate_temp
    
    conversion_rate = get_cur.get_the_currency(to_cur=to_currency)

    return {"result": conversion_rate * value}
