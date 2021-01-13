# movorg

## Regex explained
`javascript^(\w+(\.\w+)*)\.([0-9]{4})(?!p)`
  - Test Strings
    - Resident.Evil.The.Final.Chapter.2016.German.Dubbed.DTSHD.DL.2160p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    - 300.2000.German.Dubbed.DTSHD.DL.2160p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    - 21.2000.German.Dubbed.DTSHD.DL.1080p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
    - In.the.year.2000.before.Christus.2000.German.Dubbed.DTSHD.DL.1080p.UHD.BluRay.HDR.HEVC.Remux-NIMA4K
  - Explaination
    - Negative Lookahead `(?!p)`
      - Assert that the Regex below does not match
      - p matches the character p literally (case sensitive)
