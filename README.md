# Otopeni (OTP/LROP) airport timetable scraper
Scrapes the departure and arrival board from Otopeni's website.

## Installation
`pipenv install` and off you go.

## Usage
You can either use the scraper.py file as a library or modify the main.py file
to your liking. Please not that this project is a proof-of-concept made at 4AM
on a sleepless night so quality is not ensured.

This script provides the following information, if available:
- Airline name
- Airline logo (big and small)
- Commercial flight number
- Destination/Origin airport (and IATA code)
- Estimated time
- Actual time
- Flight status (i.e. in flight, landed, shot down by terrorists etc.) 

## Example

Output from running `pipenv run python main.py`:

    ARRIVALS:
    W63136 - Scheduled 00:15, estimated 00:08 from BGY (BERGAMO) - Landed
    0B2924 - Scheduled 00:30, estimated 00:21 from BRU (BRUSSELS) - Landed
    LH1422 - Scheduled 00:35, estimated 00:32 from FRA (FRANKFURT) - Landed
    KL1379 - Scheduled 00:35, estimated 00:28 from AMS (AMSTERDAM) - Landed
    RO9362 - Scheduled 00:35, estimated 00:28 from AMS (AMSTERDAM) - Landed
    W63036 - Scheduled 00:55, estimated 00:43 from SEN (LONDON) - Landed
    W63216 - Scheduled 01:15, estimated 01:03 from TRF (OSLO) - Landed
    W63176 - Scheduled 01:20, estimated 01:17 from BCN (BARCELONA) - Landed
    W63020 - Scheduled 02:00, estimated 02:06 from BHX (BIRMINGHAM) - Landed
    0B138 - Scheduled 02:00, estimated 01:33 from LCA (LARNACA) - Landed
    0B9542 - Scheduled 02:30, estimated 01:47 from CRA (CRAIOVA) - Landed
    W63022 - Scheduled 02:35, estimated 02:24 from TFS (TENERIFE SOUTH) - Landed
    W63006 - Scheduled 02:55, estimated 02:37 from LTN (LONDON) - Landed
    W63016 - Scheduled 02:55, estimated 02:47 from DSA (SHEFFELD) - Landed
    0B1014 - Scheduled 06:35, estimated 06:35 from VLC (VALENCIA) - Estimated
    0B134 - Scheduled 07:00, estimated 06:51 from LPL (LIVERPOOL) - Estimated
    TK1043 - Scheduled 08:30, estimated 08:30 from IST (ISTANBUL) - Estimated
    FR3992 - Scheduled 09:05, estimated 09:05 from BGY (BERGAMO) - Estimated
    (...)
    
    DEPARTURES:
    BUR205P - Scheduled 05:15, estimated 05:15 from SBZ (SIBIU) - Estimated
    LH1423 - Scheduled 06:10, estimated 06:10 from FRA (FRANKFURT) - Estimated
    W63051 - Scheduled 06:10, estimated 06:10 from BVA (BEAUVAIS) - Estimated
    W63093 - Scheduled 06:20, estimated 06:20 from DTM (DORTMUND) - Estimated
    W63099 - Scheduled 06:30, estimated 06:30 from FMM (MEMMINGEN) - Estimated
    W63001 - Scheduled 06:40, estimated 06:40 from LTN (LONDON) - Estimated
    AWG2001 - Scheduled 06:45, estimated 06:45 from AYT (ANTALYA) - Estimated
    FR1006 - Scheduled 06:50, estimated 06:50 from STN (LONDON) - Estimated
    RO601 - Scheduled 06:55, estimated 06:55 from TSR (TIMISOARA) - Estimated
    KL2726 - Scheduled 06:55, estimated 06:55 from TSR (TIMISOARA) - Estimated
    KL1372 - Scheduled 07:00, estimated 07:00 from AMS (AMSTERDAM) - Estimated
    (...)
    
 ## Disclaimer
 The script might break at any time so if it does, let me know - or even better, 
 make a pull request.