from swiftBaseClass import swiftBaseClass as sbc

if __name__ == "__main__":
    generator = sbc()

    cbs_df, swift_df, pp_df = generator.generate_records()
    cbs_file_name, swift_file_name, pp_file_name = generator.generate_file_names()

    cbs_df.to_csv(cbs_file_name, index=False, sep="|")
    pp_df.to_csv(pp_file_name, index=False, sep="|")
    swift_df.to_excel(swift_file_name, index=False)

    print("Files generated successfully:", cbs_file_name, swift_file_name, pp_file_name)