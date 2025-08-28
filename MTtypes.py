class MTtypes:
    EXPOSURE_MT = {
        '103': 'GROUP1', '110': 'GROUP8', '202': 'GROUP9', '008': 'GROUP9',
        '009': 'GROUP9', '700': 'GROUP2', '701': 'GROUP2', '707': 'GROUP3',
        '708': 'GROUP3', '759': 'GROUP4', '760': 'GROUP5', '761': 'GROUP5',
        '765': 'GROUP6', '767': 'GROUP7', '775': 'GROUP7'
    }
    FREE_TEXT_MT = {'199','299','799','999'}

    @classmethod
    def get_mt(cls):
        return cls.EXPOSURE_MT,cls.FREE_TEXT_MT,[
            str(i) for i in range(100, 800)
            if str(i) not in cls.EXPOSURE_MT and str(i) not in cls.FREE_TEXT_MT
        ]