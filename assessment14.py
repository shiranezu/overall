def KelvinToFarenheit(temperature):
    assert temperature >= 0, "hmm,too cold"
    print((temperature-273.15)*9/5+32)
KelvinToFarenheit(43)