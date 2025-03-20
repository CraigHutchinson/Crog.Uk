---
layout: post
title:  "Comparison of 5Kw Heat Pumps"
date:   2024-02-15 11:14:02 +0000
modified_date: 2025-03-20 10:52:00 +0000
categories: HeatPump
datatable: true
pinned: false
---

This is a comparison table of all 2024-2025 heat-pump datasheet figures for make+models I am aware of.

Criteria:
- Target property 4-5Kw
- EN 14511/14825 (?) Average Climate and Low temperature = 35C and Medium = 55C
- Ordered by SCOP where higher is better. Where order is ambiguous the SCOP at 45C is used, and then 35C i.e. We prefer mild weather performance which gives greater yearly SCOP.

All SCOP figures are now correlated (i.e. replaced) with MCS 3rd party certified figures where possible. 
Please be aware :broken_heart: currently indicates a device that has not got a verified performance and may not be correctly ranked among others.

<div class="datatable-begin"></div>

| Make/Model              | SCOP@35C | SCOP@45C | SCOP@55C | Gas  | Comment/Validation                                                          | Sound Power Level (dBA) | Date Valid | Wall-Mount | Site/Datasheet |
| [<sup>1</sup>](#k_make) |    | [<sup>3</sup>](#k_45) |   |      | [<sup>2</sup>](#k_std)                                                      |                         |            | [<sup>4</sup>](#k_wall) |                |
| ----------------------: | :------- | :------- | :------- | ---: | --------------------------------------------------------------------------- | :---------------------- | ---------- | ---------- | -------------- |
| `Lambda 8Kw`            | 5.66     | `5.07`   | 4.48     | R290 | :broken_heart: No MCS cert as of 2024-06                                    | 42-56                   | 2024-12    | :x:        | [site](https://lambda-wp.at/luft-waermepumpen/) [datasheet](https://lambda-wp.at/wp-content/uploads/2024/12/20241203_Technisches-Datenblatt_.pdf)|
| `Ovum AC208P`           | 5.53     | `4.89`   | 4.00     | R290 | :broken_heart: No MCS cert as of 2024-06                                    | 41-54.5                 | 2024-07    | :x:        | [site](https://www.ovum.at/en/produkte/luft-die-koenigsklasse/) [datasheet](https://www.ovum.at/wp-content/uploads/2024/07/ACP_Datenblatt_alle_CI2024_web_240703.pdf) |
| `LG ThermaV HM093HF 9Kw` | 5.04    | 3.74     | 3.75     | R290 | :orange_book: MCS `011-1W0831_04` over Datasheet(5.23,`4.49`,3.75)          | 48-49                   | 2024-01    | :x:        | [site](https://www.lg.com/uk/business/heating/air-to-water-heat-pumps/thermav_r290/hm093hfx-ub60-phcs0-encxleu/) [datasheet](https://www.lg.com/uk/lgecs.downloadFile.ldwf?DOC_ID=20240521220550&ORIGINAL_NAME_b1_a1=Webinfo_HM093HFX+UB60_new.pdf&FILE_NAME=Webinfo_HM093HFX+UB60_new%5B20240521124251609%5D.pdf&TC=DwnCmd&GSRI_DOC=GSRI&SPEC_DOWNLOAD=Y) |
| EBac H1A05WG-GB 5Kw     | 4.91     | 4.38     | 3.96     | R32  | :gem: `MCS HP0369/01`                                                       | 64.5                    | 2024-02    | :+1:       | [site](https://www.ebac.com/air-source-heat-pump) [datasheet](https://files.ebac.com/production/default/EBA%E2%80%A2240014_HEATPUMP-DATASHEET_QR_LR_2024-02-10-072606_tqkz.pdf?dm=1707549967) [brochure](https://files.ebac.com/production/default/EBA%E2%80%A2240014_AIR-SOURCE-HEAT-PUMP-E-BROCHURE_HOT-WATER-CYLINDER_LR.pdf?dm=1707549642&_gl=1*13a0crf*_ga*ODYzOTEyOTE1LjE3MDIzODE4NDc.*_ga_6WDFCXQC67*MTcxMDg0OTQxMC4yNC4wLjE3MTA4NDk0MTIuNTguMC4w) |
| Nibe 6kw                | 4.87     | 4.07     | 3.46     | R32  | :orange_book: MCS `012-C700141` over Datasheet(5.08,`4.33`,3.58)            | 53                      | {todo}     | :x:        | [datasheet](https://assetstore.nibe.se/hcms/v2.3/entity/document/874828/storage/ODc0ODI4LzAvbWFzdGVy) |
| Samsung Gen7 5Kw        | 4.84     | 4.14     | 3.43     | R290 | :gem: MCS `011-1W0686_2`                                                    | 55                      | {todo}     | :x:        | [datasheet](https://midsummerwholesale.co.uk/pdfs/samsung-gen-7-r290-datasheet.pdf) |
| Stiebel Eltron WPL-A 07 | 4.66     | 4.21     | 3.69     | R454C | :orange_book: MCS `011-1W0393_02` over Datasheet(4.88, ? , ?)              | 48                      | 2024?      | :x:        | [site](https://www.stiebel-eltron.co.uk/en/products-solutions/renewables/heat_pump/air_water_heat_pumps/wpl-a-05-07-hk-premium/wpl-a-07-hk-230-premium.html) [datasheet](https://www.stiebel-eltron.co.uk/en/products-solutions/renewables/heat_pump/air_water_heat_pumps/wpl-a-05-07-hk-premium/wpl-a-07-hk-230-premium/technical-data.product.pdf) |
| Aira 6KW 1.0            | 4.62     | 4.10     | 3.58     | R290 | :green_book: Source `MCS HP0372/06`                                         | 57                      | 2024-03    | :x:        | [datasheet](https://cms-assets.prod.airahome.com/Installation_Manual_Aira_Outdoor_Unit_Rev1_1_UK_0dbf6a3a3c.pdf) |
| Baxi  5Kw               | 4.77     | 4.06     | 3.39     | R32  | :gem: `MCS HP0033/10`                                                       | 58                      | {todo}     | :x:        | [site](https://www.baxi.co.uk/new-build/products/air-source-heat-pumps/baxi-assure-hp50-ashp) |
| Viessmann 151.A06       | 4.53     | 4.03     | 3.61     | R290 | :green_book: MCS `011-1W0590_06` over Datasheet(4.58,`4.10`,3.61)           | 51                      | {todo}     | :+1:       | [datasheet](https://viessmanndirect.co.uk/files//7a81a248-e65a-4fcf-8735-e4a33fa33fe4/Energy%20Consumption%20Datasheet.pdf) [brochure](https://www.viessmann.co.uk/content/dam/public-brands/gb/products/heat-pump/vitocal-151-a/Vitocal%20150-A_151-A%20brochure.pdf/_jcr_content/renditions/original./Vitocal%20150-A_151-A%20brochure.pdf)|
| Bosch CS5800iAW 5Kw     | 4.53     | 3.90     | 3.28     | R290 | :orange_book: MCS `MCS HP0329/06` over Datasheet(4.65,`4.08`,3.50)          | 42                      | {todo}     | :x:        | [site](https://www.worcester-bosch.co.uk/products/heat-pumps/directory/compress-5800i-aw)  |
| Mitsubishi Ecodan       | 4.42     | 3.90     | 3.53     | R290 | :orange_book: MCS `037-0135-23-1` over Datasheet(4.62,`4.08`,3.53)          |                         | {todo}     | :+1:       | [site](https://library.mitsubishielectric.co.uk/pdf/book/EcodanR290Outdoor1#page-1) |
| Ideal 5Kw               | 4.39     | 3.83     | 3.06     | R32  | :orange_book: MCS `KIWA 00027/023 HP` over Datasheet(5.07,`4.36`,3.65)      | 52                      | 2023-06    | :x:        | [site](https://idealtouch.co.uk.idealboilers.com/products/logic-air-heat-pump-3) |
| Vaillant aroTherm+ 5Kw  | 4.48     | 3.77     | 3.06     | R290 | :gem: `KIWA 00016/018HP`                                                    | 51-55                   | {todo}     | :+1:       | [datasheet](https://professional.vaillant.co.uk/downloads/aproducts/renewables-1/arotherm-plus/arotherm-plus-spec-sheet-1892564.pdf) |
| Daikin Altherma 4Kw     | 4.43     | 3.72     | 3.20     | R32  | :green_book: MCS `011-1W0527_3` over Datasheet(4.48,`3.87`,3.26)            | 60                      | {todo}     |            | [site](https://www.daikin.co.uk/en_gb/products/product.table.html/EDLA04-08E3V3.html) |
| Octopus Cosy 6          | 3.98     | 3.36     | 3.06     | R290 | :green_book: `MCS HP0255/03`                                                | 53.8                    | 2024-05    | :x:        | [datsheet](https://26119526.fs1.hubspotusercontent-eu1.net/hubfs/26119526/Cosy%206-overview-vol%201.pdf). MCS database source https://mcscertified.com/product-directory/ |
| CTC Ecoair 700M         | ????     | ????     | ????     | R290 | :broken_heart: No MCS cert or data of any SCOP kind as of 2024-03           | 46                      | 2024-03    |            | [site](https://ctc-heating.com/products/air-to-water-heat-pumps/ctc-ecoair-700m). |
| Wonderwall DR-HP-006-UK | ????     | ????     | ????     | R290 | :broken_heart: No MCS cert or data of any SCOP kind as of 2024-03           | 60                      | 2024-03    |            | [datsheet](https://wondrwall.com/wp-content/uploads/2024/11/WW-Air-Source-Heat-Pump-Datasheet.pdf). |

><sup id="k_make">1</sup>`Make/Model` = models may cycle due to being oversized i.e. 8KW+
>
><sup id="k_std">2</sup> :gem: = Datasheet-matches-MCS, :green_book: = MCS-only-or-close-match, :orange_book: = MCS-not-close-to-datasheet, :broken_heart: = Not validated/Unknown
>
><sup id="k_45">3</sup>```1.23``` = SCOP at 45C calculated as MEAN(35,55) when not made available in datasheet.
>      This produces conservative underestimate of SCOP when unavailable.
>
><sup id="k_wall">4</sup>Only if directly shown in datasheet, many, if not all could be wall mounted, but not directly mentioned in datasheet.

<div class="datatable-end"></div>

ToDo:
- Add Wonderwall DR-HP-006-UK  https://wondrwall.com/products/air-source-heat-pump/#technical-specifications
- Add CTC Ecoair 700M https://ctc-heating.com/products/air-to-water-heat-pumps/ctc-ecoair-700m

Changes:
- Fix data-entry error on Ebac 45C 4.63 to 4.38 (down to 4th)
- 2024-02 Ovum AC208P from `5.78` to `5.53` @ 35C, `4.15` to `4.00` @ 55C etc. [old-datasheet](https://www.ovum.at/wp-content/uploads/2023/10/ACP_Datenblatt_alle_Web_230928.pdf)
- 2024-02 EBac H1A05WG-GB from `5.11` to `4.91` @ 35C, `4.12` to `3.96` @ 55C  [old-datasheet](https://ebac-serverless.files.svdcdn.com/production/default/EBA%E2%80%A2230341_AIR-SOURCE-HEAT-PUMP-E-BROCHURE_HOT-WATER-CYLINDER.pdf?dm=1695277753) 
- 2024-04-25 Added `Aira 6KW 1.0` with SCOP figures from MCS Product Database
- 2024-06-03 Added `Octopus Cosy 6` with SCOP figures from MCS Product Database
- 2024-06-10 Remove inconsistent standard in favour of 3rd party MCS correlation for SCOP accuracy, devices re-ordered respectively
- 2024-12-11 Added Sound Power LEvel (dBa) + add `Stiebel Eltron`
- 2024-12-12 Added MCS figures for `Bosch CS5800iAW  5Kw` and `LG Therma V 9Kw`
- 2025-03 Preliminary entry of Wonderwall DR-HP-006-UK