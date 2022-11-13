import requests
import numpy as np
import time
import matplotlib.pyplot as plt
import sys


def getRadioFFT(station, session, buffer_size, num_bars, refresh_time):
    # with requests.get("http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one", stream=True) as r:
    start = time.time()
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    data = []
    with session.get(station, stream=True, headers=headers, timeout=refresh_time/2) as r:
        r.raw.chunked = True
        data = []
        for i, chunk in enumerate(r.iter_content(buffer_size)):
            data = [k for k in chunk]
            print(chunk)
            # if chunk:
            #     data += list(chunk)
            break
            # if i == 1:
            #     break

        # with open('stream.mp3', 'wb') as f:
        #     try:
        #         for l, chunk in enumerate(r.iter_content(1024)):
        #             # sample += chunk
        #             if not chunk:
        #                 break
        #
        #             f.write(chunk)
        #             f.flush()
        #             if l==30:
        #                 break
        #     except KeyboardInterrupt:
        #         pass

        # try:
        #     data = np.array(np.frombuffer(sample, dtype = np.float64))
        # except ValueError:
        #     print(sample, np.array(np.frombuffer(sample, "float32")))
        #     pass
        data = np.array(data)
        # print(len(data))
        data[np.isnan(data)] = 0

        data = data/max(data)
        window = signal.windows.get_window("hann", len(data))
        fft = np.fft.fftshift(np.fft.fft(data*window))[len(data)//2:]
        fftfreq = np.fft.fftshift(np.fft.fftfreq(len(data)))[len(data)//2:]
        fft_hist, fft_bins = np.histogram(np.abs(fft), bins=np.logspace(min(fftfreq), max(fftfreq), num_bars))
        end = time.time()
        print(f"loop = {end-start}")
        return fft_hist/buffer_size

def getFakeRadioFFT(num_bars):
    fakex = np.arange(1, num_bars+1)
    fakey = ((1/fakex)#*(1+np.random.random(num_bars)*0.2)
            + np.random.random(num_bars)*0.1
            + 0.1*np.random.normal(np.random.random(), 5*np.random.random(), num_bars))
    # window = signal.windows.get_window("hann", len(fakey))
    # fft = np.fft.fftshift(np.fft.fft(fakey*window))[len(fakey)//2:]
    # fftfreq = np.fft.fftshift(np.fft.fftfreq(len(fakey)))[len(fakey)//2:]
    # fft_hist, fft_bins = np.histogram(np.abs(fft), bins=np.logspace(min(fftfreq), max(fftfreq), num_bars))
    return np.array(fakey)



# j = 0
# num_loops = 5
# num_chunks = 1
# num_bars = 22
# buffer_size = 2048
#
# while j < num_loops:
#     start = time.time()
#     # fft_hist= getRadioFFT("http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one", 1, buffer_size, num_bars, 1)
#     fft_hist = getFakeRadioFFT(num_bars)
#     print(fft_hist)
#     # print(data, len(data))
#     # print(np.abs(fft), sum(np.abs(fft)))
#     #
#     plt.figure()
#     # plt.plot(np.arange(len(data)), data)
#
#     plt.bar(np.arange(len(fft_hist)), fft_hist[::-1], width=0.8, align="center", edgecolor="black")
#     # plt.yscale("log")
#     # plt.xscale("log")
#     plt.savefig(f"audiotest\\bar_{str(j)}.png", dpi=600)
#
#     # plt.figure()
#     # # plt.plot(np.arange(len(data)), data)
#     #
#     # plt.plot(fftfreq, np.abs(fft))
#     # plt.yscale("log")
#     # plt.xscale("log")
#     # plt.savefig(f"audiotest\\audiotest_{str(j)}.png", dpi=600)
#     end = time.time()
#     print(f"loop time = {end-start}s")
#     time.sleep(1)
#     j+=1

#
# with open('stream.mp3', 'wb') as f:
#     try:
#         # for block in r.iter_content(1024):
#         #     f.write(block)
#         f.write(list(r.iter_content())[0])
#     except KeyboardInterrupt:
#         pass
