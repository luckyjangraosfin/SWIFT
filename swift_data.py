from many103data import many103data
from many7seriesdata import many7seriesdata
from swiftBaseClass import swiftBaseClass as sbc
import pandas as pd

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