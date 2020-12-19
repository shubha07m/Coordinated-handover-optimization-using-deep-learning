import numpy as np
import pandas as pd

# data frame preparation #
data = pd.read_csv('finaldata_new.csv')
df = pd.DataFrame(data)

# continuous comparison #
# print(df['Upload (Tx) bandwidth (bps)_1'][4000])

if (df['User_type'][4000]) == 1:
    for i in range(4000, 5000, 10):
        # print(df['Download (Rx) bandwidth (bps)_1'][i])
        x1 = (np.mean(df['Download (Rx) bandwidth (bps)_1'][i:i + 10] + df['Upload (Tx) bandwidth (bps)_1'][i:i + 10]))
        y1 = (np.mean(df['Download (Rx) bandwidth (bps)_2'][i:i + 10] + df['Upload (Tx) bandwidth (bps)_2'][i:i + 10]))
        z1 = (np.mean(df['Download (Rx) bandwidth (bps)_3'][i:i + 10] + df['Upload (Tx) bandwidth (bps)_3'][i:i + 10]))
        x2 = (np.mean(
            df['Download (Rx) bandwidth (bps)_1'][i + 10:i + 20] + df['Upload (Tx) bandwidth (bps)_1'][i + 10:i + 20]))
        y2 = (np.mean(
            df['Download (Rx) bandwidth (bps)_2'][i + 10:i + 20] + df['Upload (Tx) bandwidth (bps)_2'][i + 10:i + 20]))
        z2 = (np.mean(
            df['Download (Rx) bandwidth (bps)_3'][i + 10:i + 20] + df['Upload (Tx) bandwidth (bps)_3'][i + 10:i + 20]))

        if (((x1 - x2) / x1) * 100) > 10:
            throughput = [x2, y2, z2]
        else:
            throughput = [x1, y1, z1]
        # print(throughput.index(max(throughput)) + 1)

        for j in range(10):
            if j == 0:
                print(throughput.index(min(throughput)) + 1)
            else:
                print('')
if (df['User_type'][4000]) == 2:
    for i in range(4000, 5000, 10):
        # print(df['Download (Rx) bandwidth (bps)_1'][i+20])
        x1 = (np.mean(df['RTT (ping) (ms)_1'][i:i + 10]))
        y1 = (np.mean(df['RTT (ping) (ms)_2'][i:i + 10]))
        z1 = (np.mean(df['RTT (ping) (ms)_3'][i:i + 10]))

        x2 = (np.mean(df['RTT (ping) (ms)_1'][i + 10:i + 20]))
        y2 = (np.mean(df['RTT (ping) (ms)_2'][i + 10:i + 20]))
        z2 = (np.mean(df['RTT (ping) (ms)_3'][i + 10:i + 20]))

        if (((x2 - x1) / x1) * 100) > 10:
            latency = [x2, y2, z2]
        else:
            latency = [x1, y1, z1]
        for j in range(10):
            if j == 0:
                print(latency.index(min(latency)) + 1)
            else:
                print('')
        # print(min(latency))
if (df['User_type'][4000]) == 3:
    for i in range(4000, 5000, 10):
        # print(df['Download (Rx) bandwidth (bps)_1'][i])
        x1 = (np.mean(df['Rx packet loss (percent)_1'][i:i + 10] + df['Tx packet loss (percent)_1'][i:i + 10]))
        y1 = (np.mean(df['Rx packet loss (percent)_2'][i:i + 10] + df['Tx packet loss (percent)_2'][i:i + 10]))
        z1 = (np.mean(df['Rx packet loss (percent)_3'][i:i + 10] + df['Tx packet loss (percent)_3'][i:i + 10]))

        x2 = (
            np.mean(df['Rx packet loss (percent)_1'][i + 10:i + 20] + df['Tx packet loss (percent)_1'][i + 10:i + 20]))
        y2 = (
            np.mean(df['Rx packet loss (percent)_2'][i + 10:i + 20] + df['Tx packet loss (percent)_2'][i + 10:i + 20]))
        z2 = (
            np.mean(df['Rx packet loss (percent)_3'][i + 10:i + 20] + df['Tx packet loss (percent)_3'][i + 10:i + 20]))

        if (((x2 - x1) / x1) * 100) > 10:
            packetloss = [x2, y2, z2]
        else:
            packetloss = [x1, y1, z1]
        # print(packetloss.index(min(packetloss)) + 1)

        for j in range(10):
            if j == 0:
                print(packetloss.index(min(packetloss)) + 1)
            else:
                print('')
