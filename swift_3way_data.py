import random
import string
import uuid
from datetime import datetime, timedelta
import pandas as pd

def random_string(prefix="", length=8):
    return prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def random_bool():
    return random.choice([True, False])

def random_date(start, end, with_time=False):
    dt = start + timedelta(days=random.randint(0, (end - start).days))
    return dt.strftime("%d-%m-%Y") if not with_time else dt.strftime("%d-%m-%Y %H:%M:%S")



EXPOSURE_MT = {'103':'GROUP1','110':'GROUP1','202':'GROUP1','8':'GROUP1','9':'GROUP1','700':'GROUP2','701':'GROUP2','707':'GROUP3','708':'GROUP3','759':'GROUP4','760':'GROUP5','761':'GROUP5','765':'GROUP6','767':'GROUP7','775':'GROUP7'}


def make_swift(uumid, amt, ccy, mt, vdate, corr, scenario="", creation_time=None):
    return {
        "Scenario": scenario,
        "ValidationRequested": random.choice(["MAXIMUM", "MINIMUM"]),
        "ValidationPassed": random.choice(["MAXIMUM", "MINIMUM"]),
        "Class": random.choice(["NORMAL"]),
        "TextReadonly": random_bool(),
        "DeleteInhibited": random_bool(),
        "TextModified": random_bool(),
        "Partial": random_bool(),
        "Status": random.choice(["LIVE", "COMPLETED"]),
        "CreationApplication": random_string("APP"),
        "CreationMpfnName": random_string("MPFN"),
        "CreationRoutingPoint": random_string("RTP"),
        "CreationOperator": random.choice(["SYSTEM"]),
        "CreationDate": creation_time if creation_time else datetime.today().strftime("%d-%m-%Y %H:%M:%S"),
        "ModificationOperator": random_string("MOP"),
        "ModificationDate": random_date(datetime(2023,1,1), datetime(2025,12,31)),
        "Uumid": uumid,
        "UumidSuffix": random.randint(1,9),
        "SenderCorrespondentType": random.choice(["Bank", "Broker", "Other"]),
        "SenderCorrespondentInstitutionName": random.choice(["HDFC", "SBI", "CITI"]),
        "FormatName": random.choice(["MX", "Swift"]),
        "SubFormat": random.choice(["INPUT", "OUTPUT"]),
        "SyntaxTableVersion": random.randint(1,5),
        "Nature": random.choice(["PAY","MSG","ENQ"]),
        "NetworkApplicationIndication": random_string("NAI"),
        "Type": mt,
        "Live": random_bool(),
        "NetworkPriority": random.choice(["HIGH","NORM","LOW"]),
        "DeliveryOverdueWarningRequired": random_bool(),
        "NetworkDeliveryNotificationRequired": random_bool(),
        "UserReferenceText": random_string("URT"),
        "FinValueDate": vdate,
        "FinCurrencyAmount": f"{ccy}{amt:.2f}" if amt else None,
        "TransactionReference": random_string("TRX"),
        "RelatedTransactionReference": random_string("RTR"),
        "PossibleDuplicate": random_bool(),
        "MessageIdentifier": str(uuid.uuid4()),
        "SenderSwiftAddress": random_string("SND"),
        "ReceiverSwiftAddress": random_string("RCV"),
        "Service": random_string("SRV"),
        "ExpiryDateTime": random_date(datetime(2023,1,1), datetime(2025,12,31), with_time=True),
        "HasVerifiableField": random_bool(),
        "TransactionNumber": random.randint(10000,99999),
        "SecondarySenderCorrespondentInstitutionName": random_string("SEC"),
        "SenderCorrespondentDepartment": random_string("DEP"),
        "MessageUserGroup": random_string("MUG"),
        "RequestorDn": random_string("REQ"),
        "RequestType": random.choice(["TYPEA","TYPEB"]),
        "RequestSubtype": random.choice(["SUB1","SUB2"]),
        "XmlQueryReference1": random_string("XQ1"),
        "XmlQueryReference3": random_string("XQ3"),
        "PayloadType": random.choice(["XML","JSON"]),
        "PayloadAttributeName": random_string("PAN"),
        "PayloadAttributeValue": random_string("PAV"),
        "ServiceUri": random_string("URI"),
        "MessageTypeUri": random_string("MTU"),
        "MessageTypeUploadId": str(uuid.uuid4()),
        "ServiceLevelAgreement": random_string("SLA"),
        "E2ETransactionReference": random_string("E2E"),
        "SecondaryFormatName": random_string("SFN"),
        "MessageSecondaryIdentifier": random_string("MSI"),
        "SecondaryService": random_string("SSRV"),
        "SecondarySyntaxTableVersion": random.randint(1,5),
        "MessageSecondaryType": random_string("MST"),
        "TranlationResult": random_string("TRS"),
        "SecondaryUumid": random_string("SUU"),
        "HeaderIdentifier": random_string("HDR"),
        "TransactionManagerResult": random_string("TMR"),
        "CasSenderReference": random_string("CSR"),
        "RecoveryAcceptInfo": random_string("RAI"),
        "UserIssuedAsPde": random_bool(),
        "MessageSecondaryUserGroup": random_string("MSUG"),
        "CasTargetRoutingPoint": random_string("CTRP"),
        "ApplicationSenderReference": random_string("ASR"),
        "RequiredSignatureNRS": random_bool(),
        "SimplifiedScreen": random_bool()
    }

