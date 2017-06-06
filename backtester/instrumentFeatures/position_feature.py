from instrument_feature import InstrumentFeature


class PositionFeature(InstrumentFeature):

    @classmethod
    def validateInputs(cls, featureParams, currentFeatures, instrument):
        return True

    @classmethod
    def compute(cls, featureParams, currentFeatures, instrument):
        bookData = instrument.getCurrentBookData()
        instrumentType = instrument.getInstrumentType()
        return instrument.getCurrentPosition()
