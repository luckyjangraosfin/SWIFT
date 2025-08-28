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


EXPOSURE_MT = {'103','110','202','8','9','700','701','707','708','759','760','761','765','767','775'}
NON_EXPOSURE_MT = [str(i) for i in range(100, 800) if str(i) not in EXPOSURE_MT]
FREE_TEXT_MT = {'199','299','799','999'}


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
        "TransactionNumber": random.randint(1000000,9999999),
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

def make_pp(uumid, amt, ccy, mt, vdate, corr, evt_ref, scenario="", creation_time=None):
    return {
        "Scenario": scenario,
        "MTTYPE": "MT" + mt,
        "CORRESPONSDENT": corr,
        "VALUE DATE": datetime.strptime(vdate, "%y%m%d").strftime("%d-%m-%Y"),
        "CCY": ccy,
        "AMOUNT": amt,
        "REFERENCE NUMBER": uumid[15:35],
        "EVENT REFERENCE": evt_ref,
        "UNIQUE ID": str(uuid.uuid4())[:12],
        "CREATION DATE": datetime.today().strftime("%d-%m-%Y"),
        "CREATION TIME": creation_time if creation_time else datetime.today().strftime("%H:%M:%S"),
    }


def generate_scenarios():
    swift_records, pp_records = [], []

    def common_fields():
        mt = random.choice(NON_EXPOSURE_MT)
        ccy = random.choice(["USD","EUR","INR","GBP"])
        amt = round(random.uniform(1000,9999), 2)
        vdate = datetime.today().strftime("%y%m%d")
        uumid = random_string("UUM", 25)
        corr = uumid[1:9] + uumid[8:11]
        evt_ref = f"CR{random.randint(1,100):03d}" 

        return uumid, amt, ccy, mt, vdate, corr, evt_ref

    def free_common_fields():
        mt = random.choice(list(FREE_TEXT_MT))
        vdate = datetime.today().strftime("%y%m%d")
        uumid = random_string("UUM", 25)
        corr = uumid[1:9] + uumid[8:11]
        return uumid, None, None, mt, vdate, corr, None

    # Scenario 1: One-to-one (5 records)
    for _ in range(5):
        uumid, amt, ccy, mt, vdate, corr, evt_ref = common_fields()
        base_time = datetime.now()
        swift_records.append(make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario1", base_time.strftime("%d-%m-%Y %H:%M:%S")))
        pp_records.append(make_pp(uumid, amt, ccy, mt, vdate, corr, evt_ref, "Scenario1", base_time.strftime("%H:%M:%S")))

    # Scenario 2: SWIFT only
    uumid, amt, ccy, mt, vdate, corr, evt_ref = common_fields()
    swift_records.append(make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario2"))

    # Scenario 3: PP only
    uumid, amt, ccy, mt, vdate, corr, evt_ref = common_fields()
    pp_records.append(make_pp(uumid, amt, ccy, mt, vdate, corr, evt_ref, "Scenario3"))

    # Scenario 4: Two PP vs one SWIFT
    uumid, amt, ccy, mt, vdate, corr, evt_ref = common_fields()
    base_time = datetime.now()
    swift_records.append(make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario4", base_time.strftime("%d-%m-%Y %H:%M:%S")))
    pp_records.append(make_pp(uumid, amt, ccy, mt, vdate, corr, evt_ref, "Scenario4", (base_time+timedelta(seconds=10)).strftime("%H:%M:%S")))
    pp_records.append(make_pp(uumid, amt, ccy, mt, vdate, corr, None, "Scenario4", (base_time+timedelta(seconds=20)).strftime("%H:%M:%S")))

    # Scenario 5: Two SWIFT vs one PP
    uumid, amt, ccy, mt, vdate, corr, evt_ref = common_fields()
    base_time = datetime.now()
    pp_records.append(make_pp(uumid, amt, ccy, mt, vdate, corr, evt_ref, "Scenario5", base_time.strftime("%H:%M:%S")))
    swift_records.append(make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario5", (base_time+timedelta(seconds=5)).strftime("%d-%m-%Y %H:%M:%S")))
    swift_records.append(make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario5", (base_time+timedelta(seconds=15)).strftime("%d-%m-%Y %H:%M:%S")))

    # Scenario 6: Two PP without SWIFT
    uumid, amt, ccy, mt, vdate, corr, evt_ref = common_fields()
    base_time = datetime.now()
    alt_evt_ref = random.choice([f"CR{str(i).zfill(3)}" for i in range(1, 101) if f"CR{str(i).zfill(3)}" != evt_ref])

    pp_records.append(make_pp(uumid, amt, ccy, mt, vdate, corr, evt_ref, "Scenario6", base_time.strftime("%H:%M:%S")))
    pp_records.append(make_pp(uumid, amt, ccy, mt, vdate, corr, alt_evt_ref, "Scenario6", (base_time+timedelta(seconds=30)).strftime("%H:%M:%S")))

    # Scenario 7: One PP with two SWIFT
    uumid, amt, ccy, mt, vdate, corr, evt_ref = common_fields()
    base_time = datetime.now()
    pp_records.append(make_pp(uumid, amt, ccy, mt, vdate, corr, evt_ref, "Scenario7", base_time.strftime("%H:%M:%S")))
    swift_records.append(make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario7", (base_time+timedelta(seconds=40)).strftime("%d-%m-%Y %H:%M:%S")))
    swift_records.append(make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario7", (base_time+timedelta(seconds=60)).strftime("%d-%m-%Y %H:%M:%S")))

    # Free-text Scenarios (199,299,799,999)
    # freeScenario1: One-to-one
    for _ in range(2):
        uumid, amt, ccy, mt, vdate, corr, evt_ref = free_common_fields()
        base_time = datetime.now()
        swift_records.append(make_swift(uumid, None, None, mt, vdate, corr, "freeScenario1", base_time.strftime("%d-%m-%Y %H:%M:%S")))
        pp_records.append(make_pp(uumid, None, None, mt, vdate, corr, evt_ref, "freeScenario1", base_time.strftime("%H:%M:%S")))

    # freeScenario2: One PP vs two SWIFT
    uumid, amt, ccy, mt, vdate, corr, evt_ref = free_common_fields()
    base_time = datetime.now()
    swift_records.append(make_swift(uumid, None, None, mt, vdate, corr, "freeScenario2", base_time.strftime("%d-%m-%Y %H:%M:%S")))
    swift_records.append(make_swift(uumid, None, None, mt, vdate, corr, "freeScenario2", base_time.strftime("%d-%m-%Y %H:%M:%S")))
    pp_records.append(make_pp(uumid, None, None, mt, vdate, corr, evt_ref, "freeScenario2", base_time.strftime("%H:%M:%S")))

    # freeScenario3: Only in PP
    uumid, amt, ccy, mt, vdate, corr, evt_ref = free_common_fields()
    base_time = datetime.now()
    pp_records.append(make_pp(uumid, None, None, mt, vdate, corr, evt_ref, "freeScenario3", base_time.strftime("%H:%M:%S")))

    # freeScenario4: Two in PP vs one SWIFT
    uumid, amt, ccy, mt, vdate, corr, evt_ref = free_common_fields()
    base_time = datetime.now()

    pp_records.append(make_pp(uumid, None, None, mt, vdate, corr, evt_ref, "freeScenario4", base_time.strftime("%H:%M:%S")))
    pp_records.append(make_pp(uumid, None, None, mt, vdate, corr, None , "freeScenario4", (base_time+timedelta(seconds=15)).strftime("%H:%M:%S")))
    swift_records.append(make_swift(uumid, None, None, mt, vdate, corr, "freeScenario4", base_time.strftime("%d-%m-%Y %H:%M:%S")))

    # freeScenario5: Two PP vs two SWIFT
    uumid, amt, ccy, mt, vdate, corr, evt_ref = free_common_fields()
    base_time = datetime.now()
    alt_evt_ref = random.choice([f"CR{str(i).zfill(3)}" for i in range(1, 101) if f"CR{str(i).zfill(3)}" != evt_ref])

    pp_records.append(make_pp(uumid, None, None, mt, vdate, corr, evt_ref, "freeScenario5", base_time.strftime("%H:%M:%S")))
    pp_records.append(make_pp(uumid, None, None, mt, vdate, corr, alt_evt_ref, "freeScenario5", (base_time+timedelta(seconds=10)).strftime("%H:%M:%S")))
    swift_records.append(make_swift(uumid, None, None, mt, vdate, corr, "freeScenario5", base_time.strftime("%d-%m-%Y %H:%M:%S")))
    swift_records.append(make_swift(uumid, None, None, mt, vdate, corr, "freeScenario5", (base_time+timedelta(seconds=12)).strftime("%d-%m-%Y %H:%M:%S")))

    # freeScenario6: Two in PP without SWIFT
    uumid, amt, ccy, mt, vdate, corr, evt_ref = free_common_fields()
    base_time = datetime.now()
    alt_evt_ref = random.choice([f"CR{str(i).zfill(3)}" for i in range(1, 101) if f"CR{str(i).zfill(3)}" != evt_ref])

    pp_records.append(make_pp(uumid, None, None, mt, vdate, corr, evt_ref, "freeScenario6", base_time.strftime("%H:%M:%S")))
    pp_records.append(make_pp(uumid, None, None, mt, vdate, corr, alt_evt_ref, "freeScenario6", (base_time+timedelta(seconds=40)).strftime("%H:%M:%S")))

    # freeScenario7: One in SWIFT only
    uumid, amt, ccy, mt, vdate, corr, evt_ref = free_common_fields()
    base_time = datetime.now()
    swift_records.append(make_swift(uumid, None, None, mt, vdate, corr, "freeScenario7", base_time.strftime("%d-%m-%Y %H:%M:%S")))

    # freeScenario8: Two in SWIFT only
    uumid, amt, ccy, mt, vdate, corr, evt_ref = free_common_fields()
    base_time = datetime.now()
    swift_records.append(make_swift(uumid, None, None, mt, vdate, corr, "freeScenario8", base_time.strftime("%d-%m-%Y %H:%M:%S")))
    swift_records.append(make_swift(uumid, None, None, mt, vdate, corr, "freeScenario8", (base_time+timedelta(seconds=40)).strftime("%d-%m-%Y %H:%M:%S")))

    return pd.DataFrame(swift_records), pd.DataFrame(pp_records)


#
swift_df, pp_df = generate_scenarios()
swift_df.to_excel("swift_scenarios_7.xlsx", index=False)
pp_df.to_excel("pp_scenarios_7.xlsx", index=False)

print("Lucky: Generated SWIFT & PP data with all scenarios.")
