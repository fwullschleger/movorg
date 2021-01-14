# movorg

## Prerequisites

### Packages
- In order for the script to work the following linux packages need to be installed on the host running the script.
  - `tree`

### Installation
- No Installation is needed in order to execute the script

## Regex
`javascript^(\w+(\.\w+)*)\.([0-9]{4})(?!p)`
  - **Test Strings**
    - Resident.Evil.The.Final.Chapter.2016.German.Dubbed.DTSHD.DL.2160p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    - 300.2000.German.Dubbed.DTSHD.DL.2160p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    - 21.2000.German.Dubbed.DTSHD.DL.1080p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    - In.the.year.2000.before.Christus.2000.German.Dubbed.DTSHD.DL.1080p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    
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
      - Assert that the Regex below does not match
      - p matches the character p literally (case sensitive)