def make_pp(uumid, amt, ccy, mt, vdate, corr, scenario="", creation_time=None):
    return {
        "Scenario": scenario,
        "MTTYPE": "MT" + mt,
        "CORRESPONSDENT": corr,
        "VALUE DATE": datetime.strptime(vdate, "%y%m%d").strftime("%d-%m-%Y"),
        "CCY": ccy,
        "AMOUNT": amt,
        "REFERENCE NUMBER": uumid[15:35],
        "EVENT REFERENCE": random_string("EVT"),
        "UNIQUE ID": str(uuid.uuid4())[:12],
        "CREATION DATE": datetime.today().strftime("%d-%m-%Y"),
        "CREATION TIME": creation_time if creation_time else datetime.today().strftime("%H:%M:%S"),
    }

# Need to change and append custom text in Reference_number here in CBS.
def make_cbs(uumid,amt,ccy,scenario="",creation_time=None):
    return{
        "SCENARIO":scenario,
        "CBS_CCY":ccy,
        "CBS_AMOUNT":amt,
        "REFERENCE_NUMBER":uumid[15:35],
        "CREATION_DATE":datetime.today().strftime("%d-%m-%Y"),
        "CREATION_TIME": creation_time if creation_time else datetime.today().strftime("%H:%M:%S")
    }


def generate_records():
    swift_records,pp_records,cbs_records=[],[],[]

    def exposure_details():
        mt = random.choice(list(EXPOSURE_MT.keys()))
        ccy = random.choice(["USD","EUR","INR","GBP"])
        amt = round(random.uniform(1000,9999),2)
        vdate = datetime.today().strftime("%y%m%d")
        uumid = random_string("UUM", 25)
        corr = uumid[1:9] + uumid[8:11]
        return uumid, amt, ccy, mt, vdate, corr
    
    #Exposure Data
    # One to One (ALL MTs) Present in ALL

    for i in range(10):
        uumid, amt, ccy, mt, vdate, corr=exposure_details()
        cbs_records.append(make_cbs(uumid,amt,ccy,"Scenario 1",datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        pp_records.append(make_pp(uumid, amt, ccy, mt, vdate, corr,"Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        swift_records.append(make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

    return pd.DataFrame(cbs_records),pd.DataFrame(swift_records),pd.DataFrame(pp_records)

def generate_file_names():
    cbs_file_name = "3WAY_TRADE_CBS_GL_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".txt"
    swift_file_name = "SWIFT_GL_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".xlsx"
    pp_file_name = "2WAY_PRODUCT_PROCESSOR_GL_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".txt"
    return cbs_file_name,swift_file_name,pp_file_name

cbs_df,swift_df,pp_df=generate_records()
cbs_file_name,swift_file_name,pp_file_name=generate_file_names()

cbs_df.to_csv(cbs_file_name, index=False, sep='|')
pp_df.to_csv(pp_file_name, index=False, sep='|')
swift_df.to_excel(swift_file_name, index=False)