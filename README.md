# movorg

## TODOs and Enhancements
- [ ] make script idempotent
- [ ] describe usage and parameters

## Prerequisites

### Packages
- In order for the script to work the following linux packages need to be installed on the host running the script.
  - `tree`

### Installation
- No Installation is needed in order to execute the script

## Regex

### Nima4k
`^(\w+(\.\w+)*)\.([0-9]{4})(?!p)`
  - **Test Strings**
    ```
    Resident.Evil.The.Final.Chapter.2016.German.Dubbed.DTSHD.DL.2160p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    300.2000.German.Dubbed.DTSHD.DL.2160p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    21.2000.German.Dubbed.DTSHD.DL.1080p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    In.the.year.2000.before.Christus.2000.German.Dubbed.DTSHD.DL.1080p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    ```

  - **Matches**
    - Full match
        - `Resident.Evil.The.Final.Chapter.2016`
    - Group 0.
        - `The entire match`
    - Group 1.
        - `Resident.Evil.The.Final.Chapter`
    - Group 2.
        - `.Chapter`
    - Group 3.
        - `2016`
        
  - **Explaination**
    - Negative Lookahead `(?!p)`
      - Assert that the Regex below does not match:

        `p matches the character p literally (case sensitive)`

### hd-world.org
`(?<=/)(.*[_|-]1080p)`
- **Test Strings**
    ```
    hdworld/encounters-anmaanthwa_1080p.jpg
    hdworld/encounters-anmaanthwa_1080p.mkv
    hdworld/encounters-anmaanthwa_1080p.nfo
    hdworld/encounters-anmaanthwa_1080p_eng.idx
    hdworld/encounters-anmaanthwa_1080p_eng.sub
    hdworld/encounters-anmaanthwa_1080p_ger.idx
    hdworld/encounters-anmaanthwa_1080p_ger.sub
    hdworld/encounters-anmaanthwa_1080p_ger_forced.idx
    hdworld/encounters-anmaanthwa_1080p_ger_forced.sub
    hdworld/coincidence-avengersendgame-1080p-eng-forced.idx
    hdworld/coincidence-avengersendgame-1080p-eng-forced.sub
    hdworld/coincidence-avengersendgame-1080p-eng.idx
    hdworld/coincidence-avengersendgame-1080p-eng.sub
    hdworld/coincidence-avengersendgame-1080p-ger-forced.idx
    hdworld/coincidence-avengersendgame-1080p-ger-forced.sub
    hdworld/coincidence-avengersendgame-1080p-ger.idx
    hdworld/coincidence-avengersendgame-1080p-ger.sub
    hdworld/coincidence-avengersendgame-1080p.jpg
    hdworld/coincidence-avengersendgame-1080p.mkv
    hdworld/coincidence-avengersendgame-1080p.nfo
    hdworld/d-topas-1080p-eng.idx
    hdworld/d-topas-1080p-eng.sub
    hdworld/d-topas-1080p-forced.idx
    hdworld/d-topas-1080p-forced.sub
    hdworld/d-topas-1080p.idx
    hdworld/d-topas-1080p.sub
    hdworld/gh-psychouncut1080.mkv
    hdworld/gh-psychouncut1080.nfo
    ```

- **Matches**
    ```
    encounters-anmaanthwa_1080p
    coincidence-avengersendgame-1080p
    d-topas-1080p
    ```

    **Notice**: The following strings will have no match.
    ```
    hdworld/gh-psychouncut1080.mkv
    hdworld/gh-psychouncut1080.nfo
    ```

- **Explaination**
  - Positive Lookbehind (?<=/)
    - Assert that the Regex below matches:
      
      `/` matches the character `/` literally (case sensitive)