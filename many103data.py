from swiftBaseClass import swiftBaseClass as sbc
import random
import pandas as pd
from datetime import datetime

class many103data(sbc):
    def exposure_details(self):
        uumid, amt, ccy, mt, vdate, corr = super().exposure_details()
        mt=random.choice([keys for keys,values in self.EXPOSURE_MT.items() if values=='GROUP1'])
        return uumid, amt, ccy, mt, vdate, corr
    
    def generate_records(self):
        swift_records, pp_records, cbs_records = [], [], []

        # Happy Case Scenario, Many/one CBS entry sum(cbsamount)>=swift amount=ppamount(Reconciled Case)
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift Not present, Many/one CBS entry
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP Not present, Many/one CBS entry, Swift Present
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP 2 entries, Swift 1 entry, CBS 1/many entry
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time/Money
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP 2 entries, Swift Not present, Many/one CBS entry
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time/Money

        # Swift 2 entry, PP 1 entry, CBS 1/many entry
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter Time

        # Swift 2 entry, PP no entry, CBS 1/many entry
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter Time

        # Swift 2 entry, PP 2 entry, CBS 1/many entry
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter time
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter Time

        
        # Swift 1 entry, PP 1 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift no entry, PP 1 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 

            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            
        # Swift 1 entry, PP no entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift 1 entry, PP 2 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 

            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # adjust time
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift no entry, PP 2 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 

            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # adjust time
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        
        # Swift 2 entry, PP 1 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 

        # Swift 2 entry, PP no entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time

        # Swift 2 entry, PP 2 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # adjust time


        return pd.DataFrame(cbs_records), pd.DataFrame(swift_records), pd.DataFrame(pp_records)