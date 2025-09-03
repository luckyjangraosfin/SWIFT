from swiftBaseClass import swiftBaseClass as sbc
import random
import pandas as pd
from datetime import datetime

class obtc202data(sbc):
    def exposure_details(self):
        uumid, amt, ccy, mt, vdate, corr = super().exposure_details()

        mt=random.choice(['202'])
        uumid = self.random_string("UUM", 25) 
        uumid = uumid = uumid[:15] + "OBTC" + uumid[19:]      
        return uumid, amt, ccy, mt, vdate, corr
    
    def generate_records(self):
        swift_records, pp_records, cbs_records, cbs_lim_records = [], [], [], []

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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 1", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))


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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 2", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 3", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 3", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 3", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 3", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))


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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time/Money
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 4", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 5", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 5", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 5", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 5", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time/Money
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 5", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter Time
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 6", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 7", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 7", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 7", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 7", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter Time
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 7", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

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
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter time
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter Time
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 8", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        
        # Swift 1 entry, PP 1 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 9", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 9", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 9", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift no entry, PP 1 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 

            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 10", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
 
            
        # Swift 1 entry, PP no entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 11", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift 1 entry, PP 2 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 

            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 12", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 12", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # adjust time
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 12", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 12", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift no entry, PP 2 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 

            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 13", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 13", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # adjust time
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 13", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 13", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift 2 entry, PP 1 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 14", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 14", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 14", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 14", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift 2 entry, PP no entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 15", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 15", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 15", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift 2 entry, PP 2 entry, No CBS entries
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 16", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 16", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 16", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 16", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # adjust time
            cbs_lim_records.append(self.make_cbs_lim(uumid, amt, ccy, vdate, "Scenario 16", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))



        # happy , Many/one CBS entry sum(cbsamount)>=swift amount=ppamount , not present in cbs_lim (unreconciled)
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 17", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 17", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 17", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 17", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))


        # Swift Not present, Many/one CBS entry, cbs_lim not present
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 18", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 18", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 18", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP Not present, Many/one CBS entry, Swift Present, cbs_lim not present
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 19", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 19", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 19", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))


        # PP 2 entries, Swift 1 entry, CBS 1/many entry, cbs_lim not present
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 20", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 20", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 20", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 20", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time/Money
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 20", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # PP 2 entries, Swift Not present, Many/one CBS entry, cbs_lim not present
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 21", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 21", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 21", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 21", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time/Money

        # Swift 2 entry, PP 1 entry, CBS 1/many entry, cbs_lim not present
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 22", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 22", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 22", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 22", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 22", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter Time

        # Swift 2 entry, PP no entry, CBS 1/many entry, cbs_lim not present
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 23", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 23", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 23", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 23", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter Time

        # Swift 2 entry, PP 2 entry, CBS 1/many entry, cbs_lim not present 
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            cbs_random_split=random.randint(1,3)

            if cbs_random_split!=1:
                amt=int(amt)

                cut_points = sorted(random.sample(range(1, amt), cbs_random_split - 1))
                cut_points = [0] + cut_points + [amt]
                amt_split = [cut_points[i+1] - cut_points[i] for i in range(len(cut_points)-1)]

                for split_amt in amt_split:
                    cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 24", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            
            else :
                cbs_records.append(self.make_cbs(uumid, split_amt, ccy, vdate, "Scenario 24", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 24", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 24", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter time
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 24", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 24", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # Alter Time

        
        # Swift 1 entry, PP 1 entry, No CBS entries, cbs_lim not present 
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 25", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 25", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift no entry, PP 1 entry, No CBS entries, cbs_lim not present 
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 

            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 26", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
 
            
        # Swift 1 entry, PP no entry, No CBS entries, cbs_lim not present 
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 27", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift 1 entry, PP 2 entry, No CBS entries, cbs_lim not present 
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 

            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 28", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 28", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # adjust time
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 28", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift no entry, PP 2 entry, No CBS entries, cbs_lim not present 
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 

            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 29", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 29", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # adjust time
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 29", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

        # Swift 2 entry, PP 1 entry, No CBS entries, cbs_lim not present 
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 30", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 30", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 30", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 

        # Swift 2 entry, PP no entry, No CBS entries, cbs_lim not present 
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 31", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 31", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time

        # Swift 2 entry, PP 2 entry, No CBS entries, cbs_lim not present 
        for i in range(10):
            uumid, amt, ccy, mt, vdate, corr = self.exposure_details() 
            
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 32", datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            swift_records.append(self.make_swift(uumid, amt, ccy, mt, vdate, corr, "Scenario 32", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) #Adjust Time
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 32", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) 
            pp_records.append(self.make_pp(uumid, amt, ccy, mt, vdate, corr, "Scenario 32", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))) # adjust time



        return pd.DataFrame(cbs_records), pd.DataFrame(swift_records), pd.DataFrame(pp_records), pd.DataFrame(cbs_lim_records)