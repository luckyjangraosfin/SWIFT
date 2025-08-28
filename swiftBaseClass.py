import random
import string
import uuid
from datetime import datetime, timedelta
import pandas as pd
from MTtypes import MTtypes as mt


class swiftBaseClass:

    EXPOSURE_MT,FREE_TEXT_MT,NON_EXPOSURE_MT=mt.get_mt()

    @staticmethod
    def random_string(prefix="", length=8):
        return prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    @staticmethod
    def random_bool():
        return random.choice([True, False])

    @staticmethod
    def random_date(start, end, with_time=False):
        dt = start + timedelta(days=random.randint(0, (end - start).days))
        return dt.strftime("%d-%m-%Y") if not with_time else dt.strftime("%d-%m-%Y %H:%M:%S")


    def make_swift(self, uumid, amt, ccy, mt, vdate, corr, scenario="", creation_time=None):
        return {
            "Scenario": scenario,
            "ValidationRequested": random.choice(["MAXIMUM", "MINIMUM"]),
            "ValidationPassed": random.choice(["MAXIMUM", "MINIMUM"]),
            "Class": random.choice(["NORMAL"]),
            "TextReadonly": self.random_bool(),
            "DeleteInhibited": self.random_bool(),
            "TextModified": self.random_bool(),
            "Partial": self.random_bool(),
            "Status": random.choice(["LIVE", "COMPLETED"]),
            "CreationApplication": self.random_string("APP"),
            "CreationMpfnName": self.random_string("MPFN"),
            "CreationRoutingPoint": self.random_string("RTP"),
            "CreationOperator": random.choice(["SYSTEM"]),
            "CreationDate": creation_time if creation_time else datetime.today().strftime("%d-%m-%Y %H:%M:%S"),
            "ModificationOperator": self.random_string("MOP"),
            "ModificationDate": self.random_date(datetime(2023,1,1), datetime(2025,12,31)),
            "Uumid": uumid,
            "UumidSuffix": random.randint(1,9),
            "SenderCorrespondentType": random.choice(["Bank", "Broker", "Other"]),
            "SenderCorrespondentInstitutionName": random.choice(["HDFC", "SBI", "CITI"]),
            "FormatName": random.choice(["MX", "Swift"]),
            "SubFormat": random.choice(["INPUT", "OUTPUT"]),
            "SyntaxTableVersion": random.randint(1,5),
            "Nature": random.choice(["PAY","MSG","ENQ"]),
            "NetworkApplicationIndication": self.random_string("NAI"),
            "Type": mt,
            "Live": self.random_bool(),
            "NetworkPriority": random.choice(["HIGH","NORM","LOW"]),
            "DeliveryOverdueWarningRequired": self.random_bool(),
            "NetworkDeliveryNotificationRequired": self.random_bool(),
            "UserReferenceText": self.random_string("URT"),
            "FinValueDate": vdate,
            "FinCurrencyAmount": f"{ccy}{amt:.2f}" if amt else None,
            "TransactionReference": self.random_string("TRX"),
            "RelatedTransactionReference": self.random_string("RTR"),
            "PossibleDuplicate": self.random_bool(),
            "MessageIdentifier": str(uuid.uuid4()),
            "SenderSwiftAddress": self.random_string("SND"),
            "ReceiverSwiftAddress": self.random_string("RCV"),
            "Service": self.random_string("SRV"),
            "ExpiryDateTime": self.random_date(datetime(2023,1,1), datetime(2025,12,31), with_time=True),
            "HasVerifiableField": self.random_bool(),
            "TransactionNumber": random.randint(10000,99999),
            "SecondarySenderCorrespondentInstitutionName": self.random_string("SEC"),
            "SenderCorrespondentDepartment": self.random_string("DEP"),
            "MessageUserGroup": self.random_string("MUG"),
            "RequestorDn": self.random_string("REQ"),
            "RequestType": random.choice(["TYPEA","TYPEB"]),
            "RequestSubtype": random.choice(["SUB1","SUB2"]),
            "XmlQueryReference1": self.random_string("XQ1"),
            "XmlQueryReference3": self.random_string("XQ3"),
            "PayloadType": random.choice(["XML","JSON"]),
            "PayloadAttributeName": self.random_string("PAN"),
            "PayloadAttributeValue": self.random_string("PAV"),
            "ServiceUri": self.random_string("URI"),
            "MessageTypeUri": self.random_string("MTU"),
            "MessageTypeUploadId": str(uuid.uuid4()),
            "ServiceLevelAgreement": self.random_string("SLA"),
            "E2ETransactionReference": self.random_string("E2E"),
            "SecondaryFormatName": self.random_string("SFN"),
            "MessageSecondaryIdentifier": self.random_string("MSI"),
            "SecondaryService": self.random_string("SSRV"),
            "SecondarySyntaxTableVersion": random.randint(1,5),
            "MessageSecondaryType": self.random_string("MST"),
            "TranlationResult": self.random_string("TRS"),
            "SecondaryUumid": self.random_string("SUU"),
            "HeaderIdentifier": self.random_string("HDR"),
            "TransactionManagerResult": self.random_string("TMR"),
            "CasSenderReference": self.random_string("CSR"),
            "RecoveryAcceptInfo": self.random_string("RAI"),
            "UserIssuedAsPde": self.random_bool(),
            "MessageSecondaryUserGroup": self.random_string("MSUG"),
            "CasTargetRoutingPoint": self.random_string("CTRP"),
            "ApplicationSenderReference": self.random_string("ASR"),
            "RequiredSignatureNRS": self.random_bool(),
            "SimplifiedScreen": self.random_bool()
        }

    def make_pp(self, uumid, amt, ccy, mt, vdate, corr, scenario="", creation_time=None):
        return {
            "Scenario": scenario,
            "MTTYPE": "MT" + mt,
            "CORRESPONSDENT": corr,
            "VALUE DATE": datetime.strptime(vdate, "%y%m%d").strftime("%d-%m-%Y"),
            "CCY": ccy,
            "AMOUNT": amt,
            "REFERENCE NUMBER": uumid[15:35],
            "EVENT REFERENCE": self.random_string("EVT"),
            "UNIQUE ID": str(uuid.uuid4())[:12],
            "CREATION DATE": datetime.today().strftime("%d-%m-%Y"),
            "CREATION TIME": creation_time if creation_time else datetime.today().strftime("%H:%M:%S"),
        }

    def make_cbs(self, uumid, amt, ccy, vdate, scenario="", creation_time=None):
        return {
            "SCENARIO": scenario,
            "AUTH_DATE": vdate,
            "VALUE_DATE": vdate,
            "ACCOUNT_NUMBER": random.randint(10**11, 999999999999),
            "CBS_CCY": ccy,
            "CBS_AMOUNT": amt,
            "REFERENCE_NUMBER": uumid[15:35],
            "CREATION_DATE": datetime.today().strftime("%d-%m-%Y"),
            "CREATION_TIME": creation_time if creation_time else datetime.today().strftime("%H:%M:%S")
        }

    def generate_records(self):
        swift_records, pp_records, cbs_records = [], [], []

        def exposure_details():
            mt = random.choice(list(self.EXPOSURE_MT.keys()))
            ccy = random.choice(["USD", "EUR", "INR", "GBP"])
            amt = round(random.uniform(1000, 9999), 2)
            vdate = datetime.today().strftime("%y%m%d")
            uumid = self.random_string("UUM", 25)
            corr = uumid[1:9] + uumid[8:11]
            return uumid, amt, ccy, mt, vdate, corr

        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = exposure_details()
            cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        return pd.DataFrame(cbs_records), pd.DataFrame(swift_records), pd.DataFrame(pp_records)

    def generate_file_names(self):
        cbs_file_name = "3WAY_TRADE_CBS_GL_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        swift_file_name = "SWIFT_GL_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx"
        pp_file_name = "2WAY_PRODUCT_PROCESSOR_GL_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
        return cbs_file_name, swift_file_name, pp_file_name