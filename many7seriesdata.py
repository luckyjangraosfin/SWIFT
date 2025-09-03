from swiftBaseClass import swiftBaseClass as sbc
import random
import pandas as pd
from datetime import datetime

class many7seriesdata(sbc):
    def exposure_details(self):
        uumid, amt, ccy, mt, vdate, corr = super().exposure_details()  # random.choice(
        mt=[[keys for keys,values in self.EXPOSURE_MT.items() if values==group] for group in set(self.EXPOSURE_MT.values()) if group not in ('GROUP1','GROUP4','GROUP6')]
        
        return uumid, amt, ccy, mt, vdate, corr
    
    def generate_records(self):
        swift_records, pp_records, cbs_lim_records = [], [], []

        # Happy Case Scenario (lower 7XX has amount details, higher 7XX doesn't have amount details)
        for i in range(20):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()
            
            outer_mt_index=random.randint(0,len(mt)-1)
            
            cbs_lim_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 3", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 3", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 3", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 3", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Unhappy Case Scenario (lower 7XX has amount details, higher 7XX doesn't have amount details, CBS not present) (Unreconciled Case)
        for i in range(2):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()
            
            outer_mt_index=random.randint(0,len(mt)-1)
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 9", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 9", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 9", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Only Lower 7XX present with same amount (Reconciled Case)
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()
            
            outer_mt_index=random.randint(0,len(mt)-1)
            
            cbs_lim_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))


        # Only Lower 7XX present with same amount, also CBS has multiple amounts (sum of CBS amount>=swiftamount) (Reconciled Case)
        for i in range(15):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()
            
            outer_mt_index=random.randint(0,len(mt)-1)
            amt=int(amt)

            cbs_random_split=random.randint(2,3)

            cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
            cut_points = [0] + cut_points + [amt]
            amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

            for split_amt in amt_split:
                cbs_lim_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Only Lower 7XX present with same amount, CBS not present (Unreconciled Case)
        for i in range(3):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()
            
            outer_mt_index=random.randint(0,len(mt)-1)
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift not present, CBS single entry/multiple entry
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_lim_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_lim_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP not present, CBS single entry/multiple entry, Swift single Lower 7XX
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_lim_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_lim_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP not present, CBS not present, Swift single Lower 7XX
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 12", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))


        # PP not present, CBS single entry/multiple entry, Swift both 7XX
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_lim_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 13", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_lim_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 13", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 13", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 13", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP not present, CBS not present, Swift both 7XX
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 15", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 15", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift not present, CBS single entry/multiple entry, PP 2 entry
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_lim_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 16", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_lim_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 16", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 16", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 16", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Handle Time

        # Swift single lower 7XX present, CBS single entry/multiple entry, PP 2 entry
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_lim_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 17", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_lim_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 17", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 17", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 17", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 17", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Handle Time

        # Swift both 7XX present, CBS single entry/multiple entry, PP 2 entry
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_lim_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 18", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_lim_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 18", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 18", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 18", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 18", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 18", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Handle Time

        # Swift not present, CBS not present, PP 2 entry
        for i in range(3):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 19", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 19", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Handle Time

        # Swift not present, CBS not present, PP 1 entry
        for i in range(3):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 19", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        
        # Swift lower 7XX present, CBS not present, PP 2 entry
        for i in range(3):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 20", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 20", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 20", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Handle Time

        # Swift both 7XX present, CBS not present, PP 2 entry
        for i in range(3):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 21", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 21", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 21", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 21", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Handle Time
        
        


        return pd.DataFrame(cbs_lim_records), pd.DataFrame(swift_records), pd.DataFrame(pp_records)