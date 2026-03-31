nongdu=8.7
hour=0
while nongdu>0.1:
    nongdu=nongdu*0.5
    hour=hour+5
print("After {} hours, drug concentration is {:0.2f}".format(hour,nongdu))