# step by step guide
1. open it in wireshark and see that leftover "Leftover Capture data" changes between packages.
2. same thing could also have been seen with:
    ```
    tshark -V -r data.pcap
    ```
3. either solve it the hard way (solution.py) via parsing the raw data or
4. parse it with tshark. To know what field that "Leftover Capture data" is:
    ```
    tshark -G fields | grep "Leftover Capture data"
    ```
    gets us "usb.capturedata"

5. lets read them but ignore the empty ones:
    ```
    tshark -T fields -e usb.capdata -r data.pcap | cut -d ':' -f 3 | grep -v 00
    ```
6. now it is again time to translate those values into letters. For that we need to take a look at the doc under Keyboard/Keypad page: http://www.usb.org/developers/hidpage/Hut1_12v2.pdf

# credits
the solution with tshark is from:
https://github.com/LFlare/picoctf_2017_writeup/tree/master/forensics/just-keyp-trying
