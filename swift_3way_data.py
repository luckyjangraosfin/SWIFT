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
        return super().exposure_details()

if __name__ == "__main__":
    happygenerator = sbc()
    many103generator = many103data()

    cbs_df1, swift_df1, pp_df1 = happygenerator.generate_records()
    cbs_df2, swift_df2, pp_df2 = many103generator.generate_records()

    cbs_df = pd.concat([cbs_df1, cbs_df2], ignore_index=True)
    swift_df = pd.concat([swift_df1, swift_df2], ignore_index=True)
    pp_df = pd.concat([pp_df1, pp_df2], ignore_index=True)

    cbs_file_name, swift_file_name, pp_file_name = happygenerator.generate_file_names()

    cbs_df.to_csv(cbs_file_name, index=False, sep="|")
    pp_df.to_csv(pp_file_name, index=False, sep="|")
    swift_df.to_excel(swift_file_name, index=False)

    print("Files generated successfully:", cbs_file_name, swift_file_name, pp_file_name)