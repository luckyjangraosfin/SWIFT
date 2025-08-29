from swiftBaseClass import swiftBaseClass as sbc
import random
import pandas as pd
from datetime import datetime, timedelta

class many103data(sbc):
    def exposure_details(self):
        uumid, amt, ccy, mt, vdate, corr = super().exposure_details()
        mt=random.choice([keys for keys,values in self.EXPOSURE_MT.items() if values=='GROUP1'])
        return uumid, amt, ccy, mt, vdate, corr
    
    def generate_records(self):
        swift_records, pp_records, cbs_records = [], [], []

        # Happy Case Scenario, Many CBS entry sum(cbsamount)>=swift amount=ppamount(Reconciled Case)
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            amt=int(amt)

            cbs_random_split=random.randint(2,4)

            cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
            cut_points = [0] + cut_points + [amt]
            amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

            for split_amt in amt_split:
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        return pd.DataFrame(cbs_records), pd.DataFrame(swift_records), pd.DataFrame(pp_records)

class many7seriesdata(sbc):
    def exposure_details(self):
        uumid, amt, ccy, mt, vdate, corr = super().exposure_details()  # random.choice(
        mt=[[keys for keys,values in self.EXPOSURE_MT.items() if values==group] for group in set(self.EXPOSURE_MT.values()) if group not in ('GROUP1','GROUP4','GROUP6')]
        
        return uumid, amt, ccy, mt, vdate, corr
    
    def generate_records(self):
        swift_records, pp_records, cbs_records = [], [], []

        # Happy Case Scenario (lower 7XX has amount details, higher 7XX doesn't have amount details)
        for i in range(20):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()
            
            outer_mt_index=random.randint(0,len(mt)-1)
            
            cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 3", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
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
            
            cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Only Higher 7XX present with same amount (Unreconciled Case)
        for i in range(3):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()
            
            outer_mt_index=random.randint(0,len(mt)-1)
            
            cbs_records.append(self.make_cbs(uumid, amt, ccy, vdate, "Scenario 5", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 5", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 5", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        
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
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Only Higher 7XX present with same amount, also CBS has multiple amounts (Unreconciled Case)
        for i in range(3):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()
            
            outer_mt_index=random.randint(0,len(mt)-1)
            amt=int(amt)

            cbs_random_split=random.randint(2,3)

            cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
            cut_points = [0] + cut_points + [amt]
            amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

            for split_amt in amt_split:
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 7", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 7", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 7", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Only Lower 7XX present with same amount, CBS not present (Unreconciled Case)
        for i in range(3):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()
            
            outer_mt_index=random.randint(0,len(mt)-1)
            
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP not present, CBS not present, Swift single Lower 7XX
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 12", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))   
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][0], vdate, corr, "Scenario 12", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP not present, CBS single entry/multiple entry, Swift single Higher 7XX
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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP not present, CBS not present, Swift single Higher 7XX
        for i in range(5):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details()

            outer_mt_index=random.randint(0,len(mt)-1)

            pp_records.append(self.make_pp(uumid, amt, ccy, mt[outer_mt_index][0], vdate, corr, "Scenario 12", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))   
            swift_records.append(self.make_swift(uumid, None, None, mt[outer_mt_index][1], vdate, corr, "Scenario 12", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        

        return pd.DataFrame(cbs_records), pd.DataFrame(swift_records), pd.DataFrame(pp_records)
    

if __name__ == "__main__":
    happygenerator = sbc()
    many103generator = many103data()
    many7XXgenerator = many7seriesdata()

    cbs_df1, swift_df1, pp_df1 = happygenerator.generate_records()
    cbs_df2, swift_df2, pp_df2 = many103generator.generate_records()
    cbs_df3, swift_df3, pp_df3 = many7XXgenerator.generate_records()

    cbs_df = pd.concat([cbs_df1, cbs_df2, cbs_df3], ignore_index=True)
    swift_df = pd.concat([swift_df1, swift_df2, swift_df3], ignore_index=True)
    pp_df = pd.concat([pp_df1, pp_df2, pp_df3], ignore_index=True)

    cbs_file_name, swift_file_name, pp_file_name = happygenerator.generate_file_names()

    cbs_df.to_csv(cbs_file_name, index=False, sep="|")
    pp_df.to_csv(pp_file_name, index=False, sep="|")
    swift_df.to_excel(swift_file_name, index=False)

    print("Files generated successfully:", cbs_file_name, swift_file_name, pp_file_name)