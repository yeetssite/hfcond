# What is this?
HFcond is actually a langauge parser of sorts... No, I don't know what language it parses(I have a less-than-average understanding of things(I'm stupid)), but it takes something that looks like this:

```
:Product: Geophysical Alert Message wwv.txt
:Issued: 2025 Mar 14 1205 UTC
# Prepared by the US Dept. of Commerce, NOAA, Space Weather Prediction Center
#
#          Geophysical Alert Message
#
Solar-terrestrial indices for 13 March follow.
Solar flux 175 and estimated planetary A-index 42.
The estimated planetary K-index at 1200 UTC on 14 March was 3.00.

Space weather for the past 24 hours has been moderate.
Geomagnetic storms reaching the G2 level occurred.

Space weather for the next 24 hours is predicted to be minor.
Geomagnetic storms reaching the G1 level are expected.
```

And uses it to spit this out:

```
Current time(UTC+00:00): 14:40:05
Geophysical Alert Message wwv.txt
Issued: 2025 Mar 14 1205 UTC
———————————————————————————————————————————————————
Solar-terrestrial indices for 13 March follow.
Solar flux 175 and estimated planetary A-index 42.
The estimated planetary K-index at 1200 UTC on 14 March was 3.00.

Space weather for the past 24 hours has been moderate.
Geomagnetic storms reaching the G2 level occurred.

Space weather for the next 24 hours is predicted to be minor.
Geomagnetic storms reaching the G1 level are expected.
```

# Ok, but like, what is it showing me?

HFcond was originally created to show a nice, fancy version of [NOAA's wwv.txt](https://www.swpc.noaa.gov/products/geophysical-alert-wwv-text) for quick and easy knowledge about how good you can receive/transmit radio. This is it's main purpose, but it's later versions can show other things, such as [the forecast discussion](https://www.swpc.noaa.gov/products/forecast-discussion), or [the what's new page](https://yeetssite.github.io/shortwave/hfc-whatsnew.txt).

You can bring up a list of options and flags using the `--help` option:

```shell
~$ hfcond --help
```

`OPTION`s and `FLAG`s are different. You can only pick one `OPTION`, and it *has* to come *before* any `FLAG`s, or else it won't work.

For info about the `Binary/` folder, see README.txt. 
